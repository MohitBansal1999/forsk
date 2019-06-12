# -*- coding: utf-8 -*-
"""
Created on Tue May 14 09:15:44 2019

@author: Mohit Bansal
"""
#21 faculty
[{
	"Name": {
		"fname": "Mohit",
		"lname": "Bansal"
	},
	"Photo": "https://haha.jpg",
	"Department": "Computer Science",
	"Research_areas": ["AI", "ML", "Quantum science"],
	"Contact detail": {
		"Phone number": [9887580149, 8503077209],
		"Email": "mohitbansalmb99@gmail.com"
	}
}, {
	"Name": {
		"fname": "Tarun",
		"lname": "Bansal"
	},
	"Photo": "https://haha1.jpg",
	"Department": "Mechanical",
	"Research areas": ["Fluid science", "Quantum science"],
	"Contact detail": {
		"Phone number": [9855860149, 85558077209],
		"Email": "mohitbsjbhcmb99@gmail.com"
	}
}]

#1 student
{
	"Name": {
		"fname": "Mohit",
		"lname": "Bansal"
	},
	"Photo": "https://haha.jpg",
    "clg_id" : "16kjbfsd27",
    "Address" : "gandhi ngar,jaipur",
	"Department": "civil",
	"Intrested_areas": ["AI", "ML", "Quantum science"],
	"Contact detail": {
		"Phone number": [9999999999, 8888899999],
		"Email": "ndjdjhjsosj@gmail.com"
	}
}
    
    
#2
import requests
import json
city=input("enter city name : ")
url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q="
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"
url = url1 + url2 + city + url3
response = requests.get(url)
jsondata = response.json()
print("longitude : " , jsondata['coord']['lon'])
print("lattitude : " , jsondata['coord']['lat'])
print("weather condition : " , jsondata['weather'][0]['main'])
print("wind speed : ",jsondata['wind']['speed'])
print("sunrise : ",jsondata['sys']['sunrise'])
print("sunset : ",jsondata['sys']['sunset'])

#3
url1="https://free.currconv.com/api/v7/convert?q=USD_INR,INR_USD&compact=ultra&apiKey="
url2="fec1bb86c314ba121f1b"
url=url1+url2
response = requests.get(url)
jsondata = response.json()
print("USD to INR : ",jsondata["USD_INR"])
print("INR to USD : ",jsondata["INR_USD"])


#4
import json
import requests
Host = "https://en2lrgwf101pq.x.pipedream.net"
data = {
	"Name": {
		"fname": "Mohit",
		"lname": "Bansal"
	},
	"Photo": "https://haha.jpg",
    "clg_id" : "16kjbfsd27",
    "Address" : "gandhi ngar,jaipur",
	"Department": "civil",
	"Intrested_areas": ["AI", "ML", "Quantum science"],
	"Contact detail": {
		"Phone number": [9999999999, 8888899999],
		"Email": "ndjdjhjsosj@gmail.com"
	}
}
headers = {"Content-Type":"application/json","Content-Length":len(data),"data":json.dumps(data)}
response = requests.post(Host,data,headers)
print(response.json())



#5
import json
import requests
data={"Phone" : "9999999999",
      "Name" : "Mohit Bansal",
      "College" : "IIT Rurkee",
      "Branch" : "Computer Science"
      } 
url1="http://13.127.155.43/api_v0.1/sending"
headers = {"Content-Type":"application/json","Content-Length":len(data),"data":json.dumps(data)}
response = requests.post(url1,data,headers)
if(response.content):
    url2="http://13.127.155.43/api_v0.1/receiving"
    response = requests.get(url)
    jsondata = response.json()
    x=input("enter phonr number : ")
    while jsondata["Phone"]==x in jsondata:
        print(jsondata)