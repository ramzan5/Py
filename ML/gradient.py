import numpy as np
import pandas as pd
import math
from sklearn.linear_model import LinearRegression
def gradient_descent(x,y):
    m_curr=b_curr=0
    iteration = 100000
    n = len(x)
    learining_rate = 0.0001
    cost_previous = 0

    for i in range(iteration):
        y_predicted = m_curr * x + b_curr
        cost = (1/n) * sum([val**2 for val in (y-y_predicted)])
        md = -(2/n) * sum(x*(y-y_predicted))
        bd = -(2/n) * sum(y-y_predicted)
        m_curr = m_curr - learining_rate*md
        b_curr = b_curr - learining_rate*bd
        if math.isclose(cost, cost_previous, rel_tol=1e-20):
            break
        cost_previous = cost
        print('m {}, b {}, cost {}, iteration {}'.format(m_curr,b_curr,cost,i))
    return m_curr, b_curr
# x = np.array([1,2,3,4,5])
# y = np.array([5,7,9,11,13])
# gradient_descent(x,y)

df = pd.read_csv('test_score.csv')
x = np.array(df.math)
y = np.array(df.cs)
m, b = gradient_descent(x,y)
print("Using gradient descent function: Coef {} Intercept {}".format(m, b))
import pickle
