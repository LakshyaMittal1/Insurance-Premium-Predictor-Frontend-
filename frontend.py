import streamlit as st
import requests
import os

from dotenv import load_dotenv
load_dotenv()

# API_URL = "http://127.0.0.1:8000/predict" # The URL where the FastAPI server is running

# For local use, we can read from .env; for Streamlit Cloud, it comes from st.secrets
API_URL = os.getenv("API_URL") or st.secrets["API_URL"]

st.title("Insurance Premium Category Predictor")
st.markdown("Enter your details below:")

# Input Fields

age = st.number_input("Age", min_value=1, max_value=119, value=30)
weight = st.number_input("Weight (Kg)", min_value=1.0, value=65.0)
height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, value=1.7)
income_lpa = st.number_input("Annual Income (LPA)", min_value=0.1, value=10.0)
smoker = st.selectbox("Are you a Smoker?", options=[True, False])
city = st.text_input("City", value="Rajasthan")
occupation = st.selectbox("Occupation", ['retired', 'freelancer', 'government_job', 'business_owner', 'unemployed', 'private_job'])

if st.button("Predict Premium Category"):
    input_data = {
        'age': age,
        'weight': weight,
        'height': height,
        'income_lpa': income_lpa,
        'smoker': smoker,
        'city': city,
        'occupation': occupation
    }

    
    try:
        response = requests.post(API_URL, json=input_data)
        result = response.json()
        if response.status_code==200:
            st.success(f"Predicted Insurance Premium Category:  **{result['response']}**")
        else:
            st.error('API Error: {response.status_code} - {response.text}')
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to the FastAPI server. Make sure it's running on port 8000.")