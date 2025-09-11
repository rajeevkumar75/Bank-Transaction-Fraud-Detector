import pandas as pd
import joblib

def predict_transaction(transaction, model_path="models/isolation_forest.pkl"):
    model, scaler, columns = joblib.load(model_path)

    # Create input dataframe
    df = pd.DataFrame([transaction])

    # One-hot encode input
    df = pd.get_dummies(df, columns=['Type', 'Location'], dummy_na=True)
    df = df.reindex(columns=columns.drop(['TransactionID', 'IsFraud'], errors='ignore'), fill_value=0)

    # Scale
    input_scaled = scaler.transform(df)

    # Prediction
    score = model.predict(input_scaled)[0]
    result = "Fraudulent Transaction Detected" if score == -1 else "Transaction is Legitimate"
    return result
