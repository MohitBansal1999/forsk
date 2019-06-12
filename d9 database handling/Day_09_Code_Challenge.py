
"""

Code Challenge 1
Write a python code to insert records to a mongo/sqlite/MySQL database 
named db_University for 10 students with fields like 
Student_Name, Student_Age, Student_Roll_no, Student_Branch."""

import os
import sqlite3
from pandas import DataFrame

conn = sqlite3.connect ( 'db_University.db' )
c = conn.cursor()
c.execute ("""CREATE TABLE student(
          Student_Name  TEXT,
          Student_Age INTEGER,
          Student_Roll_no INTEGER,
          Student_Branch TEXT
          )""")
c.execute("INSERT INTO student VALUES ('Mohit',20, 1, 'ce')")
c.execute("INSERT INTO student VALUES ('Tarun',21, 2,'cse')")
c.execute("INSERT INTO student VALUES ('Karan',19, 3, 'me')")
c.execute("INSERT INTO student VALUES ('Tushar',54, 4, 'it')")
c.execute("INSERT INTO student VALUES ('Kunal',36, 5, 'cse')")
c.execute("INSERT INTO student VALUES ('Jay',25, 6, 'ee')")
c.execute("INSERT INTO student VALUES ('Vipin',45, 7, 'ce')")
c.execute("INSERT INTO student VALUES ('Rahul',36, 8, 'me')")
c.execute("INSERT INTO student VALUES ('Sandeep',48, 9, 'ece')")
c.execute("INSERT INTO student VALUES ('Swati',30, 10, 'cse')")

c.execute("SELECT * FROM student")

print ( c.fetchone()) 
print ( c.fetchmany(2)) 
print ( c.fetchall() )
c.execute("SELECT * FROM student")
df = DataFrame(c.fetchall()) #creating dataframe
df.columns = ["Name","Age","Roll_no","Branch"] 
conn.commit()
conn.close()

"""
Code Challenge 2
Perform similar steps as in the above code challenge but store the contents in 
an online mongo atlas database.
"""
import pymongo
client = pymongo.MongoClient("mongodb://mohitforsk:mohitforsk@cluster0-shard-00-00-uokc1.gcp.mongodb.net:27017,cluster0-shard-00-01-uokc1.gcp.mongodb.net:27017,cluster0-shard-00-02-uokc1.gcp.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")

mydb = client.forsk_database

def add_student(name,age,roll,branch):
    #unique_employee = mydb.employees.find_one({"id":idd})
    #if unique_employee:
    #    return "Employee already exists"
    #else:
    mydb.forsk_collection.insert_one(
            {
            "Name" : name,
            "Age" : age,
            "Roll_no" : roll,
            "Branch" : branch
            })
    return "Student added successfully"

def fetch_all_student():
    user = mydb.forsk_collection.find()
    for i in user:
        print (i)
add_student('Mohit',20, 1, 'ce')
add_student('Tarun',21, 2,'cse')
add_student('Karan',19, 3, 'me')
add_student('Tushar',54, 4, 'it')
add_student('Kunal',36, 5, 'cse')
add_student('Jay',25, 6, 'ee')
add_student('Vipin',45, 7, 'ce')
add_student('Rahul',36, 8, 'me')
add_student('Sandeep',48, 9, 'ece')
add_student('Swati',30, 10, 'cse')

fetch_all_student()

"""
Code Challenge 3
In the Bid plus Code Challenege 

          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)

Store the information into a database mySQL Database"""

import mysql.connector 
conn = mysql.connector.connect(user='mohitforsk', password='mohitforsk',
                              host='db4free.net', database = 'forsk_database')
c = conn.cursor()
c.execute ("""CREATE TABLE BID(
          BID_no INTEGER,
          items  INTEGER,
          Quantity_required INTEGER,
          Department_Name TEXT,
          Department_Address TEXT,
          Start_date DATE,
          Start_time TIME,
          End_date DATE,
          End_time TIME
          )""")
def add_bid(BID_no,items,Quantity_required,Department_Name,Department_Address,Start_date,Start_time,End_date, End_time):
    
    c.execute("INSERT INTO BID VALUES ({},{},{}, '{}','{}','{}','{}','{}','{}')".format(BID_no,items,Quantity_required,Department_Name,Department_Address,Start_date,Start_time,End_date, End_time))
    return "Bid added successfully"
add_bid(1,20,21,"sdjdbvd",'gerg','1999-12-12','113021','2008-12-12','113021')
c.execute("SELECT * FROM BID")

print ( c.fetchone()) 
print ( c.fetchmany(2)) 
print ( c.fetchall() )

c.execute("SELECT * FROM BID")

df = DataFrame(c.fetchall())  # putting the result into Dataframe
df.columns = ["BID_no","items","Quantity_required","Department_Name","Department_Address","Start_date","Start_time","End_date"," End_time"]




"""
Code Challenge 4

Scrap the data from the URL below and store in sqlite database

https://www.icc-cricket.com/rankings/mens/team-rankings/odi """

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

import os
import sqlite3
from pandas import DataFrame

conn = sqlite3.connect ( 'team_ranking.db' )
c = conn.cursor()
c.execute("DROP TABLE rank")
c.execute ("""CREATE TABLE rank(
          Team_Name  TEXT,
          Weighted_matches INTEGER,
          Points INTEGER,
          Rating INTEGER
          )""")
def add_team(team,match,points,rating):
    
    c.execute("INSERT INTO rank VALUES (?,?,?,?)",(team,match,points,rating))
    return "team added successfully"
for i in range(len(A)):
    add_team(A[i],B[i],C[i],D[i])

c.execute("SELECT * FROM rank")

print ( c.fetchone()) 
print ( c.fetchmany(2)) 
print ( c.fetchall() )
c.execute("SELECT * FROM rank")
df = DataFrame(c.fetchall()) #creating dataframe
df.columns = ["team","match","points","rating"] 
conn.commit()
conn.close()