import numpy
from scipy import stats

# Let a dice roll 200-times
dataSet = numpy.random.uniform(1, 6, 2000)
dataSetRounded = []

i = 0
for result in dataSet:
    dataSetRounded.append( round(result) )

# Get the mean of the dataSet
print("Mean = ", numpy.mean(dataSetRounded))
print("Median = ", numpy.median(numpy.sort(dataSetRounded)))
print("Minimum = ", numpy.min(dataSetRounded))
print("Maximum = ", numpy.max(dataSetRounded))
print("Mode = ", stats.mode(dataSetRounded).mode[0], " with a count of", stats.mode(dataSetRounded).count[0])

# The results show us that our randomized object was a dice because we can apply all statistical properties of a dice to our model.