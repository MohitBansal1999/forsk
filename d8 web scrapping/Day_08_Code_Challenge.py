

"""
Code Challenge
  Name: 
    Webscrapping ICC Cricket Page
  Filename: 
    icccricket.py
  Problem Statement:
    Write a Python code to Scrap data from ICC Ranking's 
    page and get the ranking table for ODI's (Men). 
    Create a DataFrame using pandas to store the information.
  Hint: 
    https://www.icc-cricket.com/rankings/mens/team-rankings/odi 
    
    
    #https://www.icc-cricket.com/rankings/mens/team-rankings/t20i
    #https://www.icc-cricket.com/rankings/mens/team-rankings/test
"""
from bs4 import BeautifulSoup
import requests
wiki = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
source = requests.get(wiki).text
soup = BeautifulSoup(source,"lxml")
right_table=soup.find('table')
A=[]
B=[]
C=[]
D=[]
for row in right_table.find_all('tr'):
    cells = row.find_all('td')
    if len(cells) == 5:
        A.append(cells[1].text.strip())
        B.append(cells[2].text.strip())
        C.append(cells[3].text.strip())
        D.append(cells[4].text.strip())
import pandas as pd
from collections import OrderedDict
col_name = ["Team","Weighted Matches","Points","Rating"]
col_data = OrderedDict(zip(col_name,[A,B,C,D]))
df = pd.DataFrame(col_data) 
print(df)



"""
Code Challenge:
  Name: 
    Bid Plus
  Filename: 
    bid_plus.py
  Problem Statement:
      USE SELENIUM
      Write a Python code to Scrap data and download data from given url.
      url = "https://bidplus.gem.gov.in/bidlists"
      Make list and append given data:
          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)
     Make a csv file add all data in it.
      csv Name: bid_plus.csv
"""


import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
wiki = "https://bidplus.gem.gov.in/bidlists"
driver = webdriver.Chrome("C:\\Users\\Mohit Bansal\\Desktop\\FORSK\\chromedriver_win32\\chromedriver.exe")
source=driver.get(wiki)

A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]
H=[]
a=right_data.find_all('p',class_='bid_no')
print(a)
           



source = requests.get(wiki).text
soup = BeautifulSoup(source,"lxml")

right_bid=soup.find_all("p",class_="bid_no")
for single_bid in right_bid:
    x=single_bid.find('a')
    A.append(x.text)
print(A)
     

"""
http://forsk.in/images/Forsk_logo_bw.png"

Download the image from the url above and store in your workking diretory with the same
name as the image name.

Do not hardcode the name of the image


"""

import requests

url = "http://forsk.in/images/Forsk_logo_bw.png"
response = requests.get(url)
with open("forsk-logo.png","wb") as file:
    file.write(response.content)
    
    