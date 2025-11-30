# Churn Prediction API (Flask + ML)

This project is a small learning-focused API that uses a machine learning model
(Logistic Regression) to predict customer churn based on simple features.

## What It Does

The API takes customer information (tenure, monthly charges, contract type) and predicts:
- **Churn probability** (0.0 to 1.0) - likelihood the customer will leave
- **Prediction** ("churn" or "no_churn") - binary decision based on 50% threshold

I built it to learn the foundations of:

- Machine learning basics (train/test split, logistic regression, evaluation)
- Feature preprocessing (handling categorical features)
- Building a Flask API around an ML model
- Writing unit tests for both ML code and API endpoints with pytest

---

## Tech Stack

- Python
- Flask
- scikit-learn
- pandas
- pytest

---

## Project Structure

```text
.
├── app.py            # Flask API ( /health and /predict )
├── ml_model.py       # ML pipeline (data, split, preprocess, train, predict)
├── conftest.py       # pytest fixtures (test client setup)
├── test_ml_model.py  # tests for ML functions
├── test_app.py       # tests for API endpoints
├── requirements.txt
├── README.md
├── .gitignore
```


---

## How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/<your-username>/churn-ml-flask-api.git
cd churn-ml-flask-api

# 2. Create & activate virtual env (optional but recommended)
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run tests
pytest -v

# 5. Start the Flask app
python app.py
```

---

## API Usage

### Health Check
```bash
curl http://localhost:5000/health
```
**Response:**
```json
{"status": "ok"}
```

### Predict Churn
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "tenure_months": 2,
    "monthly_charges": 90.0,
    "contract_type": "month-to-month"
  }'
```

**Response:**
```json
{
  "churn_probability": 0.85,
  "prediction": "churn"
}
```

### Input Parameters
- `tenure_months` (int): How long customer has been with company
- `monthly_charges` (float): Monthly bill amount
- `contract_type` (string): Either "month-to-month" or "annual"

---

## Model Details

- **Algorithm**: Logistic Regression
- **Features**: 3 (tenure, charges, contract type)
- **Training Data**: 25 synthetic customer records with clear churn patterns
- **Accuracy**: Typically 80%+ on test set

The model learns that customers with short tenure, high charges, and month-to-month contracts are more likely to churn.
