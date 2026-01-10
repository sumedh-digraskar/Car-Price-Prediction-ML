import streamlit as st
import joblib
import numpy as np

model = joblib.load("car_price_model.pkl")

st.title("🚗 Car Price Prediction")

year = st.number_input("Car Year", min_value=1990, max_value=2026)
km = st.number_input("Kilometers Driven")
fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])

fuel_map = {"Petrol": 0, "Diesel": 1, "CNG": 2}

if st.button("Predict"):
    features = np.array([[year, km, fuel_map[fuel]]])
    price = model.predict(features)
    st.success(f"Estimated Price: ₹ {int(price[0])}")
