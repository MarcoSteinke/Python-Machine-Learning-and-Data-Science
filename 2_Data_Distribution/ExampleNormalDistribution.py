import numpy
from scipy import stats
from matplotlib import pyplot as plt

data = numpy.random.normal(6, 1, 10000)

plt.hist(data)

plt.show()