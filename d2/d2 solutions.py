# -*- coding: utf-8 -*-
"""
Created on Sat May 11 09:38:00 2019

@author: Mohit Bansal
"""

#1
list=[]
for i in range(1,21):
    list.append(i)
print(list)
print(list[::2])
print(list[1::2])

#2
def leap_year(year):
    if(year%400==0):
        return 1
    elif(year%4==0 and year%100!=0):
        return 1
    else:
        return 0
    

year=int(input("Enter the year"))
a=leap_year(year)
a

#3
list1=[31,28,31,30,31,30,31,31,30,31,30,31]
month=int(input("enter the month"))
print("number of days are",list1[month])

##vowels finder
state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
vowel='aeiouAEIOU'
state_name1=[]
for item in state_name:
    x=[]
    for i in item:
        if i not in vowel:
            x.append(i)
    str=''
    item=str.join(x)
    state_name1.append(item)
print(state_name1)

##pattern builder
num=int(input("Enter the number of rows"))
for i in range(num+1):
    for j in range(i):
        print("*",end=' ')
    print()
for i in range(num-1,0,-1):
    for j in range(i):
        print("*",end=' ')
    print()
    
##pallindromic integer
lst1=input("Enter bspace seprated number>").split()
for i in lst1:
    if int(i)>0:
        a=i
        pal=0
        pal=a[::-1]
        if pal==i:
            print("TRUE")
            break

#pangram
string1=input("enter the sentence: ")
alpha='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
beta=[]
count=0
for i in string1:
    if (i in alpha) and (i not in beta):
        beta.append(i)
        count=count+1
    if count==26:
        print('PANGRAM')
        break
if count!=26:
    print('NOT PANGRAM')
    
#bricks
num=input("enter the info.: ").split(',')
a=int(int(num[2])%5)
b=int(int(num[2])/5)
if a<= int(num[0]) and b<=int(num[1]):
    print("TRUE")
else:
    print("False")
    
#reverse
def reverse(string3):
    list3=[]
    list4=[]
    for i in string3:
        list3.append(i)
    for i in list3:
        list4.insert(0,i)
    str=''
    string3=str.join(list4)
    return string3
string2=input("enter the string: ")
string3=reverse(string2)
print(string3)



#translate
def translate(string5):
    consonent='bcdfghjklmnpqrstvwyyz'
    list5=[]
    list6=[]
    for i in string5:
        list5.append(i)
    for i in list5:
        if i in consonent:
            list6.append(i)
            list6.append('0')
            list6.append(i)
        else:
            list6.append(i)
    str=''
    string5=str.join(list6)
    return string5

string4=input("enter the string: ")
string5=translate(string4)
print(string5)


#
def Add(num):
    sum=0
    for i in num:
        sum=sum+int(i);
    return sum
def mul(num):
    mul=1
    for i in num:
        mul=mul*int(i)
    return mul
def largest(num):
    lar=0
    for i in num:
        if lar<int(i):
            lar=int(i)
    return lar
def smallest(num):
    sma=100000000
    for i in num:
        if sma>int(i):
            sma=int(i)
    return sma

num=input("enter the info.: ").split(',')
print(Add(num))
print(mul(num))
print(largest(num))
print(smallest(num))


#unlucky
user_input = input("Enter comma seperated nos >").split(",")

previous_number_is_13 = False
total = 0

for number in user_input:
    if int(number) == 13:
        previous_number_is_13 = True
    
    elif not previous_number_is_13:
        total += int(number)
    
    elif previous_number_is_13 and int(number) != 13:
        previous_number_is_13 = False

print (total)


#sorting
student_list = []

while True:
    user_input = input("Enter name, age and score: ")
    
    if not user_input:
        break
    
    name, age, marks = user_input.split(",")
    
    student_list.append( (name, int(age), int(marks) ) )

student_list.sort()
print (student_list)
