import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import log
from sklearn import linear_model
from statsmodels.formula.api import ols
from numpy import exp

# Set some Pandas options
pd.set_option('max_columns', 30)
pd.set_option('max_rows', 20)

# Default Plotting Size
mpl.rc("figure", figsize=(20, 8))

# Store data in a consistent place
DATA_DIR = 'data/'

mammals = pd.read_csv(DATA_DIR + 'mammals.csv')
# print mammals.describe()

# plt.scatter(mammals['body'], mammals['brain'])
# plt.show()

# sns.lmplot("body", "brain", mammals);

# plt.hist(mammals['body'], bins=range(0, 10000, 100))
# plt.show()

# sns.distplot(mammals['body']);

# plt.hist(mammals['brain'], bins=range(0, 10000, 100))
# plt.show()

# mammals['log_body'] = log(mammals['body'])
# mammals['log_brain'] = log(mammals['brain'])

# plt.scatter(mammals['log_body'], mammals['log_brain'])
# plt.show()

# # Make the model object
# regr = linear_model.LinearRegression()

# # Fit the data
# body = [[x] for x in mammals['body'].values]
# brain = mammals['brain'].values

# regr.fit(body, brain)

# # Display the coefficients:
# print regr.coef_

# # Display our SSE:
# print np.sum((regr.predict(body) - brain) ** 2)

# # Scoring our model (closer to 1 is better!)
# print regr.score(body, brain)

# plt.scatter(body, brain)
# plt.plot(body, regr.predict(body), color='blue', linewidth=1)
# plt.show()

# results = ols('brain ~ body', mammals).fit()
# print(results.summary())

# Make the model object
regr = linear_model.LinearRegression()

mammals['log_body'] = log(mammals['body'])
mammals['log_brain'] = log(mammals['brain'])

# Fit the data
body = [[x] for x in mammals['log_body'].values]
brain = mammals['log_brain'].values

regr.fit(body, brain)

# Display the coefficients:
print regr.coef_

# Display our SSE:
print np.sum((regr.predict(body) - brain) ** 2)

# Scoring our model (closer to 1 is better!)
print regr.score(body, brain)

plt.scatter(body, brain)
plt.plot(body, regr.predict(body), color='blue', linewidth=1)
plt.show()

results = ols('log_brain ~ log_body', mammals).fit()
print(results.summary())

# The model can predict an answer
print exp(regr.predict([[log(4)]]))