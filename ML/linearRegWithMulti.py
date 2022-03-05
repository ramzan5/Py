import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

df = pd.read_csv('homePrices.csv')
a = int(df.bedrooms.median())
df.bedrooms = df.bedrooms.fillna(a)

reg = linear_model.LinearRegression()
# independent variable will be on x axis
reg.fit(df[['area','bedrooms','age']],df.price)
print(reg.coef_,reg.intercept_)
print(reg.predict([[3000,3,40]]))