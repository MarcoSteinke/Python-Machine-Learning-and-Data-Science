import matplotlib.pyplot as plt
import numpy
from scipy import stats

class_test_result = [3, 4, 4, 3, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1]

print("The average student scored a ", round(numpy.mean(class_test_result), 2), " in this class test")
print(class_test_result.__len__(), " students participated in this test.")

plt.hist(class_test_result)

plt.show()