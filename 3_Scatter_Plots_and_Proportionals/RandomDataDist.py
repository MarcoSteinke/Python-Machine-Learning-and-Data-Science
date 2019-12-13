import numpy
import matplotlib.pyplot as plt

# First generate the bigData 
# by using the Normal Data Distribution
# This time we will need two sets to scatter them
bigDataX = numpy.random.normal(5.0, 1.0, 1000)
bigDataY = numpy.random.normal(10.0, 2.0, 1000)

# Now we will plot the Scatter Plot for both of our sets. This will lead PyPlot to plot 1000 points.
plt.scatter(bigDataX, bigDataY);
plt.show()