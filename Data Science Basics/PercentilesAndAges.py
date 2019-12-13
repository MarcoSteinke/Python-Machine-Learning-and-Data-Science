import numpy

print("I want to find the value of the array which is bigger than 75% of the rest.")
print("Lets make an example: Imagine you write down the ages of all people living in your street")
print
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
print(ages)
print
# In this context I want to know which is the exact age where 75% of the people have this age or are younger.
# Therefore we will need the so called Percentiles
#Percentile: A number that describes a which value where a certain percentage of the other values are lower than
# "To do so in Python: "
percentileOfAges = numpy.percentile(ages, 75)
print("Percentile of 75% of ages = " + str(percentileOfAges))