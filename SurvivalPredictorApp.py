import joblib
import pandas as pd
import streamlit as st
import numpy as np

model = joblib.load("DeathPredictorLOGREG.joblib")

st.set_page_config(page_title="COVID-19 Patient Survival Predictor", page_icon=":bar_chart:")

with st.container():
    st.title('COVID-19 Patient Survival Predictor')
    st.write("""
    #### Enter the details of the patient below.
    Enter **1** for **Yes** and **0** for **No**
    """)

st.write('---')
intubed = st.selectbox("Was the patient intubated?", [1, 0])
pneumonia = st.selectbox("Did the patient have pneumonia?", [1, 0])
age = st.selectbox("Age of the patient (1 if greater than 43, else 0)", [1, 0])
pregnancy = st.selectbox("Was the patient pregnant?", [1, 0])
diabetes = st.selectbox("Was the patient diabetic?", [1, 0])
copd = st.selectbox("Did the patient suffer from Chronic obstructive pulmonary disease (COPD)?", [1, 0])
asthma = st.selectbox("Was the patient asthmatic?", [1, 0])
inmsupr = st.selectbox("Was the patient under Immunosuppression?", [1, 0])
hypertension = st.selectbox("Did the patient suffer from hypertension?", [1, 0])
other_disease = st.selectbox("Did the patient have any other diseases?", [1, 0])
cardiovascular = st.selectbox("Did the patient have any heart disorders?", [1, 0])
obesity = st.selectbox("Was the patient obese?", [1, 0])
renal_chronic = st.selectbox("Did the patient have any kidney diseases?", [1, 0])
tobacco = st.selectbox("Did the patient consume tobacco?", [1, 0])
contact_other_covid = st.selectbox("Was the patient in contact with a COVID infected person?", [1, 0])
covid_res = st.selectbox("What was the COVID test result of the patient?", [1, 0])
icu = st.selectbox("Was the patient admitted in the ICU?", [1, 0])

columns = ["intubed", "pneumonia", "age", 'pregnancy', 'diabetes', 'copd', 'asthma', 'inmsupr', 'hypertension',
           'other_disease', 'cardiovascular', 'obesity', 'renal_chronic', 'tobacco', 'contact_other_covid',
           'covid_res', 'icu']

features = [intubed, pneumonia, age, pregnancy, diabetes, copd, asthma, inmsupr, hypertension, other_disease
            , cardiovascular, obesity, renal_chronic, tobacco, contact_other_covid, covid_res, icu]


def predict():
    row = np.array(features)
    X = pd.DataFrame([row], columns=columns)
    prediction = model.predict(X)[0]

    if prediction == 1:
        st.error("The patient did not survive :thumbsdown:")
    else:
        st.success("The patient survived :thumbsup::fire:")


st.button("Predict", on_click=predict)
st.caption("Made by Aniruddh")
