import streamlit as st
import pandas as pd
import joblib

# Load model and feature list
model, features = joblib.load("xgb_simple_model.pkl")

st.title("📊 Credit Default Risk Predictor")

# Input fields
age = st.slider("Age", 18, 70, 30)
income = st.number_input("Annual Income", value=100000)
credit = st.number_input("Loan Amount", value=200000)
source2 = st.slider("EXT_SOURCE_2", 0.0, 1.0, 0.5)
source3 = st.slider("EXT_SOURCE_3", 0.0, 1.0, 0.5)

# Prepare input DataFrame
X_input = pd.DataFrame([{
    "AGE_YEARS": age,
    "AMT_INCOME_TOTAL": income,
    "AMT_CREDIT": credit,
    "EXT_SOURCE_2": source2,
    "EXT_SOURCE_3": source3,
}])[features]

# Predict
if st.button("Predict"):
    prob = model.predict_proba(X_input)[0][1]
    st.markdown(f"### 🧮 Predicted Default Risk: **{prob:.2%}**")
