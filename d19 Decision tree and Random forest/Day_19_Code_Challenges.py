'''
Q1. (Create a program that fulfills the following specification.)
Auto_mpg.txt

Here is the dataset about cars. The data concerns city-cycle fuel consumption in miles per gallon (MPG).

    Import the dataset Auto_mpg.txt
    Give the column names as "mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name" respectively
    Display the Car Name with highest miles per gallon value 
    Build the Decision Tree and Random Forest models and find out which of the two is more accurate in predicting the MPG value
    Find out the MPG value of a 80's model car of origin 3, weighing 2630 kgs with 6 cylinders, having acceleration around 22.2 m/s due to it's 100 horsepower engine giving it a displacement of about 215. (Give the prediction from both the models)
'''

import pandas as pd
import numpy as np

data = pd.read_csv('Auto_mpg.txt', delim_whitespace=True, header=None)
data.columns = ["mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name"]

#car with max mpg
data["car name"][data["mpg"]==np.max(data["mpg"])]


data["horsepower"]=data["horsepower"].replace('?', None)

features = data.drop(["mpg","car name"], axis=1)  
labels = data['mpg']  

from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.20)  

a=np.array([6,215,100,2630,22.2,80,3]).reshape(1,7)
#Training and making predictions
#Decision tree
from sklearn.tree import DecisionTreeRegressor  
regressor = DecisionTreeRegressor()  
regressor.fit(features_train, labels_train)

labels_pred = regressor.predict(features_test) 

regressor.predict(a) 
regressor.score(features_test,labels_test)

#random forest
from sklearn.ensemble import RandomForestRegressor

regressor = RandomForestRegressor(n_estimators=25, random_state=0)  
regressor.fit(features_train, labels_train)  
labels_pred = regressor.predict(features_test)  

regressor.predict(a) 
regressor.score(features_test,labels_test)
''''
Q1. (Create a program that fulfills the following specification.)
PastHires.csv


Here, we are building a decision tree to check if a person is hired or not based on certain predictors.

Import PastHires.csv File.

scikit-learn needs everything to be numerical for decision trees to work.

So, use any technique to map Y,N to 1,0 and levels of education to some scale of 0-2.

    Build and perform Decision tree based on the predictors and see how accurate your prediction is for a being hired.

Now use a random forest of 10 decision trees to predict employment of specific candidate profiles:

    Predict employment of a currently employed 10-year veteran, previous employers 4, went to top-tire school, having Bachelor's Degree without Internship.
    Predict employment of an unemployed 10-year veteran, ,previous employers 4, didn't went to any top-tire school, having Master's Degree with Internship.

'''
import pandas as pd
import numpy as np

data = pd.read_csv('PastHires.csv')
features = data.drop("Hired", axis=1) 
labels = data['Hired']

from sklearn.preprocessing import LabelEncoder
labelencoding=LabelEncoder()
for i in [1,3,4,5]:
    features.iloc[:, i] = labelencoding.fit_transform(features.iloc[:, i])
labels = labelencoding.fit_transform(labels)

#decision tree
from sklearn.tree import DecisionTreeClassifier  
classifier = DecisionTreeClassifier()  
classifier.fit(features, labels)

classifier.score(features,labels)

labels_pred = classifier.predict(features) 
from sklearn.metrics import confusion_matrix,accuracy_score
cm = confusion_matrix(labels, labels_pred)
print(cm)

a=np.array([10,"Y",4,"BS","Y","N"]).reshape(1,6)
for i in [1,3,4,5]:
    a[:, i] = labelencoding.fit_transform(a[:, i])
classifier.predict(a)

b=np.array([10,"N",4,"MS","N","Y"]).reshape(1,6)
for i in [1,3,4,5]:
    b[:, i] = labelencoding.fit_transform(b[:, i])
classifier.predict(b)



#random
from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(n_estimators=10, random_state=0)  
classifier.fit(features, labels)  
labels_pred = classifier.predict(features) 
classifier.score(features,labels)

from sklearn.metrics import confusion_matrix,accuracy_score
cm = confusion_matrix(labels, labels_pred)
print(cm)
a=np.array([10,"Y",4,"BS","Y","N"]).reshape(1,6)
for i in [1,3,4,5]:
    a[:, i] = labelencoding.fit_transform(a[:, i])
classifier.predict(a)

b=np.array([10,"N",4,"MS","N","Y"]).reshape(1,6)
for i in [1,3,4,5]:
    b[:, i] = labelencoding.fit_transform(b[:, i])
classifier.predict(b)

