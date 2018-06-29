
import random as rand
import matplotlib.pyplot as plt 
from sklearn import preprocessing, metrics, linear_model, model_selection
import pandas as pd 
import numpy as np 
import matplotlib.dates as mdates

year = [rand.randint(2015, 2020) for i in range(100)]
month = [rand.randint(1, 12) for i in range(100)]
day = [rand.randint(1, 30) for i in range(100)]

day = sorted(day)
month = sorted(month)
year=sorted(year)
ticks = pd.Series([rand.uniform(1,1.25)*i for i in range(100)])

dates = [None] * 100
for i in range(100):
	val = str(year[i]) + '/' + str(month[i]) + '/' + str(day[i])
	dates[i] = val

years = []
months = []
days = []

for line in dates:
	array = line.split('/')
	years.append(int(array[0]))
	months.append(int(array[1]))
	days.append(int(array[2]))

df = pd.DataFrame()

df['day'] = pd.Series(days)
df['month'] = pd.Series(months)
df['year'] = pd.Series(years)

x = df
y = ticks

x = preprocessing.normalize(x)
x_train = x[:90]
y_train = y[:90]
x_test = x[90:]
y_test = y[90:]

clf = linear_model.LinearRegression()
clf.fit(x_train, y_train)
forecast_set = clf.predict(x_test)

x_train = np.array(x_train)
x = [str(i[0])+ '-' + str(i[1])+ '-'+ str(i[2]) for i in x_train]
predictions = [str(i[0])+ '-' + str(i[1])+ '-'+ str(i[2]) for i in np.array(x_test)]
fig = plt.figure()
ax= plt.subplot2grid((1,1), (0,0))
print(predictions)
print(forecast_set)
ax.plot_date(x, y_train)
ax.plot_date(predictions, forecast_set)
ax.plot
for label in ax.xaxis.get_ticklabels():
	label.set_rotation(50)
	label.set_fontsize(8)
plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
plt.show()


