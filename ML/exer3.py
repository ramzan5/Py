# Exercise 3
# At the same level as this notebook on github, there is an Exercise folder that contains carprices.csv. This file has car sell prices for 3 different models. First plot data points on a scatter plot chart to see if linear regression model can be applied. If yes, then build a model that can answer following questions,

# 1) Predict price of a mercedez benz that is 4 yr old with mileage 45000

# 2) Predict price of a BMW X5 that is 7 yr old with mileage 86000

# 3) Tell me the score (accuracy) of your model. (Hint: use LinearRegression().score())
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.core.reshape.merge import merge
from sklearn import linear_model
from sklearn.linear_model import LinearRegression

df = pd.read_csv('carprices1.csv')
# plt.xlabel(['Mileage','age'])
# plt.ylabel('Price')
# x = df['Mileage']

# y = df['Sell Price($)']

# plt.scatter(y,x,color='red',marker='+')
# plt.show()

model = LinearRegression()

dum = pd.get_dummies(df['Car Model'])
merged = pd.concat([df,dum],axis='columns')
# print(merged)
final = merged.drop(['Car Model','Mercedez Benz C class'],axis='columns')
# print(final)
X = final.drop('Sell Price($)',axis='columns')
print(X)
y = df['Sell Price($)']
# print(y)
model.fit(X,y)
print(model.predict([[45000,4,0,0]]))
print(model.predict([[86000,7,0,1]]))
print(model.score(X,y))