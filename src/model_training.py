import joblib
from sklearn.ensemble import IsolationForest
from .data_preprocessing import preprocess_data

def train_model(df, save_path="models/isolation_forest.pkl"):
    X, scaler, processed_df = preprocess_data(df)

    # Train Isolation Forest
    model = IsolationForest(contamination=0.01, random_state=42)
    model.fit(X)

    # Save model & scaler
    joblib.dump((model, scaler, processed_df.columns), save_path)
    print(f"Model saved at {save_path}")
    return model, scaler
