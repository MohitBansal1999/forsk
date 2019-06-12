'''Code Challenge:
dataset: BreadBasket_DMS.csv

Q1. In this code challenge, you are given a dataset which has data and time wise transaction on a bakery retail store.
1. Draw the pie chart of top 15 selling items.
2. Find the associations of items where min support should be 0.0025, min_confidence=0.2, min_lift=3.
3. Out of given results sets, show only names of the associated item from given result row wise.
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from apyori import apriori

dataset=pd.read_csv("BreadBasket_DMS.csv")

#1
item=[]
number=[]
x=0
a=dataset["Item"].value_counts()
for i in a:
    if (a[a == i].index[0] != "NONE") and x<15:
        item.append(a[a == i].index[0])
        number.append(i)
        x=x+1
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','gold', 'yellowgreen', 'lightcoral', 'lightskyblue','gold', 'yellowgreen', 'lightcoral', 'lightskyblue','gold', 'yellowgreen', 'lightcoral']
explode = (0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0,0)  

plt.pie(number, explode=explode, labels=item, colors=colors, autopct='%1.1f%%', shadow=True, startangle=0)
plt.axis('equal')  
plt.show()

#2
item=[]
b=1
a=[]
a.append(str(dataset.iloc[0,3]))
for i in range(1,21293):
    
    if dataset.iloc[i,2]==b and dataset.iloc[i,3]!="NONE":
        a.append(dataset.iloc[i,3])
    elif dataset.iloc[i,3]!="NONE":
        item.append(a)
        a=[]
        a.append(dataset.iloc[i,3])
        b=dataset.iloc[i,2]
        
rules = apriori(item, min_support = 0.0025, min_confidence = 0.2, min_lift = 3)

results = list(rules)
#3
for item in results:
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])
    print("Support: " + str(item[1]))
    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")
    
    
'''Code Challenge:
Datset: Market_Basket_Optimization.csv
Q2. In today's demo sesssion, we did not handle the null values before fitting the data to model, remove the null values from each row and perform the associations once again.
Also draw the bar chart of top 10 edibles.
'''
import pandas as pd
from apyori import apriori

# Data Preprocessing
transactions = []

with open("Market_Basket_Optimisation.csv") as f:
    for i, line in enumerate(f):             
        transactions.append(line.split(","))

# Training Apriori on the dataset
rules = apriori(transactions, min_support = 0.003, min_confidence = 0.25, min_lift = 4)

# Visualising the results
results = list(rules)

for item in results:
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])
    print("Support: " + str(item[1]))
    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")