# 🚗 Car Price Prediction using Machine Learning

## 📌 Project Overview
This project focuses on predicting car prices based on various technical and categorical features using multiple machine learning regression algorithms.  
The goal is to build an end-to-end ML pipeline including data cleaning, feature engineering, exploratory data analysis (EDA), model training, evaluation, and hyperparameter tuning.

---

## 📂 Dataset
- Source: Automobile / Car Price Dataset
- Target Variable: `price`
- Total Features:
  - Numerical features (engine size, horsepower, curb weight, etc.)
  - Categorical features (fuel type, car body, drive wheel, engine type, fuel system, etc.)

---

## 🔍 Exploratory Data Analysis (EDA)
- Analyzed price distribution and detected skewness
- Studied relationship between price and numerical features using:
  - Histograms
  - Boxplots
  - Scatter plots
- Used correlation heatmap to analyze multicollinearity
- Identified and handled outliers

---

## 🛠 Feature Engineering
- Dropped `carname` column due to high cardinality and redundant information
- Applied:
  - **One-Hot Encoding** for nominal categorical features:
    - `fueltype`, `carbody`, `drivewheel`, `enginelocation`,
      `enginetype`, `fuelsystem`, `aspiration`
  - **Manual Mapping** for ordinal features:
    - `doornumber` → converted to integer
    - `cylindernumber` → converted to integer
- Scaled features where required (for SVR)

---

## 🤖 Models Implemented
- Linear Regression
- Support Vector Regressor (SVR)
- Decision Tree Regressor
- Random Forest Regressor

---

## 📊 Model Performance

| Model            | R² Score | MAE |
|------------------|----------|-----|
| Linear Regression| 0.46     | 2309 |
| SVR              | -0.01    | 3754 |
| Decision Tree    | 0.74     | 1540 |
| Random Forest    | **0.87** | **1180** |

✔ Random Forest performed best.

---

## 🔧 Hyperparameter Tuning
- Used `RandomizedSearchCV` on Random Forest
- Improved performance slightly after tuning

---

## 📁 Project Structure
