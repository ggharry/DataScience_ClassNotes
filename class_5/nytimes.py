import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import log
from sklearn import linear_model
from statsmodels.formula.api import ols

from mpl_toolkits.mplot3d import Axes3D

# Set some Pandas options
pd.set_option('max_columns', 30)
pd.set_option('max_rows', 20)

# Default Plotting Size
mpl.rc("figure", figsize=(20, 8))

# Store data in a consistent place
DATA_DIR = 'data/'

nytimes = pd.read_csv(DATA_DIR + 'nyagg.csv')

# Two Features: Age + Gender to predict CTR
regrTwoFeatures = linear_model.LinearRegression()

length = len(nytimes['Age'].values)

age = [[x] for x in nytimes['Age'].values]
gender = [[x] for x in nytimes['Gender'].values]

ageAndGender = [[nytimes['Age'].values[i], nytimes['Gender'].values[i]] for i in range(length)]
ctr = nytimes['Ctr'].values

regrTwoFeatures.fit(ageAndGender, ctr)

print "Two Features: Age + Gender to predict CTR"
print "-----------------------"
print regrTwoFeatures.coef_
print np.sum((regrTwoFeatures.predict(ageAndGender) - ctr) ** 2)
print regrTwoFeatures.score(ageAndGender, ctr)

ax = Axes3D(plt.gcf())
ax.scatter(age, gender, ctr)
plt.show()