import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def load_data():
    data = [
        # High churn patterns: Short tenure + High charges + Month-to-month
        {"tenure_months": 1, "monthly_charges": 95.0, "contract_type": "month-to-month", "churn": 1},
        {"tenure_months": 2, "monthly_charges": 89.0, "contract_type": "month-to-month", "churn": 1},
        {"tenure_months": 3, "monthly_charges": 92.0, "contract_type": "month-to-month", "churn": 1},
        {"tenure_months": 4, "monthly_charges": 87.0, "contract_type": "month-to-month", "churn": 1},
        {"tenure_months": 5, "monthly_charges": 91.0, "contract_type": "month-to-month", "churn": 1},
        {"tenure_months": 6, "monthly_charges": 88.0, "contract_type": "month-to-month", "churn": 1},
        
        # Medium churn risk: Medium tenure + Medium charges + Month-to-month
        {"tenure_months": 8, "monthly_charges": 65.0, "contract_type": "month-to-month", "churn": 1},
        {"tenure_months": 10, "monthly_charges": 70.0, "contract_type": "month-to-month", "churn": 1},
        {"tenure_months": 12, "monthly_charges": 68.0, "contract_type": "month-to-month", "churn": 0},
        {"tenure_months": 15, "monthly_charges": 72.0, "contract_type": "month-to-month", "churn": 1},
        
        # Low churn patterns: Long tenure + Low-medium charges + Annual contracts
        {"tenure_months": 24, "monthly_charges": 45.0, "contract_type": "annual", "churn": 0},
        {"tenure_months": 30, "monthly_charges": 42.0, "contract_type": "annual", "churn": 0},
        {"tenure_months": 36, "monthly_charges": 38.0, "contract_type": "annual", "churn": 0},
        {"tenure_months": 42, "monthly_charges": 40.0, "contract_type": "annual", "churn": 0},
        {"tenure_months": 48, "monthly_charges": 35.0, "contract_type": "annual", "churn": 0},
        {"tenure_months": 60, "monthly_charges": 32.0, "contract_type": "annual", "churn": 0},
        
        # Very low churn: Very long tenure customers (loyal customers)
        {"tenure_months": 72, "monthly_charges": 30.0, "contract_type": "annual", "churn": 0},
        {"tenure_months": 84, "monthly_charges": 28.0, "contract_type": "annual", "churn": 0},
        {"tenure_months": 96, "monthly_charges": 25.0, "contract_type": "annual", "churn": 0},
        
        # Edge cases: High charges but long tenure (satisfied premium customers)
        {"tenure_months": 54, "monthly_charges": 85.0, "contract_type": "annual", "churn": 0},
        {"tenure_months": 66, "monthly_charges": 82.0, "contract_type": "annual", "churn": 0},
        
        # Edge cases: Low charges but short tenure (still churning due to other factors)
        {"tenure_months": 3, "monthly_charges": 25.0, "contract_type": "month-to-month", "churn": 1},
        {"tenure_months": 5, "monthly_charges": 22.0, "contract_type": "month-to-month", "churn": 1},
        
        # Borderline cases for learning
        {"tenure_months": 18, "monthly_charges": 55.0, "contract_type": "month-to-month", "churn": 0},
        {"tenure_months": 20, "monthly_charges": 58.0, "contract_type": "month-to-month", "churn": 1},
    ]
    return pd.DataFrame(data)

def split_data(df):
    # removes churn column, axis=0 removes churn rows
    X = df.drop("churn", axis=1)
    y = df["churn"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=.2, random_state=42
    )
    return X_train, X_test, y_train, y_test


def preprocess_features(X):
    X_processed = X.copy()
    mapping = {"month-to-month": 0, "annual": 1}
    X_processed["contract_type"] = X_processed["contract_type"].map(mapping)
    return X_processed


def train_model(X_train, y_train):
    X_train_processed = preprocess_features(X_train)
    model = LogisticRegression()
    model.fit(X_train_processed, y_train)
    return model
 
def evaluate_model(model, X_test, y_test):
    X_test_preprocessed = preprocess_features(X_test)
    y_pred = model.predict(X_test_preprocessed)
    acc = accuracy_score(y_test, y_pred)
    return acc

def predict_single(model, customer_features: dict):
    df = pd.DataFrame([customer_features])
    df_processed = preprocess_features(df)

    df_processed = df_processed[model.feature_names_in_]

    
    probabilities = model.predict_proba(df_processed)
    probability = probabilities[0, 1] 
    
    label = int(probability >= 0.5)
    return {"churn_probability": float(probability), "prediction": label}






