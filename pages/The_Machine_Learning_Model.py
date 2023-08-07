import matplotlib.pyplot as plt
import streamlit as st
from sklearn import metrics
import seaborn as sns
from SurvivalPredictor import df, df_original, y_test, y_pred

st.title("The Machine Learning Model")
st.write("""
#### Following data cleaning, this model was created using simple Logistic Regression.
""")

st.write("---")
st.write("""
The data was already split into train and test data.
Here is a glimpse of the raw data:
""")

st.write(df_original.head())

st.write("This is a correlation heatmap for the training data:")
fig, ax = plt.subplots()
sns.heatmap(df.corr(), ax=ax)
st.write(fig)
st.write("""The data was cleaned by converting continuous data to categorical, eliminating extraneous features, 
            and changing dummy values to 0s and actual values to 1.""")

st.write(df.head())
         
st.write("Utilizing MinMaxScaler, the age column was scaled and transformed into categorical data. "
         "The data was split into X and y and the model was trained.")

st.write("---")
cnf_matrix = metrics.confusion_matrix(y_test, y_pred)


st.write("##### Confusion Matrix:")
st.write(cnf_matrix)

st.write("""
         From the above Confusion Matrix we can see that

         True Positive: 52286
         False Positive: 701
         True Negative: 2736
         False Negative: 938
         """)


st.write("---")
st.write("""
The accuracy of this model is 93.9341%.
""")
