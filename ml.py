import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures

plt.rcParams['font.sans-serif'] = ['SimHei']
data = pd.read_excel('predict_data/data.xlsx')
X = data[['人口','城镇人口','工业GDP']]
y = data['总电量']

data2 = pd.read_excel('predict_data/test.xlsx')
Xt = data2[['人口','城镇人口','工业GDP']]
yt = data2['总电量']

model = LinearRegression()
model.fit(X, y)
y_p = model.predict(X)

t_fearurizer=PolynomialFeatures(degree=3)
X_train_k=t_fearurizer.fit_transform(X)
modelk=LinearRegression()
modelk.fit(X_train_k,y)
print(modelk.score(X_train_k,y))
print(modelk.coef_)