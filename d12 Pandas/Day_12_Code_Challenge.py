"""
Code Challenge
  Name: 
    Titanic Analysis
  Filename: 
    titanic.py
  Dataset:
    training_titanic.csv
  Problem Statement:
      It’s a real-world data containing the details of titanic ships 
      passengers list.
      Import the training set "training_titanic.csv"
  Answer the Following:
      How many people in the given training set survived the disaster ?
      How many people in the given training set died ?
      Calculate and print the survival rates as proportions (percentage) 
      by setting the normalize argument to True.
      Males that survived vs males that passed away
      Females that survived vs Females that passed away
      
      Does age play a role?
      since it's probable that children were saved first.
      
      Another variable that could influence survival is age; 
      since it's probable that children were saved first.

      You can test this by creating a new column with a categorical variable Child. 
      Child will take the value 1 in cases where age is less than 18, 
      and a value of 0 in cases where age is greater than or equal to 18.
 
      Then assign the value 0 to observations where the passenger 
      is greater than or equal to 18 years in the new Child column.
      Compare the normalized survival rates for those who are <18 and 
      those who are older. 
    
      To add this new variable you need to do two things
        1.     create a new column, and
        2.     Provide the values for each observation (i.e., row) based on the age of the passenger.
    
  Hint: 
      To calculate this, you can use the value_counts() method in 
      combination with standard bracket notation to select a single column of
      a DataFrame
"""
import pandas as pd
df=pd.read_csv("C:\\Users\\Mohit Bansal\\Desktop\\Forsk_training\\d12\\training_titanic.csv")
print("People survived : ",df["Survived"].value_counts().tolist()[1])
print("People died : ",df["Survived"].value_counts().tolist()[0])
df['Survived'].value_counts(normalize = True) #people survied percentage
df[(df["Sex"]=="male")]["Survived"].value_counts() #male survived vs male died
df[(df["Sex"]=="female")]["Survived"].value_counts() #female survived vs female died
df["Children"] = df["Age"].map(lambda x: 1 if x > 18 else 0 )
df["Children"].value_counts()
"""
Code Challenge
  Name: 
      Exploratory Data Analysis - Automobile
  Filename: 
      automobile.py
  Dataset:
      Automobile.csv
  Problem Statement:
      Perform the following task :
      1. Handle the missing values for Price column
      2. Get the values from Price column into a numpy.ndarray
      3. Calculate the Minimum Price, Maximum Price, Average Price and Standard Deviation of Price
"""
import pandas as pd
import numpy as np
df1=pd.read_csv("C:\\Users\\Mohit Bansal\\Desktop\\Forsk_training\\d12\\Automobile.csv")
df1["price"]=df1["price"].fillna(round(df1["price"].mean())) #nan handling
price=np.array(df1["price"]) #Get the values from Price column into a numpy.ndarray
print("Standard deviation:",np.std(price),"\nAvg or Mean:",np.mean(price),"\nMin:",np.min(price),"\nMax:",np.max(price) )
"""
Code Challenge
  Name: 
    Thanks giving Analysis
  Filename: 
    Thanksgiving.py
  Problem Statement:
    Read the thanksgiving-2015-poll-data.csv file and 
    perform the following task :

    Discover regional and income-based patterns in what Americans eat for 
    Thanksgiving dinner

    Convert the column name to single word names
    
    Using the apply method to Gender column to convert Male & Female
    Using the apply method to clean up income
    (Range to a average number, X and up to X, Prefer not to answer to NaN)
    
    compare income between people who tend to eat homemade cranberry sauce for
    Thanksgiving vs people who eat canned cranberry sauce?
    
    find the average income for people who served each type of cranberry sauce
    for Thanksgiving (Canned, Homemade, None, etc).
    
    Plotting the results of aggregation
    
    Do people in Suburban areas eat more Tofurkey than people in Rural areas?
    Where do people go to Black Friday sales most often?
    Is there a correlation between praying on Thanksgiving and income?
    What income groups are most likely to have homemade cranberry sauce?

    Verify a pattern:
        People who have Turducken and Homemade cranberry sauce seem to have 
        high household incomes.
        People who eat Canned cranberry sauce tend to have lower incomes, 
        but those who also have Roast Beef have the lowest incomes
        
    Find the number of people who live in each area type (Rural, Suburban, etc)
    who eat different kinds of main dishes for Thanksgiving:
        
  Hint:

"""
import pandas as pd
import numpy as np
df2=pd.read_csv("thanksgiving.csv",encoding="windows 1252")

"""
Code Challenge
  Name: 
    Telecom Churn Analysis
  Dataset:
    Telecom_churn.csv
  Filename: 
    telecom_churn.py
  Problem Statement:
    Read the telecom_churn.csv file and perform the following task :
        To perfrom analysis on the Telecom industry churn dataset -
    1. Predict the count of Churned customer availing both voice mail plan and international plan schema
    2. Total charges for international calls made by churned and non-churned customer and visualize it
    3. Predict the state having highest night call minutes for churned customer
    4. Visualize -
        a. the most popular call type among churned user
        b. the minimum charges among all call type among churned user
    5. Which category of customer having maximum account lenght? Predict and print it
    6. Predict a relation between the customer and customer care service that whether churned customer have shown their concern to inform the customer care service about their problem or not
    7. In which area code the international plan is most availed?
        
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df3=pd.read_csv("Telecom_churn.csv")
#1
df3[(df3["international plan"]=="yes") & (df3["voice mail plan"]=="yes")]["phone number"].count() 
print(df3[df3["churn"]==True]["total intl charge"].sum()) #2
print(df3[df3["churn"]==False]["total intl charge"].sum()) #2
from scipy import stats
#3
df3[df3["total night minutes"]==int(stats.mode(np.array(df3[df3["churn"]==True]["total night minutes"]))[0])]["state"] 
#4a
labels = ['Day', 'Eve', 'Night']
sizes=[]
colors = ['gold', 'yellowgreen', 'lightcoral']
a,b,c=df3[df3["churn"]==True]["total day calls"].sum(),df3[df3["churn"]==True]["total eve calls"].sum(),df3[df3["churn"]==True]["total night calls"].sum()
sizes.append(a)
sizes.append(b)
sizes.append(c)
if a>b and a>c:
    explode = (0.1, 0, 0)
elif b>c:
    explode = (0, 0.1, 0)
else:
    explode = (0, 0, 0.1)
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=0)

#4b

#5


   
