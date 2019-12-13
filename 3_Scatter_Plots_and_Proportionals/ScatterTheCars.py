import numpy
import matplotlib.pyplot as plt


# As mentioned in the description, we got two 
# data sets which consist of the ages and the speeds
# of the cars
agesOfCars = [6,9,12,11,4,9,2,17,2,7,8,7,5]
speedOfCars = [286, 285, 277, 278, 294, 287, 303, 286, 311, 288, 287, 286, 299]

# In the next step we have to scatter the cars with the
# method seen in ScatterPlot.py or 3.1
plt.scatter(agesOfCars, speedOfCars)
plt.show();