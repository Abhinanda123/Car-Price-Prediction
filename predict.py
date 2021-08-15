# Importing the necessary Python modules.
import numpy as np
import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error, mean_squared_log_error

# Define the 'prediction()' function.
@st.cache()
def prediction(car_df, car_width, engine_size, horse_power, drive_wheel_fwd, car_comp_buick):
    X = car_df.iloc[:, :-1] 
    y = car_df['price']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42) 

    lin_reg = LinearRegression()
    lin_reg.fit(X_train, y_train)
    score = lin_reg.score(X_train, y_train)

    price = lin_reg.predict([[car_width, engine_size, horse_power, drive_wheel_fwd, car_comp_buick]])
    price = price[0]

    y_test_pred = lin_reg.predict(X_test)
    test_r2_score = r2_score(y_test, y_test_pred)
    test_mae = mean_absolute_error(y_test, y_test_pred)
    test_msle = mean_squared_log_error(y_test, y_test_pred)
    test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))

    return price, score, test_r2_score, test_mae, test_msle, test_rmse

def app(df):
  st.markdown("<p style=color: blue; font-size:25px> This app uses <b> Linear regression </b> to predict the price of a car based on your inputs </p>" , unsafe_allow_html = True )
  st.header("Select the values")
  car_wdt= st.slider("Car width", float(df["carwidth"].min()), float(df["carwidth"].max()))
  car_eng_sz= st.slider("Engine size", float(df["enginesize"].min()), float(df["enginesize"].max()))
  hp= st.slider("Horsepower", float(df["horsepower"].min()), float(df["horsepower"].max()))
  fwd_dr= st.radio("Is it a Forward-drive car? [0---> no; 1---> yes]", (0,1))
  car_buick= st.radio("Is the car manufactured by buick [0---> no; 1---> yes]", (0,1))
  if st.button("Predict"):
    st.subheader("Prediction Results")
    price, score, r2_score, mae, msle, rmse= prediction(df, car_wdt,car_eng_sz, hp, fwd_dr, car_buick)
    st.success(f"The predicted car price is: {price}")
    st.info(f"Accuracy of model: {score}\nR2 score: {r2_score}\nMean Squared Log Error value: {msle}\nMean Absolute Error Value: {mae}\nRoot Mean Squared Error: {rmse}")
