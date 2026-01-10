import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("car_price_model.pkl")

# Streamlit UI
st.set_page_config(page_title="Car Price Prediction", page_icon="🚗")
st.title("🚗 Car Price Prediction")
st.write("Predict your car price with just a few details!")

# Create array of zeros (49 features)
features = np.zeros(49)

# ===== USER INPUTS =====
kms = st.number_input("Kilometers Driven", min_value=0, max_value=300000, value=40000)
horsepower = st.number_input("Horsepower", min_value=50, max_value=500, value=100)
fuel = st.selectbox("Fuel Type", ["Gas", "Diesel"])

# ===== MAP USER INPUTS TO MODEL FEATURE INDICES =====
# Note: fill only the corresponding indices, rest stay 0
features[0] = kms / 10000       # Example mapping to 'symboling' as proxy
features[13] = horsepower       # 'horsepower'
if fuel == "Gas":
    features[16] = 1            # fueltype_gas
else:
    features[15] = 1            # fueltype_diesel

# ===== PREDICT BUTTON =====
if st.button("Predict Price"):
    predicted_price = model.predict([features])[0]
    st.success(f"💰 Estimated Price: ₹ {int(predicted_price):,}")
    st.balloons()
