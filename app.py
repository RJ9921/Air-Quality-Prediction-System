import streamlit as st
import joblib
import pandas as pd 
from streamlit_option_menu import option_menu
from PIL import Image
import seaborn as sns
import base64
import pickle
import numpy as np


with st.sidebar:
    selected=option_menu(
    menu_title="Main Menu",
        options=['Home','Prediction'],
        icons=['house','book'],
        styles={
            "container":{"background-color":"#f67704"},
            "nav-link":{
                "font-size":"21px",
                "--hover-color":"#facf7d",
                "color":"317202A"
            },
            "nav-link-selected":{
                "background-color":"#fedc57"
            },
            "icon":{
                "font-size":"20px"
            },
        },
    )

if selected == 'Home':
    st.markdown("""
    <style>
    .big-font1{
    font-size:50px !important;
    color:#900C3F;
    text-align:center;
    font-weight:bold;
    
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<p class="big-font1"> WELCOME TO THE AIR QUALITY PREDICTION SYSTEM </p>',unsafe_allow_html=True)
    file_=open("air2.png","rb")
    contents=file_.read()
    data_url=base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" width="750" length="500" image-align="center"  alt="air2">',
        unsafe_allow_html=True, )

    

if selected=='Prediction':
    file_=open("air2.gif","rb")
    contents=file_.read()
    data_url=base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" width="700" image-align="center"  alt="air2 gif">',
        unsafe_allow_html=True, )

    st.markdown("""
    <style>
        .big-font1{
            font-size:50px !important;
            color:red;
            text-align:center;
            font-weight:bold;
    </style>
    """,unsafe_allow_html=True)
    loaded_model=pickle.load(open('air_quality.sav','rb'))

    def quality_prediction(input_data):
    

        # changing the input_data to numpy array
        input_data_as_numpy_array = np.asarray(input_data)

        # reshape the array as we are predicting for one instance
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

        prediction = loaded_model.predict(input_data_reshaped)
        print(prediction)

        if (prediction[0] == 0):
            return 'Quality of Air is Poor'
        else:
            return 'Quality of Air is Good'
    def main(): 


        st.markdown("<h1 style='text-align: center; color: #C70039 ;'>AIR QUALITY PREDICTION SYSTEM</h1>", unsafe_allow_html=True)
        #getting the input data from the user
        co1,col2,col3=st.columns(3)


        with co1:
            PM2_5=st.number_input('Enter the Value of PM 2.5',format='%f')
            PM10=st.number_input('Enter the Value of PM10',format='%f')
            NO=st.number_input('Enter the Value of NO',format='%f')

        with col2:
            NO2=st.number_input('Enter the Value of No2',format='%f')
            Nox=st.number_input('Enter the Value of Nox',format='%f')
            CO=st.number_input('Enter the Value of CO',format='%f')


        with col3:
            SO2=st.number_input('Enter the Value of SO2',format='%f')
            Benzene=st.number_input('Enter the Value of Benzene',format='%f')
            Toluene=st.number_input('Enter the Value of Toluene',format='%f')
            AQI=st.number_input('Enter the Value of AQI',format='%f')

        #code for the prediction 
        diagnosis=''
        #creating a button for prediction 
        if st.button('Air Quality Prediction Result'):
            diagnosis = quality_prediction([PM2_5,PM10,NO,NO2,Nox,CO,SO2,Benzene,Toluene,AQI])
            st.success(diagnosis)
        

    
    if __name__ =='__main__':
        main()










