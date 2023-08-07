# Importing Libraries 
import random
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle


# Reading train and test data
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

df = pd.concat([train,test])

df_original = df

df = df.replace(['9999-99-99'], '0')
df = df.replace(['9999-99-99$'], '0')

date_died = df['date_died'].to_list()
date_died = list(set(date_died))
date_died.pop(date_died.index('0'))
df['date_died'] = df['date_died'].replace(date_died, '1')

df = df.drop(df.columns[[0,1,2,3,4,5]], axis=1)

cols = ['intubed','pneumonia','pregnancy','diabetes','copd','asthma','inmsupr','hypertension','other_disease','cardiovascular','obesity','renal_chronic','tobacco','contact_other_covid','icu']

for col in cols:
    df[col] = df[col].replace([97,98,99], 2)

for col in cols:
    df[col] = df[col].replace(2, 0)

df['covid_res'] = df['covid_res'].replace([1,2,3], [1,0,0])

ages=[]
for i in df['age']:
    i = i[:2]
    i=int(i)
    ages.append(i)
df['age'] = ages

scaler = MinMaxScaler()
df['age'] = scaler.fit_transform(df[['age']]).round()

df['date_died'] = df['date_died'].astype(int)

#split dataset in features and target variable
feature_cols = ['intubed','pneumonia','age','pregnancy','diabetes','copd','asthma','inmsupr','hypertension','other_disease','cardiovascular','obesity','renal_chronic','tobacco','contact_other_covid','covid_res','icu']
X= df.drop(['date_died'],axis=1) # Features
y = df.drop(feature_cols,axis=1) # Target variable
y = np.ravel(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 42)

model = LogisticRegression(max_iter = 999999)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

with open("FinalModel.pkl", "wb") as f:
    pickle.dump(model, f)
