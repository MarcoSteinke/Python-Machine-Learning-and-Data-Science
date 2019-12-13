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

## 3 Two dimensional plots or Scatter Plots
`The files required to understand this chapter are located in 3_Scatter_Plots_and_Proportionals`

## 3.1 Scatter Plots

The Subchapter Scatter Plots will teach you about the 
definition and generation of Scatter Plots

#### Scatter Plot
A Scatter plot is a plot of random values which will be
represented by dots in the x-y-plane. Per definition you
will need two sets or collections to generate a Scatter Plot. Additionally the two collections need to have the
same length.

## Generation of a Scatter Plot:

The following image shows the generated Scatter Plot

![](https://github.com/maste150hhu/Python-Machine-Learning-and-Data-Science/blob/master/3_Scatter_Plots_and_Proportionals/ScatterPlot.png)

As you can see in the picture, the dots are widely spread around the graph. It seems as if the dots are
all closer to the two coordinate-axes

You will find the Python-Code for this in 3_Scatter_Plots_and_Proportionals in ScatterPlot.py

## 3.2 Application of Scatter plots

Assert that we got some information about cars from a
mysterious source. He asks us to analyse his data to find
out if newer cars are really faster than the older ones,
because he does not want to waste his money.

Since we learned how to scatter sets of data we could
give it a try.

The mysterious source gave us two sets of data, the first
consists of the ages of certain cars and the second one
gives us any kind of unit which measures the speed. The higher the unit, the faster the car.

Let's scatter some cars!

#### Graph

![](https://github.com/maste150hhu/Python-Machine-Learning-and-Data-Science/blob/master/3_Scatter_Plots_and_Proportionals/Cars.png)