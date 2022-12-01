import streamlit as st
import pandas as pd
from sklearn import metrics
from SurvivalPredictor import y_test, y_pred

st.title("The Machine Learning Model")
st.write("""
#### Following data cleaning, this model was created using simple Logistic Regression.
""")

st.write("---")
st.write("""
The data was already split into train and test data.
Here is a glimpse of the training data:
""")

train = pd.read_csv("train.csv")
st.dataframe(train.head())
st.write("""The data was cleaned by converting continuous data to categorical, eliminating extraneous features, 
            and changing dummy values to 0s and actual values to 1.""")

         
st.write("Utilizing MinMaxScaler, the age column was scaled and transformed into categorical data. "
         "The data was split into X and y and the model was trained.")

st.write("---")
cnf_matrix = metrics.confusion_matrix(y_test, y_pred)

st.write("##### Confusion Matrix:")
st.dataframe(cnf_matrix)

st.write("---")
st.write("""
The accuracy of this model is 97.23675%.
""")



