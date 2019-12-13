import numpy

speed = [86,87,88,86,87,85,86]

print("Average value of speed is " + str(numpy.mean(speed)))
print("Standard Deviation of speed is " + str(numpy.std(speed)))
print("Range from " + str(numpy.mean(speed) - numpy.std(speed)) + " to " + str(numpy.mean(speed) + numpy.std(speed)))
print
print("Variance is " + str(numpy.var(speed)))
print
print("Square of standard deviation must be equal to variance, let's test this: ")
print(numpy.std(speed)**2)