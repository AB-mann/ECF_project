# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 01:26:10 2024

@author: ABHIMAN
"""

import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

#from PIL import Image

#app=Flask(_name_)
#Swagger(app)

pickle_in = open("prediction.pkl","wb")
predicted =pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(avg_energy,	weather_cluster,holiday_index):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: avg_energy
        in: query
        type: float64
        required: true
      - name:weather_cluster
        in: query
        type:  float64
        required: true
      - name:holiday_index
        in:query
        type: float64
        required: true
     
    responses:
        200:
            description: The output values
        
    """
   
    prediction = predicted.predict([[avg_energy,weather_cluster,holiday_index]])
    print(prediction)
    return prediction



def main():
    st.title("energy consumption prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit energy consumption prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    avg_energy = st.text_input("avg_energy","Type Here")
    weather_cluster = st.text_input("weather_cluster","Type Here")
    holiday_index = st.text_input("holiday_index","Type Here")
   
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(avg_energy,weather_cluster,holiday_index)
    st.success('The output is {}'.format(result))


if __name__=='__main__':
    main()

