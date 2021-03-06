#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 16:21:14 2019

@author: ken
"""


# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

'''from sklearn.model_selection import train_test_split
#X_train,Y_train,X_test, Y_test = train_test_split(X,y, test_size =0.2, random_state = 0)'''

from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 1000, random_state =0)
regressor.fit(X,y)



from sklearn.linear_model import LinearRegression


y_pred = regressor.predict([[6.5]])


X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape(len(X_grid),1)
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict((X_grid)), color = 'blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

lnreg.predict(polyreg.fit_transform([[6.5]]))