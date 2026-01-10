import streamlit as st
import joblib
import numpy as np

model = joblib.load("car_price_model.pkl")

st.set_page_config(page_title="Car Price Prediction", page_icon="🚗")
st.title("🚗 Car Price Prediction")
st.write("Simple car price predictor")

# Model expects 49 features
features = np.zeros(49)

# USER INPUTS
kms = st.number_input("Kilometers Driven", min_value=0, max_value=300000, value=40000)
horsepower = st.number_input("Horsepower", min_value=50, max_value=500, value=100)
fuel = st.selectbox("Fuel Type", ["Gas", "Diesel"])

# ---- Feature Mapping ----
features[0] = kms / 10000        # proxy usage impact
features[13] = horsepower        # horsepower

if fuel == "Gas":
    features[16] = 1
else:
    features[15] = 1

# Prediction
if st.button("Predict Price"):
    price = model.predict([features])[0]
    st.success(f"💰 Estimated Price: ₹ {int(price):,}")


