# -- coding: utf-8 --
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle

# loading the saved model
loaded_model = pickle.load(open('C:/Users/Dheeraj/OneDrive/Desktop/Fraud/Fraud_model.sav', 'rb'))

#loaded_model = pickle.load(open('D:/Work\Machine Learning/Deploying Machine Learning model/trained_model.sav', 'rb'))


input_data = (4,181,181,0)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
#print(prediction)

if (prediction[0] == 0):
  print('No Fraud')
else:
  print('Fraud')

