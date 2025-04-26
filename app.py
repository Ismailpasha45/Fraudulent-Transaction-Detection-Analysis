import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ✅ Correctly load model and scaler
model = joblib.load('fraud_detection_model.pkl')
scaler = joblib.load('scaler.pkl')

st.title("🚨 Fraud Transaction Detection App")

amount = st.number_input('Transaction Amount ($)', min_value=0.0)
time_seconds = st.number_input('Transaction Time (seconds)', min_value=0, max_value=86400)
day = st.number_input('Transaction Day (number)', min_value=0)

# Create input DataFrame
input_df = pd.DataFrame({
    'TX_AMOUNT': [amount],
    'TX_TIME_SECONDS': [time_seconds],
    'TX_TIME_DAYS': [day]
})

# Scale input
scaled_input = scaler.transform(input_df)

# Predict
prediction = model.predict(scaled_input)

# Show result
result = "🛑 Fraudulent Transaction" if prediction[0] == 1 else "✅ Legitimate Transaction"
st.subheader(f"🔍 Prediction Result: {result}")
