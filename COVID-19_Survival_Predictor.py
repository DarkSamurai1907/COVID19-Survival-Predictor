import joblib
import pandas as pd
import streamlit as st
import numpy as np

model = joblib.load("SurvivalPredictorLOGREG.joblib")

st.set_page_config(page_title="COVID-19 Patient Survival Predictor", page_icon=":syringe:")

with st.container():
    st.title('COVID-19 Patient Survival Predictor')
    st.write("""
    #### Enter the details of the patient below.
    """)

st.write('---')
intubed = st.selectbox("Was the patient intubated?", ["Yes", "No"])
intubed = 1 if intubed == "Yes" else 0

pneumonia = st.selectbox("Did the patient have pneumonia?", ["Yes", "No"])
pneumonia = 1 if pneumonia == "Yes" else 0

age = st.number_input( "Age of the patient:", key="age")
age = 1 if age > 43 else 0

pregnancy = st.selectbox("Was the patient pregnant?", ["Yes", "No"])
pregnancy = 1 if pregnancy == "Yes" else 0

diabetes = st.selectbox("Was the patient diabetic?", ["Yes", "No"])
diabetes = 1 if diabetes == "Yes" else 0

copd = st.selectbox("Did the patient suffer from Chronic obstructive pulmonary disease (COPD)?", ["Yes", "No"])
copd = 1 if copd == "Yes" else 0

asthma = st.selectbox("Was the patient asthmatic?", ["Yes", "No"])
asthma = 1 if asthma == "Yes" else 0

inmsupr = st.selectbox("Was the patient under Immunosuppression?", ["Yes", "No"])
inmsupr = 1 if inmsupr == "Yes" else 0

hypertension = st.selectbox("Did the patient suffer from hypertension?", ["Yes", "No"])
hypertension = 1 if hypertension == "Yes" else 0

other_disease = st.selectbox("Did the patient have any other diseases?", ["Yes", "No"])
other_disease = 1 if other_disease == "Yes" else 0

cardiovascular = st.selectbox("Did the patient have any heart disorders?", ["Yes", "No"])
cardiovascular = 1 if cardiovascular == "Yes" else 0

obesity = st.selectbox("Was the patient obese?", ["Yes", "No"])
obesity = 1 if obesity == "Yes" else 0

renal_chronic = st.selectbox("Did the patient have any kidney diseases?", ["Yes", "No"])
renal_chronic = 1 if renal_chronic == "Yes" else 0

tobacco = st.selectbox("Did the patient consume tobacco?", ["Yes", "No"])
tobacco = 1 if tobacco == "Yes" else 0

contact_other_covid = st.selectbox("Was the patient in contact with a COVID infected person?", ["Yes", "No"])
contact_other_covid = 1 if contact_other_covid == "Yes" else 0

covid_res = st.selectbox("What was the COVID test result of the patient?", ["Positive", "Negative"])
covid_res = 1 if covid_res == "Positive" else 0

icu = st.selectbox("Was the patient admitted in the ICU?", ["Yes", "No"])
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
    st.header(prediction)

    if prediction == 1:
        st.error("The patient did not survive :thumbsdown:🥶")
    else:
        st.success("The patient survived :thumbsup::fire:")


st.button("Predict", on_click=predict)
st.caption("Made by Aniruddh")
import joblib
import pandas as pd
import streamlit as st
import numpy as np

model = joblib.load("SurvivalPredictorLOGREG.joblib")

st.set_page_config(page_title="COVID-19 Patient Survival Predictor", page_icon=":syringe:")

with st.container():
    st.title('COVID-19 Patient Survival Predictor')
    st.write("""
    #### Enter the details of the patient below.
    """)

st.write('---')
intubed = st.selectbox("Was the patient intubated?", ["Yes", "No"])
intubed = 1 if intubed == "Yes" else 0

pneumonia = st.selectbox("Did the patient have pneumonia?", ["Yes", "No"])
pneumonia = 1 if pneumonia == "Yes" else 0

age = st.number_input( "Age of the patient:", key="age")
age = 1 if age > 43 else 0

pregnancy = st.selectbox("Was the patient pregnant?", ["Yes", "No"])
pregnancy = 1 if pregnancy == "Yes" else 0

diabetes = st.selectbox("Was the patient diabetic?", ["Yes", "No"])
diabetes = 1 if diabetes == "Yes" else 0

copd = st.selectbox("Did the patient suffer from Chronic obstructive pulmonary disease (COPD)?", ["Yes", "No"])
copd = 1 if copd == "Yes" else 0

asthma = st.selectbox("Was the patient asthmatic?", ["Yes", "No"])
asthma = 1 if asthma == "Yes" else 0

inmsupr = st.selectbox("Was the patient under Immunosuppression?", ["Yes", "No"])
inmsupr = 1 if inmsupr == "Yes" else 0

hypertension = st.selectbox("Did the patient suffer from hypertension?", ["Yes", "No"])
hypertension = 1 if hypertension == "Yes" else 0

other_disease = st.selectbox("Did the patient have any other diseases?", ["Yes", "No"])
other_disease = 1 if other_disease == "Yes" else 0

cardiovascular = st.selectbox("Did the patient have any heart disorders?", ["Yes", "No"])
cardiovascular = 1 if cardiovascular == "Yes" else 0

obesity = st.selectbox("Was the patient obese?", ["Yes", "No"])
obesity = 1 if obesity == "Yes" else 0

renal_chronic = st.selectbox("Did the patient have any kidney diseases?", ["Yes", "No"])
renal_chronic = 1 if renal_chronic == "Yes" else 0

tobacco = st.selectbox("Did the patient consume tobacco?", ["Yes", "No"])
tobacco = 1 if tobacco == "Yes" else 0

contact_other_covid = st.selectbox("Was the patient in contact with a COVID infected person?", ["Yes", "No"])
contact_other_covid = 1 if contact_other_covid == "Yes" else 0

covid_res = st.selectbox("What was the COVID test result of the patient?", ["Positive", "Negative"])
covid_res = 1 if covid_res == "Positive" else 0

icu = st.selectbox("Was the patient admitted in the ICU?", ["Yes", "No"])
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
    st.header(prediction)

    if prediction == 1:
        st.error("The patient did not survive :thumbsdown:🥶")
    else:
        st.success("The patient survived :thumbsup::fire:")


st.button("Predict", on_click=predict)
st.caption("Made by Aniruddh")
