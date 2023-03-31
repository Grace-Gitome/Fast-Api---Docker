#Machine Learning model based on pertroleum dataset from kaggle

import pandas as pd
import numpy as np
import pickle


#sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
import joblib #for creating pipelines

#Reading data
df = pd.read_csv('Data/petrol_consumption.csv')

#Defining features and target
X = df.drop('Petrol_Consumption', axis = 1)
y = df['Petrol_Consumption']

#Splitting and preparing data
X_train, X_test, y_train, y_test = train_test_split (X, y, test_size = 0.3)
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


#Model Creation & Prediction
regressor = RandomForestRegressor(n_estimators=30)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test) 



#Serialize the model using joblib
#Sample Prediction
print(int(regressor.predict([[9.0, 3571, 1976, .525]])))


#Pickle model for Flask App
joblib.dump(regressor, open('model.pkl', 'wb'))
