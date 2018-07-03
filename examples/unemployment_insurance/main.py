#==================================================================
#
#  This example use the data from Google data science blog post
#  http://www.unofficialgoogledatascience.com/2017/07/fitting-bayesian-structural-time-series.html
#
#  Make sure your working directly is pointing to the folder where
#  `main.py` locates and `data.csv` is in the same folder.
#
#==================================================================

# Read data file
import os
this_dir = os.getcwd()
DATA_PATH = os.path.join(this_dir, "data.csv")
data_file = open(DATA_PATH, 'r')

variables = data_file.readline().strip().split(',')
data_map = {}
for var in variables:
    data_map[var] = []

for line in data_file:
    for i, data_piece in enumerate(line.strip().split(',')):
        data_map[variables[i]].append(float(data_piece))

# Extract and store the data.
time_series = data_map[variables[0]]
features = [[data_map[variables[j]][i] for j in range(1, len(variables)) ]
            for i in range(len(time_series))]

# Build a simple model
from pydlm import dlm, trend, seasonality

# A linear trend
linear_trend = trend(degree=1, discount=0.95, name='linear_trend', w=10)
# A seasonality
seasonal52 = seasonality(period=52, discount=0.99, name='seasonal52', w=10)

simple_dlm = dlm(time_series) + linear_trend + seasonal52
simple_dlm.fit()

simple_dlm.getMean(filterType='backwardSmoother', name='linear_trend')
simple_dlm.getMean(filterType='backwardSmoother', name='seasonal52')
# Plot the prediction give the first 350 weeks and forcast the next 200 weeks.
simple_dlm.predictN(N=200, date=350)
# Plot the prediction give the first 250 weeks and forcast the next 200 weeks.
simple_dlm.predictN(N=200, date=250)

# Build a dynamic regression model
from pydlm import dynamic
regressor10 = dynamic(features=features, discount=1.0, name='regressor10', w=10)
drm = dlm(time_series) + linear_trend + seasonal52 + regressor10
drm.fit()

drm.getMean(filterType='backwardSmoother', name='linear_trend')
drm.getMean(filterType='backwardSmoother', name='seasonal52')
drm.getMean(filterType='backwardSmoother', name='regressor10')
# Predict given the first 300 weeks and forcast the next 150 weeks.
drm.predictN(N=150, date=300)
# Predict given the first 250 weeks and forcast the next 200 weeks.
drm.predictN(N=200, date=250)
