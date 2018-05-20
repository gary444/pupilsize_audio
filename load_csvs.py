import numpy as np
from numpy import genfromtxt

#values from csv file
inValues = genfromtxt('set2.csv', delimiter=',')
targetValue = inValues[0]
values = np.delete(inValues,0)

