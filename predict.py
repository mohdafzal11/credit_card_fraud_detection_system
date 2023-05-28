import streamlit as st
import pickle
import numpy as np
import pandas as pd


def load_model():
    model = pickle.load(open("model.pkl", "rb"))

    return model

model = load_model()

def strToIntBool(s):
    if s == 'True':
        return 1
    else: return 0

def show_predict_page():
    st.title("Credit Card Fraud Detection")
    st.subheader("""By Parth Maniar""")
    
    st.write("""### Enter Information to Predict if the Transaction is Fraud or Not!""")
    
    # Create input fields for the numerical columns
    distance_from_home = st.number_input('Distance from Home')
    distance_from_last_transaction = st.number_input('Distance from Last Transaction')
    ratio_to_median_purchase_price = st.number_input('Ratio to Median Purchase Price')
    repeat_retailer = st.radio('Repeat Retailer', ["False", "True"])
    used_chip = st.radio('Used Chip', ["False", "True"])
    used_pin_number = st.radio('Used Pin Number', ["False", "True"])
    online_order = st.radio('Online Order', ["False", "True"])


    input_dict = {
        'distance_from_home': distance_from_home,
        'distance_from_last_transaction': distance_from_last_transaction,
        'ratio_to_median_purchase_price': ratio_to_median_purchase_price,
        'repeat_retailer': strToIntBool(repeat_retailer),
        'used_chip': strToIntBool(used_chip),
        'used_pin_number': strToIntBool(used_pin_number),
        'online_order': strToIntBool(online_order)
    }

    # Convert the input dictionary to a Pandas DataFrame
    input_df = pd.DataFrame([input_dict])

    # Use the trained model to make predictions on the input data
    
    if st.button("Predict Now"):
    
        prediction = model.predict(input_df)
        print(prediction)
        # Show the predicted result
        if prediction[0]:
            st.error('The Transaction is Fraud', icon="🚨")
        else: st.success('The Transaction is Safe', icon="✅")
 
    