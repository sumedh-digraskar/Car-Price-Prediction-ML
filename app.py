import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("car_price_model.pkl")

st.set_page_config(page_title="Car Price Prediction", page_icon="🚗")
st.title("🚗 Car Price Prediction")
st.write("Enter car details below to predict price:")

# Create array of zeros with 49 features
features = np.zeros(49)

# Example numeric inputs
features[0] = st.number_input("Symboling", value=0)
features[3] = st.number_input("Car Length (in inches)", value=150)
features[6] = st.number_input("Curb Weight (in lbs)", value=2000)
features[8] = st.number_input("Engine Size", value=100)
features[13] = st.number_input("Horsepower", value=70)

# Categorical inputs (one-hot)
fuel = st.selectbox("Fuel Type", ["Gas", "Diesel"])
if fuel == "Gas":
    features[16] = 1
elif fuel == "Diesel":
    features[15] = 1

carbody = st.selectbox("Car Body Type", ["Sedan", "Hatchback", "Wagon", "Convertible", "Hardtop"])
if carbody == "Sedan":
    features[21] = 1
elif carbody == "Hatchback":
    features[20] = 1
elif carbody == "Wagon":
    features[23] = 1
elif carbody == "Convertible":
    features[18] = 1
elif carbody == "Hardtop":
    features[19] = 1

# Predict button
if st.button("Predict Price"):
    predicted_price = model.predict([features])
    st.success(f"💰 Estimated Price: ${int(predicted_price[0])}")
    st.balloons()

