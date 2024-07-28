import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load the saved model
model = joblib.load('best_model.pkl')

# Function to preprocess input data
def preprocess_input(transaction_amount, transaction_time):
    # Add your preprocessing steps here
    input_data = {
        'transaction_amount': transaction_amount,
        'transaction_time': transaction_time,
        # Add other features
    }
    input_df = pd.DataFrame([input_data])
    return input_df

# Define the Streamlit app
def main():
    st.title("Credit Card Fraud Detection")

    st.write("Enter the transaction details to predict if it's fraudulent or not.")

    # Input fields for user to enter transaction details
    transaction_amount = st.number_input("Transaction Amount", min_value=0.0)
    transaction_time = st.number_input("Transaction Time", min_value=0.0)
    # Add other input fields based on your feature set

    # Button to make prediction
    if st.button("Predict"):
        input_df = preprocess_input(transaction_amount, transaction_time)
        prediction = model.predict(input_df)
        if prediction == 1:
            st.error("This transaction is predicted to be fraudulent!")
        else:
            st.success("This transaction is predicted to be legitimate.")

if __name__ == "__main__":
    main()
