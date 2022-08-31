# fit a fifth degree polynomial to the economic data
from numpy import arange, exp
from pandas import read_csv
from scipy.optimize import curve_fit
from matplotlib import pyplot

# 
# def objective(x, a, b):
# 	return a / x + b

def objective(x, a, c):
    return a * x ** 2 + c

# load the dataset
dataframe = read_csv("data.csv", header=None)
data = dataframe.values
# choose the input and output variables
x, y = data[:, 0], data[:, -1]
# curve fit
popt, _ = curve_fit(objective, x, y)
# summarize the parameter values
a, c = popt
print("{}x^2 + {}".format(a, c))
# plot input vs output
pyplot.scatter(x, y)
# define a sequence of inputs between the smallest and largest known inputs
x_line = arange(min(x), max(x), 1)
# calculate the output for the range
y_line = objective(x_line, a, c)
# create a line plot for the mapping function
pyplot.plot(x_line, y_line, '--', color='red')
pyplot.show()