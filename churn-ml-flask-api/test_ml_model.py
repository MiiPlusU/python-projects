import pandas as pd
from ml_model import load_data, split_data, preprocess_features, train_model, evaluate_model, predict_single


def test_load_data_structure():

    df = load_data()
    assert isinstance(df, pd.DataFrame)
    assert set(["tenure_months", "monthly_charges", "contract_type", "churn"]).issubset(df.columns)
    assert len(df) >= 8

def test_split_data_shapes():

    df = load_data()
    X_train, X_test, y_train, y_test = split_data(df)


    assert('churn' not in X_train.columns)
    assert(len(X_train) + len(X_test) == len(df))
    assert(len(X_train) > len(X_test))

def test_train_model_can_predict():
    df = load_data()
    X_train, X_test, y_train, y_test = split_data(df)

    X_train_processed = preprocess_features(X_train)
    assert isinstance(X_train_processed, pd.DataFrame)
    assert X_train_processed['contract_type'].dtype == 'int64'

    model = train_model(X_train, y_train)

    X_test_processed = preprocess_features(X_test)
    y_pred = model.predict(X_test_processed)
    assert len(y_pred) == len(X_test)
    assert set(y_pred).issubset({0, 1})

def test_evaluate_model_returns_reasonable_accuracy():
    df = load_data()
    X_train, X_test, y_train, y_test = split_data(df)
    model = train_model(X_train, y_train)
    acc = evaluate_model(model, X_test, y_test)
    assert 0.0 <= acc <= 1.0
    assert acc >= 0.5

def test_predict_single_churny_customer():
    df = load_data()
    X_train, X_test, y_train, y_test = split_data(df)
    model = train_model(X_train, y_train)

    customer = {
        "tenure_months": 2,
        "monthly_charges": 90.0,
        "contract_type": "month-to-month",
    }

    result = predict_single(model, customer)

    assert 0.0 <= result["churn_probability"] <= 1.0
    assert result["prediction"] in (0, 1)
    assert result["churn_probability"] > 0.5

def test_predict_single_loyal_customer():
    df = load_data()
    X_train, X_test, y_train, y_test = split_data(df)
    model = train_model(X_train, y_train)
    customer = {
        "tenure_months": 72,
        "monthly_charges": 30.0,
        "contract_type": "annual",
    }

    result = predict_single(model, customer)

    assert 0.0 <= result["churn_probability"] <= 1.0
    assert result["prediction"] in (0, 1)
    assert result["churn_probability"] < 0.5

def test_health_ok(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}

def test_predict_happy_path(client):
    payload = {
        "tenure_months": 2,
        "monthly_charges": 90.0,
        "contract_type": "month-to-month",
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200
    data = response.get_json()
    assert "churn_probability" in data
    assert "prediction" in data
    assert 0.0 <= data["churn_probability"] <= 1.0
    assert data["prediction"] in ("churn", "no_churn")

def test_predict_missing_fields(client):
    payload = {
        "tenure_months": 2,
        # "monthly_charges": 90.0,
        "contract_type": "month-to-month",
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data

