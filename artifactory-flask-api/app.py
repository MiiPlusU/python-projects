#!/usr/bin/env python3
import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request, Response, stream_with_context
import requests
from model import db, ArtifactLog

load_dotenv()

ARTIFACTORY_TOKEN = os.getenv('ARTIFACTORY_TOKEN')
ARTIFACTORY_REPO = os.getenv('ARTIFACTORY_REPO')
ARTIFACTORY_BASE_URL = os.getenv('ARTIFACTORY_BASE_URL')

header = {
    'Authorization': f'Bearer {ARTIFACTORY_TOKEN}'
}

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


def log_artifact_event(artifact_path: str, action: str):

    try:
        log = ArtifactLog(artifact_path=artifact_path, action=action)
        db.session.add(log)
        db.session.commit()
    except Exception:
        db.session.rollback()
        app.logger.exception("Failed to log artifact event")


@app.route('/artifacts', methods=['GET'])
def get_artifacts():
    prefix = request.args.get("prefix", "").strip("/")
    limit = request.args.get("limit", type=int)

    if ".." in prefix:
        return jsonify({"error": "invalid prefix"}), 400

    storage_url = f"{ARTIFACTORY_BASE_URL}/api/storage/{ARTIFACTORY_REPO}/"
    if prefix:
        storage_url += f"{prefix}/"

    response = requests.get(url=storage_url, headers=header, timeout=10)

    if response.status_code != 200:
        return jsonify({'error': 'failed to read file'}), response.status_code

    json_response = response.json()
    data = []

    for child in json_response.get('children', []):
        if not child:
            continue

        name = child['uri'].lstrip('/')
        if prefix:
            uri = f"{prefix}/{name}"
        else:
            uri = name

        data.append({
            "name": name,
            "uri": uri
        })

    if limit is not None:
        data = data[:limit]

    return jsonify(data), 200


@app.route('/artifacts/<path:artifact_path>', methods=['GET'])
def download_artifacts(artifact_path: str):

    if artifact_path.startswith('/') or '..' in artifact_path:
        return jsonify({'error': 'invalid artifact path'}), 400

    response = requests.get(
        url=f'{ARTIFACTORY_BASE_URL}/{ARTIFACTORY_REPO}/{artifact_path}',
        headers=header,
        timeout=10,
        stream=True
    )

    if response.status_code == 404:
        return jsonify({"error": "not found"}), 404

    if response.status_code in (401, 403):
        return jsonify({"error": "unauthorized"}), response.status_code

    if response.status_code != 200:
        return jsonify({"error": "upstream error"}), response.status_code

    content_type = response.headers.get("Content-Type", "application/octet-stream")
    stream_response = stream_with_context(response.iter_content(chunk_size=8192))

    log_artifact_event(artifact_path, "download")
    return Response(stream_response, content_type=content_type)


@app.route('/artifacts/<path:artifact_path>', methods=['POST'])
def upload_artifacts(artifact_path: str):
    if artifact_path.startswith('/') or '..' in artifact_path:
        return jsonify({'error': 'invalid artifact path'}), 400

    data = request.get_data()

    upload_url = f'{ARTIFACTORY_BASE_URL}/{ARTIFACTORY_REPO}/{artifact_path}'
    response = requests.put(url=upload_url, headers=header, data=data, timeout=10)

    if response.status_code not in (200, 201):
        return jsonify({
            'error': 'failed to upload file',
            'response': response.text
        }), response.status_code

    json_response = {
        'message': 'File uploaded successfully',
        'path': artifact_path,
        'size': len(data)
    }

    log_artifact_event(artifact_path, "upload")
    return jsonify(json_response), 201


@app.route('/artifacts/<path:artifact_path>', methods=['DELETE'])
def delete_artifacts(artifact_path: str):

    if artifact_path.startswith('/') or '..' in artifact_path:
        return jsonify({'error': 'invalid artifact path'}), 400

    response = requests.delete(
        url=f'{ARTIFACTORY_BASE_URL}/{ARTIFACTORY_REPO}/{artifact_path}',
        headers=header,
        timeout=10
    )

    if response.status_code == 404:
        return jsonify({"error": "not found"}), 404

    if response.status_code in (401, 403):
        return jsonify({"error": "unauthorized"}), response.status_code

    if response.status_code not in (200, 204):
        return jsonify({"error": "upstream error"}), response.status_code

    log_artifact_event(artifact_path, "delete")
    return Response(status=204)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
