# 📘 Artifactory + Flask API

A production-style Flask API for uploading, downloading, listing, and deleting artifacts in JFrog Artifactory, with PostgreSQL logging and full unit test coverage.

Built as a learning + professional portfolio project by Mariama Sesay.

## 🚀 Features

### 🔹 REST API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/artifacts` | List all artifacts in the Artifactory repo |
| `GET` | `/artifacts/<path>` | Download a single artifact (streamed) |
| `POST` | `/artifacts/<path>` | Upload a file to Artifactory |
| `DELETE` | `/artifacts/<path>` | Delete an artifact |

### 🔹 Security & Validation

- Prevents path traversal (`..`, leading slash)
- Uses Bearer token authentication
- Protects secret credentials using `.env`

### 🔹 PostgreSQL Logging

Every upload/download/delete is logged via SQLAlchemy into a Postgres DB.

### 🔹 Unit Tests (pytest)

- Mock-based testing of Artifactory responses
- Full success-path and error-path coverage
- No real network calls

## 🛠️ Technology Stack

- Python 3.10+
- Flask
- SQLAlchemy
- PostgreSQL
- pytest
- requests
- Artifactory REST API

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/<your-username>/artifactory-flask-api.git
   cd artifactory-flask-api
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate     # Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🔐 Environment Setup

1. **Copy the example file:**
   ```bash
   cp .env.example .env
   ```

2. **Fill in your Artifactory + Postgres values.**

## ▶️ Running the API

```bash
flask run --host 0.0.0.0 --port 5000
```

Or using python:
```bash
python app.py
```

## 🧪 Running Tests

```bash
pytest -v
```

Tests use monkeypatch to mock:
- Artifactory requests
- Upstream errors
- Success responses

So the test suite runs fully offline.

## 📁 Project Structure

```
├── app.py               # Main Flask application
├── model.py             # SQLAlchemy models
├── test_app.py          # Unit tests (pytest)
├── .env.example         # Environment variable template
├── requirements.txt     # Python dependencies
├── .gitignore           # Excludes secrets / cache / venv
└── README.md            # Project documentation
```

## ✨ Future Improvements

- Add pagination + sorting
- Add `/logs` endpoint for viewing DB logs
- Add GitHub Actions CI pipeline
- Add user authentication (JWT)
- Add file-size limits + MIME validation