

"""
Code Challenge: Simple Linear Regression
  Name: 
    Food Truck Profit Prediction Tool
  Filename: 
    Foodtruck.py
  Dataset:
    Foodtruck.csv
  Problem Statement:
    Suppose you are the CEO of a restaurant franchise and are considering 
    different cities for opening a new outlet. 
    
    The chain already has food-trucks in various cities and you have data for profits 
    and populations from the cities. 
    
    You would like to use this data to help you select which city to expand to next.
    
    Perform Simple Linear regression to predict the profit based on the 
    population observed and visualize the result.
    
    Based on the above trained results, what will be your estimated profit, 
    
    If you set up your outlet in Jaipur? 
    (Current population in Jaipur is 3.073 million)
        
  Hint: 
    You will implement linear regression to predict the profits for a 
    food chain company.
    Foodtruck.csv contains the dataset for our linear regression problem. 
    The first column is the population of a city and the second column is the 
    profit of a food truck in that city. 
    A negative value for profit indicates a loss.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("Foodtruck.csv")
features=df.iloc[:,:-1].values
labels=df.iloc[:,1:].values

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()

regressor.fit(features,labels)
a=np.array([3]).reshape(1,1)
regressor.predict(a)


plt.scatter(features,labels)
plt.scatter(a, regressor.predict(a), color = 'red')
plt.plot(features, regressor.predict(features), color = 'red')

"""
Code Challenge: Simple Linear Regression

  Name: 
    Box Office Collection Prediction Tool
  Filename: 
    Bahubali2vsDangal.py
  Dataset:
    Bahubali2vsDangal.csv
  Problem Statement:
    It contains Data of Day wise collections of the movies Bahubali 2 and Dangal 
    (in crores) for the first 9 days.
    
    Now, you have to write a python code to predict which movie would collect 
    more on the 10th day.
  Hint:
    First Approach - Create two models, one for Bahubali and another for Dangal
    Second Approach - Create one model with two labels
"""
#using first approach
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1=pd.read_csv("Bahubali2_vs_Dangal.csv")

features=df1.iloc[:,:-2].values
labelsB=df1.iloc[:,1:2].values
labelsD=df1.iloc[:,2:].values

from sklearn.linear_model import LinearRegression
regressor1=LinearRegression()
regressor1.fit(features,labelsB)

from sklearn.linear_model import LinearRegression
regressor2=LinearRegression()
regressor2.fit(features,labelsD)

a=np.array([10]).reshape(1,1)
print("Bahubali 10th day => ",regressor1.predict(a))
print("Dangal 10th day => ",regressor2.predict(a))

#using second approach
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df1=pd.read_csv("Bahubali2_vs_Dangal.csv")

features=df1.iloc[:,:-2].values
labels=df1.iloc[:,1:].values

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(features,labels)

a=np.array([10]).reshape(1,1)
x=regressor.predict(a)
print("Bahubali 10th day => ",x[0,0])
print("Dangal 10th day => ",x[0,1])

