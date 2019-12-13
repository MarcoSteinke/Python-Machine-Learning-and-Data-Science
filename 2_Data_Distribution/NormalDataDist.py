import numpy
import matplotlib.pyplot as plt

# First generate the bigData 
# by using the Normal Data Distribution
bigData = numpy.random.normal(5.0, 1.0, 100000)

# Now we will plot the Histogram again. 
plt.hist(bigData, 100)
plt.show()