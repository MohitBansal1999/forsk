
# Code Challenge 

# Find the mean, median, mode, and range for the following list of values:
# 13, 18, 13, 14, 13, 16, 14, 21, 13


#Answer : Mean = 15, Median = 14 , Mode = 13 , Range = 21 - 13 = 8



"""
Code Challenge
  Name: 
    Space Seperated data
  Filename: 
    space_numpy.py
  Problem Statement:
    You are given a 9 space separated numbers. 
    Write a python code to convert it into a 3x3 NumPy array of integers.
  Input:O
    6 9 2 3 5 8 1 5 4
  Output:
      [[6 9 2]
      [3 5 8]
      [1 5 4]]
  
"""
l=[6, 9, 2, 3, 5, 8, 1, 5, 4]
l=np.array(l)
l=l.reshape((3,3))
print(l)

"""
Code Challenge
  Name: 
    Random Data
  Filename: 
    random_data.py
  Problem Statement:
    Create a random array of 40 integers from 5 - 15 using NumPy. 
    Find the most frequent value with and without Numpy.
  Hint:
      Try to use the Counter class
      
"""
import numpy as np
x=np.random.randint(5,15,40)
x=np.array(x)
from scipy import stats
print("Mode value is: ", stats.mode(x)[0])




"""
Code Challenge
  Name: 
    E-commerce Data Exploration
  Filename: 
    ecommerce.py
  Problem Statement:
      To create an array of random e-commerce data of total amount spent per transaction. 
      Segment this incomes data into 50 buckets (number of bars) and plot it as a histogram.
      Find the mean and median of this data using NumPy package.
      Add outliers 
          
  Hint:
      Execute the code snippet below.
      import numpy as np
      import matplotlib.pyplot as plt
      incomes = np.random.normal(100.0, 20.0, 10000)
      print (incomes)
 
    outlier is an observation that lies an abnormal distance from other values 
    
"""
import numpy as np
import matplotlib.pyplot as plt
incomes = np.random.normal(100.0, 20.0, 10000)
plt.hist(incomes, 50)
print("Mean value is: ", np.mean(incomes))
print("Median value is: ", np.median(incomes))

incomes = np.append(incomes, [10000000000])
plt.hist(incomes, 50)
print("Mean value is: ", np.mean(incomes))
print("Median value is: ", np.median(incomes))


"""
Code Challenge
  Name: 
    Normally Distributed Random Data
  Filename: 
    normal_dist.py
  Problem Statement:
    Create a normally distributed random data with parameters:
    Centered around 150.
    Standard Deviation of 20.
    Total 1000 data points.
    
    Plot the histogram using matplotlib (bucket size =100) and observe the shape.
    Calculate Standard Deviation and Variance. 
"""

import numpy as np
x = np.random.normal(150, 20, 1000)

print("Mean value is: ", np.mean(x))
print("Median value is: ", np.median(x))

from scipy import stats
print("Mode value is: ", stats.mode(x)[0])
print("Standard Deviation is: ", np.std(x))

import matplotlib.pyplot as plt
plt.hist(x, 100)
plt.show()
plt.boxplot(x)
