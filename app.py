import streamlit as st
import numpy as np
import joblib

# Load Trained Model
model = joblib.load("cancer_therapy_model.pkl")

# UI for User Input
st.title("🔬 AI-Guided Personalized Cancer Therapy Recommender")

st.sidebar.header("🧬 Patient Biomarker Data Input")
tmb = st.sidebar.selectbox("Tumor Mutation Burden (TMB)", ["Low", "High"])
pd_l1 = st.sidebar.selectbox("PD-L1 Expression", ["Negative", "Positive"])
msi = st.sidebar.selectbox("MSI Status", ["Stable", "Unstable"])

# Convert Input to Numerical Format
input_data = np.array([[2 if tmb == "High" else 1, 1 if pd_l1 == "Positive" else 0, 1 if msi == "Unstable" else 0]])

# Predict Therapy
if st.sidebar.button("Predict Therapy"):
    prediction = model.predict(input_data)[0]
    therapies = ["Checkpoint Inhibitors", "CAR-T Therapy", "Personalized Cancer Vaccine"]
    st.success(f"✅ Recommended Therapy: *{therapies[prediction]}*")