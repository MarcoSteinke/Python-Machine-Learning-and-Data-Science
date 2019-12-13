import numpy
import matplotlib.pyplot as plt

# A ScatterPlot displays all values in the
# data set as points

# Define two data sets
y = [5,7,8,7,2,17,2,9,4,11,12,9,6]
x = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# Now lets scatter them
plt.scatter(x, y)
plt.show()