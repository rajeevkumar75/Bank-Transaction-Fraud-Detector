import streamlit as st
import pandas as pd
import joblib
from src.model_training import train_model
from src.prediction import predict_transaction

st.title("💳 Bank Transaction Fraud Detector")
st.write("An AI-based system to detect suspicious banking transactions.")

# Upload dataset
uploaded_file = st.file_uploader("Upload Transaction Dataset (CSV)", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("📂 Sample Data")
    st.dataframe(df.head())

    if st.button("Train Fraud Detection Model"):
        model, scaler = train_model(df)
        st.success("✅ Model trained and saved successfully!")

# Real-time prediction
st.subheader("🔎 Real-Time Transaction Check")
amount = st.number_input("Amount", value=0)
txn_type = st.selectbox("Type", ["Online", "ATM", "POS", "Other"])
location = st.text_input("Location", "Unknown")

if st.button("Detect Fraud"):
    transaction = {
        "TransactionID": "T_new",
        "Amount": amount,
        "Type": txn_type,
        "Location": location
    }
    result = predict_transaction(transaction)
    st.write(f"**Prediction:** {result}")
