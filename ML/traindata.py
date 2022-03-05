import pandas as pd
from sklearn.linear_model import LinearRegression
# used sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
df = pd.read_csv('carprices1.csv')
newdf = df[['Mileage','Sell Price($)','Age(yrs)']]
X = newdf[['Mileage','Age(yrs)']]
y = newdf['Sell Price($)']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
# print(len(X_train),len(X_test))
# Traing the data 

model = LinearRegression()
model.fit(X_train,y_train)
print(model.predict(X_test))
print(y_test)
print(model.score(X_test,y_test))