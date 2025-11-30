from flask import Flask, request, jsonify
from ml_model import load_data, split_data, train_model, predict_single

app = Flask(__name__)
df = load_data()
X_train, X_test, y_train, y_test = split_data(df)
MODEL = train_model(X_train, y_train)


@app.route("/predict", methods=["POST"])
def predict_churn():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Request body must be a JSON object"}), 400

    required_fields = {"tenure_months", "monthly_charges", "contract_type"}
    missing = required_fields - set(data.keys())
    if missing:
        return jsonify({"error": f"Missing fields: {', '.join(missing)}"}), 400
    
    if not isinstance(data["tenure_months"], (int, float)):
        return jsonify({"error": "tenure_months must be a number"}), 400

    if not isinstance(data["monthly_charges"], (int, float)):
        return jsonify({"error": "monthly_charges must be a number"}), 400

    if not isinstance(data["contract_type"], str):
        return jsonify({"error": "contract_type must be a string"}), 400

    if data["contract_type"] not in {"month-to-month", "annual"}:
        return jsonify({"error": "contract_type must be 'month-to-month' or 'annual'"}), 400
    
    result = predict_single(MODEL, data)

    label_text = "churn" if result["prediction"] == 1 else "no_churn"

    return jsonify({
        "churn_probability": result["churn_probability"],
        "prediction": label_text
    }), 200



@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200