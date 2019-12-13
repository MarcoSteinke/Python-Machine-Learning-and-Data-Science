import numpy
import matplotlib.pyplot as plt

# How can BigData be shown to the user?

# For example by using a Histogram
# Please inform yourself about Histograms. In this Example
# the Histogram shows how often a dice rolled a certain number
# The experiment consisted of 100000 rolls.

# Generate a set of Big Data
bigDataToPlot = numpy.random.uniform(1, 6, 100000)

# Use matplotlib.pyplot to draw the Histogram
plt.hist(bigDataToPlot, 6)

# Now show the graphic to the user
plt.show()