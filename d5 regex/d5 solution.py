# -*- coding: utf-8 -*-
"""
Created on Sat May 11 09:44:19 2019

@author: Mohit Bansal
"""

#1
import re
num=input('enter the string : ')
if(re.search(r'[+-]?[0-9]+[.]+',num)):
    print('true')
else:
    print('false')
    
    
    
#2
import re
mail=input('enter mails : ')
a=re.findall(r'[a-z0-9_-]+@[a-z0-9]+\.[a-z]{2,3}',mail)
a=a.sort()
print(a)


#3
import re

reg = r'^[456](\d{15}|\d{3}-(\d{4}-){2}\d{4})$'

while True:
    a = raw_input().strip()
    if not a:
        break
    chk = re.match(reg,a)
    rep = re.search(r'(\d)\1{3,}',a.replace('-',''))
    if chk and not rep:
        print "Valid"
    else:
        print "Invalid"




#4
import re
mail=input('enter mails : ')
a=re.findall(r'[a-z0-9_-]+@[a-z0-9]+\.[a-z]{2,3}',mail)
a.sort()
print(a)

#5
import re
with open('simpsons_phone_book.txt', mode='rt') as file :
   for line in file:
       if(re.search(r'^J[a-z ]+Neu',line)):
           print(line)
          