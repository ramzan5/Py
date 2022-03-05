import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_csv('income.csv')
# print(df)
plt.xlabel('Year')
plt.ylabel("Income")
plt.scatter(df['year'],df.income,color='red',marker='*')
# plt.show()

reg = linear_model.LinearRegression()
reg.fit(df[['year']],df.income)
print(reg.predict([[2020]]))
plt.plot(df.year,reg.predict(df[['year']]),color='blue')
plt.show()