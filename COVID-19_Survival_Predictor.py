import joblib
import pandas as pd
import streamlit as st
import numpy as np

model = joblib.load("SurvivalPredictorModel.joblib")

st.set_page_config(page_title="COVID-19 Patient Survival Predictor", page_icon=":syringe:")

with st.container():
    st.title('COVID-19 Patient Survival Predictor')
    st.write("""
    #### Enter the details of the patient below.
    """)

st.write('---')
intubed = st.selectbox("Was the patient intubated?", ["Yes", "No"])

pneumonia = st.selectbox("Did the patient have pneumonia?", ["Yes", "No"])

age = st.number_input( "Age of the patient:", key="age")

pregnancy = st.selectbox("Was the patient pregnant?", ["Yes", "No"])

diabetes = st.selectbox("Was the patient diabetic?", ["Yes", "No"])

copd = st.selectbox("Did the patient suffer from Chronic obstructive pulmonary disease (COPD)?", ["Yes", "No"])

asthma = st.selectbox("Was the patient asthmatic?", ["Yes", "No"])

inmsupr = st.selectbox("Was the patient under Immunosuppression?", ["Yes", "No"])

hypertension = st.selectbox("Did the patient suffer from hypertension?", ["Yes", "No"])

other_disease = st.selectbox("Did the patient have any other diseases?", ["Yes", "No"])

cardiovascular = st.selectbox("Did the patient have any heart disorders?", ["Yes", "No"])

obesity = st.selectbox("Was the patient obese?", ["Yes", "No"])

renal_chronic = st.selectbox("Did the patient have any kidney diseases?", ["Yes", "No"])

tobacco = st.selectbox("Did the patient consume tobacco?", ["Yes", "No"])

contact_other_covid = st.selectbox("Was the patient in contact with a COVID infected person?", ["Yes", "No"])

covid_res = st.selectbox("What was the COVID test result of the patient?", ["Positive", "Negative"])

icu = st.selectbox("Was the patient admitted in the ICU?", ["Yes", "No"])

def negative():
    global intubed, pneumonia, age, pregnancy, diabetes, copd, asthma, inmsupr, hypertension, other_disease, cardiovascular, obesity, renal_chronic, tobacco, contact_other_covid, covid_res, icu
    intubed = "Yes"
    pneumonia = "No"
    age = 89.00
    pregnancy = "No"
    diabetes = "No"
    copd = "No"
    asthma = "Yes"
    inmsupr = "Yes"
    hypertension = "No"
    other_disease = "Yes"
    cardiovascular = "No"
    obesity = "Yes"
    renal_chronic = "No"
    tobacco = "No"
    contact_other_covid = "No" 
    covid_res = "Positive"
    icu = "Yes"
    
    
st.write("Hint: For a negative result, click here: ")
st.button("Negative Result", on_click=negative)    


intubed = 1 if intubed == "Yes" else 0
pneumonia = 1 if pneumonia == "Yes" else 0
age = 1 if age > 43 else 0
pregnancy = 1 if pregnancy == "Yes" else 0
diabetes = 1 if diabetes == "Yes" else 0
copd = 1 if copd == "Yes" else 0
asthma = 1 if asthma == "Yes" else 0
inmsupr = 1 if inmsupr == "Yes" else 0
hypertension = 1 if hypertension == "Yes" else 0
other_disease = 1 if other_disease == "Yes" else 0
cardiovascular = 1 if cardiovascular == "Yes" else 0
obesity = 1 if obesity == "Yes" else 0
renal_chronic = 1 if renal_chronic == "Yes" else 0
tobacco = 1 if tobacco == "Yes" else 0
contact_other_covid = 1 if contact_other_covid == "Yes" else 0
covid_res = 1 if covid_res == "Positive" else 0
icu = 1 if icu == "Yes" else 0
   
    
columns = ["intubed", "pneumonia", "age", 'pregnancy', 'diabetes', 'copd', 'asthma', 'inmsupr', 'hypertension',
           'other_disease', 'cardiovascular', 'obesity', 'renal_chronic', 'tobacco', 'contact_other_covid',
           'covid_res', 'icu']

features = [intubed, pneumonia, age, pregnancy, diabetes, copd, asthma, inmsupr, hypertension, other_disease
            , cardiovascular, obesity, renal_chronic, tobacco, contact_other_covid, covid_res, icu]


def predict():
    row = np.array(features)
    X = pd.DataFrame([row], columns=columns)
    prediction = model.predict(X)[0]

    if prediction == 1.0:
        st.error("The patient did not survive :thumbsdown:🥶")
    else:
        st.success("The patient survived :thumbsup::fire:")


st.button("Predict", on_click=predict)
st.caption("Made by Aniruddh")
