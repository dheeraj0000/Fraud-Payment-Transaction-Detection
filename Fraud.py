# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 11:03:51 2024

@author: Dheeraj
"""



import numpy as np
import pickle
import streamlit as st


# loading the saved model

loaded_model = pickle.load(open('Fraud_model.sav', 'rb'))


# creating a function for Prediction

def diabetes_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    prediction = loaded_model.predict(input_data_reshaped)
    #return prediction

    print(prediction)
    
    if (prediction[0] == 0):
      return 'No Fraud'
    else:
      return 'Fraud'
    
    
  
    
  
def main():
    
    
    # giving a title
    st.title('Fraud  Prediction Web App')
    
    
    # getting the input data from the user
    
    
    type = st.text_input('type')
    amount = st.text_input('amount')
    oldbalanceOrg = st.text_input('oldbalanceOrg')
    newbalanceOrig = st.text_input('newbalanceOrig')
    
    
    # code for Prediction
    diagnosis = ''
    
    
    
    # creating a button for Prediction
    
    if st.button('Fraud Test Result'):
        diagnosis = diabetes_prediction([type, amount, oldbalanceOrg, newbalanceOrig])
        

        
    st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()
