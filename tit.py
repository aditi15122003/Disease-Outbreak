import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
st.set_page_config(page_title='Prediction of Disease Outbreak', layout='wide', page_icon='doctor')
diabetes_model = pickle.load(open(r"C:\Users\Lenovo\Disease\diabetes_model.sav",'rb'))
heart_model = pickle.load(open(r"C:\Users\Lenovo\Disease\heart_model.sav",'rb'))
with st.sidebar:
    selected= option_menu('Prediction of disease Outbreak' , ['Diabetes Disease Prediction' , 'Heart Disease Prediction'],menu_icon='hospital-fill',icons=['activity' ,'heart' , 'person'],default_index=0)
    
    
if selected == 'Diabetes Disease Prediction':
    st.title("Diabetes Prediction using ML")   
    col1,col2,col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        Bloodpressure = st.text_input('Blood Pressure Value') 
    with col1:
        Skinthickness = st.text_input('Skin Thickness Value')   
    with col2:
        Insulin = st.text_input('Insulin Value')
    with col3:
        BMI = st.text_input('BMI Value')   
    with col1:
        DiabetesPedigreefunction = st.text_input('Diabetes Pedigree Function')       
    with col2:
        Age = st.text_input('Age of the Person')
        
diab_diagnosis =''
if st.button('Diabetes Test Result'):
    user_input=[Pregnancies,Glucose,Bloodpressure,Skinthickness, Insulin,BMI, DiabetesPedigreefunction, Age]
    user_input= [float(x) for x in user_input]
    diab_prediction = diabetes_model.predict([user_input])
    if diab_prediction[0]==1:
        diab_diagnosis='The person is Diabetic'
    else:
        diab_diagnosis='The person is not Diabetic'
st.success(diab_diagnosis)        
if selected == 'Heart Disease Prediction':
    st.title("Heart Disease Prediction using ML")   
    col1,col2,col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        Bloodpressure = st.text_input('Blood Pressure Value') 
    with col1:
        Skinthickness = st.text_input('Skin Thickness Value')   
    with col2:
        Insulin = st.text_input('Insulin Value')
    with col3:
        BMI = st.text_input('BMI Value')   
    with col1:
        DiabetesPedigreefunction = st.text_input('Diabetes Pedigree Function')       
    with col2:
        Age = st.text_input('Age of the Person')
        
diab_diagnosis =''
if st.button('Heart Test Result'):
    user_input=[Pregnancies,Glucose,Bloodpressure,Skinthickness, Insulin,BMI, DiabetesPedigreefunction, Age]
    user_input= [float(x) for x in user_input]
    diab_prediction = diabetes_model.predict([user_input])
    if diab_prediction[0]==1:
        diab_diagnosis='The person have Heart Disease'
    else:
        diab_diagnosis='The person dont have Heart Disease'
st.success(diab_diagnosis)        