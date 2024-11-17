import streamlit as st
import joblib
import numpy as np

# Assume the second model is a RandomForestRegressor saved using joblib
random_forest_model = joblib.load('trained_models/random_forest_model.joblib')  # Load Random Forest model
linear_reg_model = joblib.load('trained_models/linear_regression_model.joblib')  # Load linear regression model


# Streamlit UI to input features
st.title("Stock Price Prediction")

# Dropdown for model selection
model_choice = st.selectbox('Select Model', ['Linear Regression', 'Random Forest'])

# # Select stock ticker
# ticker = st.selectbox('Select Ticker', ['KRP', 'AP', 'AAPL', 'GOOG'])

# Create a grid using columns
col1, col2, col3 = st.columns(3)

with col1:
    open_price = st.number_input('Open Price')
    volume = st.number_input('Volume')

with col2:
    high_price = st.number_input('High Price')
    dividends = st.number_input('Dividends')

with col3:
    low_price = st.number_input('Low Price')
    stock_splits = st.number_input('Stock Splits')

# Calculate the Price Change and Volatility automatically
price_change = open_price - high_price  # Calculate the price change
volatility = high_price - low_price  # Calculate the volatility

# Prepare the input data for prediction
input_data = np.array([[open_price, high_price, low_price, volume, dividends, stock_splits, price_change, volatility]])

# Make prediction based on selected model
if st.button('Predict'):
    if model_choice == 'Linear Regression':
        # Predict using CatBoost model
        prediction = linear_reg_model.predict(input_data)
    elif model_choice == 'Random Forest':
        # Predict using Random Forest model
        prediction = random_forest_model.predict(input_data)
    
    st.write(f"The predicted close price for next day is: {prediction[0]}")
