import streamlit as st
import joblib
import pandas as pd
import numpy as np

# 1. Load your model and scaler
model = joblib.load("random_forest_model.pkl")
scaler = joblib.load("scaler.pkl")

# 2. Setup the UI
st.title("🛡️ Credit Card Fraud Detector")
st.write("Enter transaction details below to check for fraud.")

# 3. Create input fields (matching your notebook features)
col1, col2 = st.columns(2)

with col1:
    step = st.number_input("Step (Hour of transaction)", value=1)
    amount = st.number_input("Transaction Amount", value=0.0)
    oldbalanceOrg = st.number_input("Sender Old Balance", value=0.0)

with col2:
    newbalanceOrig = st.number_input("Sender New Balance", value=0.0)
    oldbalanceDest = st.number_input("Receiver Old Balance", value=0.0)
    newbalanceDest = st.number_input("Receiver New Balance", value=0.0)

# 4. Predict button
if st.button("Analyze Transaction"):
    # Create a dataframe for the input
    input_df = pd.DataFrame([{
        'step': step,
        'amount': amount,
        'oldbalanceOrg': oldbalanceOrg,
        'newbalanceOrig': newbalanceOrig,
        'oldbalanceDest': oldbalanceDest,
        'newbalanceDest': newbalanceDest
    }])
    
    # Scale and Predict
    scaled_data = scaler.transform(input_df)
    prediction = model.predict(scaled_data)[0]
    
    # Show results
    if prediction == 1:
        st.error("🚨 ALERT: This transaction is flagged as FRAUD!")
    else:
        st.success("✅ Safe: This transaction appears legitimate.")