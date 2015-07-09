from sklearn import feature_selection as fs

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

from sklearn import linear_model

def f_regression_feature_selection(input, response):    
# use this against your feature matrix to determine p-values for
# each feature (we care about the second array it returns).
    return fs.univariate_selection.f_regression(input, response)

cars = pd.read_csv('data/cars1920.csv')

lm = linear_model.LinearRegression()
log_lm = linear_model.LinearRegression()

body_squared = zip(cars['speed'].values, cars['dist'].values)
brain = cars['dist'].values

results = []
for alpha in [1,2,5,10,20,50,100,200,500,1000]:
    ridge = linear_model.Ridge(alpha=alpha)
    ridge.fit(body_squared, brain)
    score = ridge.score(body_squared, brain)
    results.append((alpha, score))

print results