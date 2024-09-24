import pandas as pd
from pylab import *

titanic = pd.read_csv('titanic.csv')
_average = titanic.groupby('Pclass')['Fare'].mean()
x = titanic['Pclass']
y = _average
plt.bar(x,y)
plt.xlabel('Pclass')
plt.ylabel('Average')

show()