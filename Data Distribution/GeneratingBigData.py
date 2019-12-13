import numpy
from scipy import stats

# I now know how to calculate Mean, Median and Percentiles
# But how do I get Data for testing purposes?

# Numpy offers a feature to do so:

# In this example I am generating 200 values between 40 and 68 
bigData = numpy.random.uniform(40, 68, 200)

for num in bigData:
    num = round(num)

print(bigData)
print
# Now lets do the same as before:

print("Mean = " + str(numpy.mean(bigData)))
print("Median = " + str(numpy.median(bigData)))
print("Mode = " + str(stats.mode(bigData)))