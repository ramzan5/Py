from matplotlib import colors
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
df = pd.read_csv('price.csv')
print(df)

plt.xlabel('Area')
plt.ylabel('Price')
plt.scatter(df.Area,df.Price,color='red',marker='+')
# plt.show()
# we know y = mx + b
# creating the Linear regression
reg = linear_model.LinearRegression()
# putting the data in regrsstion 
reg.fit(df[['Area']],df.Price)
# print(reg.predict(3300))
# print(reg.predict([[3300],[3700]]))
print(reg.predict([[3300]]))
# getting the value of m
print(reg.coef_)
# getting the value of b
# print(reg.intercept_)
# d = pd.read_csv('price1.csv')
# p = reg.predict(d)
# d['price'] = p
# d.to_csv('prediction.csv')
# plt.plot(df.Area,reg.predict(df[['Area']]),color='blue')
# plt.show()
# import pickle

# with open('model_pickle','wb') as f:
#     pickle.dump(df,f)

# with open('model_pickle','rb') as f:
#     mp = pickle.load(f)

# print(mp.predict(3700))




import joblib
joblib.dump(df,'model_joblib')

mj = joblib.load('model_joblib')
print(mj.predict(5000))