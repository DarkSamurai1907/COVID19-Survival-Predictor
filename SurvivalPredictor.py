import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler
import joblib

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

train = train.drop(train.columns[[0, 1, 2, 3, 4, 5]], axis=1)
test = test.drop(test.columns[[0, 1, 2, 3, 4, 5]], axis=1)

train = train.replace(['9999-99-99'], '0')
train = train.replace(['9999-99-99$'], '0')
test = test.replace(['9999-99-99'], '0')
test = test.replace(['9999-99-99$'], '0')

date_died = train['date_died'].to_list()
date_died = list(set(date_died))
date_died.pop(date_died.index('0'))
train['date_died'] = train['date_died'].replace(date_died, '1')

date_died = test['date_died'].to_list()
date_died = list(set(date_died))
date_died.pop(date_died.index('0'))
test['date_died'] = test['date_died'].replace(date_died, '1')

train = train.replace([97, 98, 99], 0)
test = test.replace([97, 98, 99], 0)

ages1 = []

for i in train['age']:
    i = i[:2]
    i = int(i)
    ages1.append(i)

train['age'] = ages1

ages2 = []

for i in test['age']:
    i = i[:2]
    i = int(i)
    ages2.append(i)

test['age'] = ages2

scaling1 = MinMaxScaler()
train = scaling1.fit_transform(train.to_numpy()).round()
scaling2 = MinMaxScaler()
test = scaling2.fit_transform(test.to_numpy()).round()

train = pd.DataFrame(train,
                     columns=['date_died', 'intubed', 'pneumonia', 'age', 'pregnancy', 'diabetes', 'copd', 'asthma',
                              'inmsupr', 'hypertension', 'other_disease', 'cardiovascular', 'obesity', 'renal_chronic',
                              'tobacco', 'contact_other_covid', 'covid_res', 'icu'])
test = pd.DataFrame(test,
                    columns=['date_died', 'intubed', 'pneumonia', 'age', 'pregnancy', 'diabetes', 'copd', 'asthma',
                             'inmsupr', 'hypertension', 'other_disease', 'cardiovascular', 'obesity', 'renal_chronic',
                             'tobacco', 'contact_other_covid', 'covid_res', 'icu'])

# Split dataset in features and target variable
feature_cols = ['intubed', 'pneumonia', 'age', 'pregnancy', 'diabetes', 'copd', 'asthma', 'inmsupr', 'hypertension',
                'other_disease', 'cardiovascular', 'obesity', 'renal_chronic', 'tobacco', 'contact_other_covid',
                'covid_res', 'icu']
X = train.drop(['date_died'], axis=1)  # Features
y = train.drop(feature_cols, axis=1)  # Target variable
y = np.ravel(y)  # Convert the column vector into a contiguous flattened array

X_test = test.drop(['date_died'], axis=1)
y_test = test.drop(feature_cols, axis=1)

# instantiate the model (using the default parameters)
logreg = LogisticRegression()
# fit the model with data
logreg.fit(X, y)
y_pred = logreg.predict(X_test)

joblib.dump(logreg, "SurvivalPredictorModel.joblib")
