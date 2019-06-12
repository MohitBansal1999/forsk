# -*- coding: utf-8 -*-
"""
Created on Mon May 13 10:34:42 2019

@author: Mohit Bansal
"""

#1
def f(x):
    if x==x[::-1]:
        return True
    else:
        return False
list1=input("enter numbers seperated by comma: ")
a=any(filter(f,list1.split(',')))
print(a)


#2
import random
names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']
name=list(map(lambda x : random.choice(code_names) ,names))
print(name)

#3
names = ['Mary', 'Isla', 'Sam']
names=list(map(lambda x : hash(x) ,names))
print (names)

#4
from functools import reduce 
people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]
height_total, height_count= 0 , 0
def f1(x):
    if 'height' in x:
        return True
    else:
        return False
def f21(x):
    return x['height']
def f3(height_total,height_count):
    if height_count>0:
        return height_total / height_count


a=list(filter(f1,people))
b=sum(list(map(f21,a)))
if(len(a)>0):
        average_height=f3(b,len(a))
print(average_height)
    
    
#5 height
#without map
list1=[[34587, 'Learning Python', 'Mark Lutz' , 4 ,40.95],
    [98762 ,'Programming Python',' Mark Lutz', 5, 56.80],
    [77226,' Head First Python', 'Paul Barry' ,3, 32.95],
    [88112 ,'Einführung in Python3',' Bernd Klein' , 3 ,24.99 ]]
list2=[]
for i in list1:
    if (i[3]*i[4])<100:
        x=(i[0],((i[3]*i[4])+10))
    else:
        x=(i[0],i[3]*i[4])
    list2.append(x)
print(list2)

#with map
list2=[]
def f1(i):
    if (i[3]*i[4])<100:
        return (i[0],((i[3]*i[4])+10))
    else:
        return (i[0],i[3]*i[4])
list2=list(map(f1,list1))
print(list2)


#6 bookshop1
invoice = []

orders = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95], 
         ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
           ["77226", "Head First Python, Paul Barry", 3,32.95],
           ["88112", "Einführung in Python3, Bernd Klein",  3, 24.99]]


for new in orders :
    orderNum = int(new[0])
    quantity = new[2]
    price = new[3]
    total = quantity * price
    if total<=100:
        total =total + 10
    else:
        total
    invoice.append((orderNum,total))  
    
print(invoice)    

#with 
orders = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95], 
         ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
           ["77226", "Head First Python, Paul Barry", 3,32.95],
           ["88112", "Einführung in Python3, Bernd Klein",  3, 24.99]]

min_order = 100
order_summary = list(map(lambda x: (x[0], round(x[2] * x[3],2)), orders))
print(order_summary)

invoice_totals = list(map(lambda x: x if x[1] >= min_order else (x[0], x[1] + 10), order_summary))
print(invoice_totals)
# or 
invoice_totals = list(map(lambda x: x if x[1] >= min_order else (x[0], x[1] + 10), 
                    map(lambda x: (x[0],round(x[2] * x[3],2)), orders)))
print(invoice_totals)

#7 bookshop2
#with
from functools import reduce

orders = [ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
         [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
         [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
           [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]

min_order = 100

invoice_totals = list(map(lambda x: [x[0]] + list(map(lambda y: y[1]*y[2], x[1:])), orders))
print (invoice_totals)

invoice_totals = list(map(lambda x: [x[0]] + [round(reduce(lambda a,b: a + b, x[1:]),2)], invoice_totals))
print (invoice_totals)

invoice_totals = list(map(lambda x: x  if x[1] >= min_order else (x[0], x[1] + 10), invoice_totals))
print (invoice_totals)



# without
from collections import OrderedDict

invoice = []
dict1 = OrderedDict()



orders = [ ['1', ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
         ['2', ("5464", 9, 9.99), ("9744", 9, 44.95)],
         ['3', ("5464", 9, 9.99), ("88112", 11, 24.99)],
         ['4', ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]


for newList in orders:
        orderNum = newList[0]
        info = (newList[1:])
        for new in info:
           invoice.append([orderNum,(list(new)[1] * list(new)[2])])
       
for new in invoice:
        dict1[new[0]] = dict1.get(new[0], 0) +  new[1] 
        
        if(dict1[new[0]] < 100):
             print((new[0],dict1[new[0]]))
        else:
          print(dict1)  