
'''
Q. (Create a p+--++++++rogram that fulfills the following specification.)
Female_Stats.Csv

Female Stat Students

 

Import The Female_Stats.Csv File

The Data Are From N = 214 Females In Statistics Classes At The University Of California At Davi.

Column1 = Student’s Self-Reported Height,

Column2 = Student’s Guess At Her Mother’s Height, And

Column 3 = Student’s Guess At Her Father’s Height. All Heights Are In Inches.

 

1. Build A Predictive Model And Conclude If Both Predictors (Independent Variables) Are Significant For A Students’ Height Or Not
2. When Father’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Mother’s Height.
3. When Mother’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Father’s Height.

'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("Female_Stats.csv")
features=df.iloc[:,1:]
labels=df.iloc[:,0:1]

import statsmodels.api as sm
features1=sm.add_constant(features)
#1
features_opt = features1.iloc[:, [0, 1, 2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

#2 cofficient if momheight is answer 
'''features2=features.iloc[:,1:]
features2["momheight"]=features.iloc[:,0:1]+1

from sklearn.preprocessing import PolynomialFeatures
polyObj=PolynomialFeatures(degree=10)
polyFeatures=polyObj.fit_transform(features2)

from sklearn.linear_model import LinearRegression
linearReg=LinearRegression()

linearReg.fit(polyFeatures,labels)
labels_pred=linearReg.predict(polyFeatures)
print("Before => ",np.mean(labels))
print("After => ",np.mean(labels_pred))
'''

#3 cofficient of dadheight is answer
'''
features3=features.iloc[:,:1]
features3["dadheight"]=features.iloc[:,1:]+1

from sklearn.preprocessing import PolynomialFeatures
polyObj=PolynomialFeatures(degree=50)
polyFeatures1=polyObj.fit_transform(features3)

from sklearn.linear_model import LinearRegression
linearReg=LinearRegression()

linearReg.fit(polyFeatures1,labels)
labels_pred=linearReg.predict(polyFeatures1)
print("Before => ",np.mean(labels))
print("After => ",np.mean(labels_pred))

'''
'''

Q. (Create a program that fulfills the following specification.)
bluegills.csv

How is the length of a bluegill fish related to its age?

In 1981, n = 78 bluegills were randomly sampled from Lake Mary in Minnesota. The researchers (Cook and Weisberg, 1999) measured and recorded the following data (Import bluegills.csv File)

Response variable(Dependent): length (in mm) of the fish

Potential Predictor (Independent Variable): age (in years) of the fish

    How is the length of a bluegill fish best related to its age? (Linear/Quadratic nature?)
    What is the length of a randomly selected five-year-old bluegill fish? Perform polynomial regression on the dataset.

NOTE: Observe that 80.1% of the variation in the length of bluegill fish is reduced by taking into account a quadratic function of the age of the fish.
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("bluegills.csv")
features=df.iloc[:,0:1]
labels=df.iloc[:,1]
#only linear
from sklearn.linear_model import LinearRegression
linearReg=LinearRegression()
linearReg.fit(features,labels)
plt.scatter(features, labels, color = 'red')
plt.plot(features, linearReg.predict(features), color = 'blue')
plt.show()
#with polynomial
from sklearn.preprocessing import PolynomialFeatures
polyObj=PolynomialFeatures(degree=6)
polyFeatures=polyObj.fit_transform(features)
from sklearn.linear_model import LinearRegression
linearReg=LinearRegression()
linearReg.fit(polyFeatures,labels)
plt.scatter(features, labels, color = 'red')
plt.scatter(features, linearReg.predict(polyFeatures), color = 'blue')
plt.plot(features, linearReg.predict(polyFeatures), color = 'blue')
plt.show()

a=np.array([5]).reshape(1,1)
linearReg.predict(polyObj.transform(a))






'''
Q. (Create a program that fulfills the following specification.)
iq_size.csv

Are a person's brain size and body size (Height and weight) predictive of his or her intelligence?

 

Import the iq_size.csv file

It Contains the details of 38 students, where

Column 1: The intelligence (PIQ) of students

Column 2:  The brain size (MRI) of students (given as count/10,000).

Column 3: The height (Height) of students (inches)

Column 4: The weight (Weight) of student (pounds)

    1. What is the IQ of an individual with a given brain size of 90, height of 70 inches, and weight 150 pounds ? 
    2. Build an optimal model and conclude which is more useful in predicting intelligence Height, Weight or brain size.
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("iq_size.csv")
features=df.iloc[:,1:]
labels=df.iloc[:,0:1]

#1
from sklearn.preprocessing import PolynomialFeatures
polyObj=PolynomialFeatures(degree=4)
polyFeatures=polyObj.fit_transform(features)

from sklearn.linear_model import LinearRegression
linearReg=LinearRegression()
linearReg.fit(polyFeatures,labels)
plt.scatter(features, labels, color = 'red')
plt.plot(features, linearReg.predict(polyFeatures), color = 'blue')
plt.show()

a=np.array([90,70,150]).reshape(1,3)
linearReg.predict(polyObj.transform(a))


#2
import statsmodels.api as sm
features1=sm.add_constant(features)

features_opt = features1.iloc[:, [0, 1, 2,3]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

features_opt = features1.iloc[:, [0, 1, 2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()
regressor_OLS.pvalues

from sklearn.preprocessing import PolynomialFeatures
polyObj=PolynomialFeatures(degree=4)
polyFeatures=polyObj.fit_transform(features_opt)

from sklearn.linear_model import LinearRegression
linearReg=LinearRegression()

linearReg.fit(polyFeatures,labels)


plt.scatter(features["Brain"], labels, color = 'red')
plt.plot(features["Brain"], linearReg.predict(polyFeatures), color = 'blue')
plt.show()