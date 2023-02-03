# -*- coding: utf-8 -*-

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

finalmodel = pickle.load(open('finalmodel.sav', 'rb'))


# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Air Quality prediction',
                          
                          ['Air Quality'],
                          icons=['activity'],
                          default_index=0)
    
    
if (selected == 'Air Quality'):
    
    # page title
    st.title('Air Quality Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('age')
        
    with col2:
        Glucose = st.text_input('nsdc dcc')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Fuefdenction value')
    
    with col2:
        Age = st.text_input('Age of the edPerson')
    with col3:
        a = st.text_input('Blood Pressuredd value')
    
    with col1:
        b = st.text_input('Skin Thicknesdedes value')
    
    with col2:
        c = st.text_input('Insulin Ldedevel')
    
    with col3:
        d = st.text_input('BMI ded')
    
    with col1:
        e = st.text_input('Diabetes Pedigree Funcewdewtion value')
    
    with col2:
        f= st.text_input('Age of the Peon')
    with col3:
        g= st.text_input('Blood Pressuvalue')
    
    with col1:
        h = st.text_input('Skin Thicdess value')
    
    with col2:
        i= st.text_input('Insuliwd Level')
        
    with col3:
        j= st.text_input('jddjl')
    
    
    
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = finalmodel.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age,a,b,c,d,e,f,g,h,i,j]])
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'Good'
        else:
          diab_diagnosis = 'bad'

        
    st.success(diab_diagnosis)















