import pandas as pd
from matplotlib import pyplot as plt



df = pd.read_csv('insurance_data.csv')
plt.scatter(df['age'],df['bought_insurance'],marker='*',color='red')

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(df[['age']],df['bought_insurance'],train_size=0.8)

print(X_train,y_train)
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

model.fit(X_train, y_train)

y_predicted = model.predict(X_test)
model.predict_proba(X_test)
print(model.predict_proba(X_test))
