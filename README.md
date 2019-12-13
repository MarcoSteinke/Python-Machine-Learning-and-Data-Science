# Python-Machine-Learning-and-Data-Science
This is a repository where i try to get into Data Science and Machine Learning using Python (NumPy, SciPy)

## 1 Data Science Basics
`The files required to understand this chapter are located in 1_Data_Science_Basics`

The basics consist of statistical method such as the Mean, Median, Mode, Standard Deviation.

#### Mean
Average value of a set or collection

#### Median
After sorting the set or collection, the median is the value in the center of the set or collection. Assert N is the cardinality of the set. Then there will be N/2 elements smaller than the median and N/2 bigger than it.

#### Mode
The mode counts the occurence of each element and returns
the most common one.

#### Standard Deviation
The standard deviation gives a radius around the mean in which 68.1% of the elements are also included.

## 2 Generation of Big Data
`The files required to understand this chapter are located in 2_Data_Distribution`

### 2.1 Data Sets
In this chapter I tried to generate some sets of Data
to learn with. In the following examples I will also try
to generate User Information and analyse it.

### 2.2 Plotting: Histogram
After the generation of Data Sets i started to plot them.
First I let PyPlot count the occurences of the certain
values and plot them in a Histogram.

#### Histogram
A Histogram is a graphic which counts the occurence of each element from a collection or a set or divides the whole set into N sections and displays the result as pillars.

You will find a picture here:

![This picture shows the Histogram generated in 2_Data_Distribution/Histogram.py](https://github.com/maste150hhu/Python-Machine-Learning-and-Data-Science/blob/master/2_Data_Distribution/Histogram.png)

### 2.3 Normal Data Distribution
In Statistics and Probability Theory there are different kinds of distributions. In the previous examples the values were pseudo-random without any distributions.

In this chapter I will use the Gaussian data distribution which is also called the normal data distribution. 

#### Normal Data Distribution
The random values are concentrated around a given value by a specific radius. (Distance)

The following Histogram will demonstrate the effect of the Data Distribution:

![](https://github.com/maste150hhu/Python-Machine-Learning-and-Data-Science/blob/master/2_Data_Distribution/NormalDistHistogram.png)

In this picture you can see an application of the definition of Normal Data Distribution.

#### Bell Curve
The graph of a normal distribution is also often called
a Bell Curve because you can see it's specific form of
a bell.

#### Result of the Normal Data Distribution
The call `numpy.random.normal(5, 1, 100000)` created a set of values where we set the mean to 5.0 and MOST (68.1%) of the values spread around 5 with a radius of 1.
So most values are between 4 and 6. You can also see the peak of the Bell Curve being at around 5.0 which was our mean.