import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('HR_comma_sep.csv')
print(df)
left = df[df.left==1]
retained = df[df.left==0]
df.groupby('left').mean()
print(df.groupby('left').mean())
pd.crosstab(df.salary,df.left).plot(kind='bar').show()
