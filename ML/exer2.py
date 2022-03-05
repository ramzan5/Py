import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
from word2number import w2n

df = pd.read_csv('hiring.csv')
medianval = int(df['test_score(out of 10)'].median())
df['test_score(out of 10)'] = df['test_score(out of 10)'].fillna(medianval)
# replacing NaN with zero in experience col
df.experience = df.experience.fillna("zero")
# changing text into numbers
df.experience = df.experience.apply(w2n.word_to_num)
reg = linear_model.LinearRegression()
reg.fit(df[['experience','test_score(out of 10)','interview_score(out of 10)']],df['salary($)'])
print(reg.coef_,reg.intercept_)
print(reg.predict([[2,9,6]]))
print(reg.predict([[12,10,10]]))

