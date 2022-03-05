# Task related to dummy variables using panda and sklearn

# First by using pandas

from os import X_OK
import  pandas as pd
import numpy as np
from pandas.core.algorithms import mode
from pandas.core.arrays import categorical
from sklearn.linear_model import LinearRegression

df = pd.read_csv('homeprice1.csv')

# for getting dummies values

dvl =pd.get_dummies(df.town)
# print(dvl)

# merging the values of dummy and df

merged = pd.concat([df,dvl],axis='columns')
# print(merged)
# droping the value

final = merged.drop(['town','west windsor'],axis='columns')
# creating linear regression model

model = LinearRegression()
# droping the price 
X = final.drop('price',axis='columns')
y = final.price

model.fit(X,y)
# Printing thr coeficient values
# print(model.coef_,model.intercept_)
# predicting the value of wind wistor
# print(model.predict([[2800,0,0]]))
# Checking the score value

# print(model.score(X,y))


# ----------------Using Another method hot coding

from sklearn.preprocessing import LabelEncoder
# label encoder
le = LabelEncoder()
dfle = df
# creating label
dfle.town = le.fit_transform(dfle.town)
# print(dfle.town)
# print(dfle)

X1 = dfle[['town','area']].values
y1 = dfle.price
# print(X1)
# print(y1)

# creaating dummy variables

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
ct = ColumnTransformer([('town', OneHotEncoder(), [0])], remainder = 'passthrough')

X1 = ct.fit_transform(X1)
X1 = X1[:,1:]
print(X1)
model.fit(X,y)
x = model.predict([[0,1,3400]])
print(x)
