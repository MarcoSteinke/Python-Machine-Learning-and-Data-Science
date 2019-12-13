import numpy
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]


print("(1) speed before sort")
print(speed)

mean = numpy.mean(speed)

print
print("Standard deviation from ", mean, " is: ")
print(numpy.std(speed))

print
print("(2) The mean of speed is ")
print(mean)

speedAfterSort = sorted(speed)

afterSort = ""
print
print("(3) speed after sort:")

print(speedAfterSort)

median = numpy.median(speed)

print
print("(4) The median of speed is ")
print(median)

mostCommonValue = stats.mode(speed)

print
print("most common value:")
print(mostCommonValue)