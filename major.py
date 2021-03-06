# -*- coding: utf-8 -*-
"""Major.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hmmXrpUy5AgmlI-dIRvFROJFefJnUUij

***Import Dependencies***
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor

from sklearn import metrics
from matplotlib import pyplot as plt
from matplotlib import *

#Font for graph labels, this is used for all graphs in this notebook
label_font = {"fontsize": 12, 
              "color" : "darkred",
             'weight': 'normal'}
#Font for graph title, this is used for all graphs in this notebook
title_font = {"fontsize": 15, 
              "color" : "darkred",
             'weight': 'normal'}

"""***Data Collection and Processing***"""

#loading the csv data to a panda DataFrame
agri_data=pd.read_csv('//Users/shreshikanayani/Desktop/sem_8/Agriculture2018.csv')

#print First 5 rows in the dataframe
agri_data.head()

#last five rows of the dataframe
agri_data.tail()

#number of rows and columns
agri_data.shape

#getting some basic information about data
agri_data.info()

#checking Number of missing values
agri_data.isnull().sum()

#getting the statistical measures of the data
agri_data.describe()

"""Find Correlation
1. POSITIVE correlation
2. NEGATIVE correlation
"""

correlation=agri_data.corr()

#constructing a heatmap to understand the correlation
plt.figure(figsize=(8,8))
sns.heatmap(correlation, cbar=True, square=True, fmt='.1f',annot=True,annot_kws={'size':8},cmap='Blues')

#Normalize labels
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
agri_data['commodity']=le.fit_transform(agri_data['commodity'])
agri_data['variety']=le.fit_transform(agri_data['variety'])
agri_data.head()

"""***Storing vector and values seperately***"""

from sklearn.metrics import r2_score
x=agri_data.iloc[:,[3,4,6,7]]
y=agri_data['modal_price']
print(x)
print(y)

"""***Splitting Training and Test Data***"""

X_train, X_test, y_train, y_test = train_test_split(x, y,train_size=0.80,  test_size = 0.20, random_state = 1)

"""**Model Training**

1. linear regression
"""

lr=LinearRegression()
lr.fit(X_train,y_train)
y_predict=lr.predict(X_test)
acc1=r2_score(y_predict,y_test)
print("Accuracy in LinearRegression is",acc1)

"""2. Random Forest"""

rfr=RandomForestRegressor()
rfr.fit(X_train,y_train)
y_predict1=rfr.predict(X_test)
acc2=rfr.score(X_test,y_test)
print("Accuracy of RandomForest is",acc2)

"""3. Decision Tree"""
from sklearn import tree
dtr=tree.DecisionTreeRegressor()
dtr.fit(X_train,y_train)
y_predict2=dtr.predict(X_test)
acc3=r2_score(y_predict2,y_test)
print("Accuracy of Decision Tree is",acc3)

"""***Model Evaluation***
1. Linear Regression
"""

test_vector=np.reshape(np.asarray([1,5,3100.0,3000.0]),(1,4))
p=int(lr.predict(test_vector)[0])
print(p)

"""2. Random Forest"""

test_vector=np.reshape(np.asarray([1,5,3100.0,3000.0]),(1,4))
q=int(rfr.predict(test_vector)[0])
print(q)

"""3. Decision Tree"""

test_vector=np.reshape(np.asarray([1,5,3100.0,3000.0]),(1,4))
r=int(dtr.predict(test_vector)[0])
print(r)

"""***Visualize the actual and predicted prices***

1. Linear Regression
"""

plt.scatter(y_test,y_predict)
plt.xlabel('Actual price')
plt.ylabel('Predicted price')
plt.title('Actual Price vs Predicted price using Linear Regression')
plt.show()

"""2.Random Forest"""

plt.scatter(y_test,y_predict1)
plt.xlabel('Actual price')
plt.ylabel('Predicted price')
plt.title('Actual Price vs Predicted price using Random Forest')
plt.show()

"""3. Decision Tree"""

plt.scatter(y_test,y_predict2)
plt.xlabel('Actual price')
plt.ylabel('Predicted price')
plt.title('Actual Price vs Predicted price using Decision Tree')
plt.show()

#saving model to disc
pickle.dump(lr,open('lrmodel.pkl','wb'))
model=pickle.load(open('lrmodel.pkl','rb'))
pickle.dump(rfr,open('rfrmodel.pkl','wb'))
model1=pickle.load(open('rfrmodel.pkl','rb'))
pickle.dump(dtr,open('dtrmodel.pkl','wb'))
model2=pickle.load(open('dtrmodel.pkl','rb'))