'''Q1. (Create a program that fulfills the following specification.)
deliveryfleet.csv


Import deliveryfleet.csv file

Here we need Two driver features: mean distance driven per day (Distance_feature) and the mean percentage of time a driver was >5 mph over 
the speed limit (speeding_feature).

    1. Perform K-means clustering to distinguish urban drivers and rural drivers.
    2. Perform K-means clustering again to further distinguish speeding drivers from those who follow speed limits, in addition to 
    the rural vs. urban division.
    Label accordingly for the 4 groups.
'''
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('deliveryfleet.csv')
features = dataset.iloc[:, [1, 2]].values

plt.scatter(features[:,0], features[:,1])
plt.show()

from sklearn.cluster import KMeans

#1
kmeans = KMeans(n_clusters = 2, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features)

plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'Urban')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'Rural')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('Clusters of datapoints')
plt.xlabel('Distance')
plt.ylabel('Speed')
plt.legend()
plt.show()

#2
kmeans = KMeans(n_clusters = 4, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features)

plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'Rural follow')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'Urban follow')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1], c = 'green', label = 'Rural unfollow')
plt.scatter(features[pred_cluster == 3, 0], features[pred_cluster == 3, 1], c = 'pink', label = 'Urban unfollow')

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('Clusters of datapoints')
plt.xlabel('Distance')
plt.ylabel('Speed')
plt.legend()
plt.show()



'''
Q2. (Create a program that fulfills the following specification.)
tshirts.csv


T-Shirt Factory:

You own a clothing factory. You know how to make a T-shirt given the height and weight of a customer.

You want to standardize the production on three sizes: small, medium, and large. How would you figure out the actual size of these 3 types 
of shirt to better fit your customers?

Import the tshirts.csv file and perform Clustering on it to make sense out of the data as stated above.

'''
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('tshirts.csv')
features = dataset.iloc[:, [1, 2]].values

plt.scatter(features[:,0], features[:,1])
plt.show()

from sklearn.cluster import KMeans

#1
kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features)

plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'Medium')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'Large')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1], c = 'green', label = 'Small')

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('Clusters of datapoints')
plt.xlabel('height')
plt.ylabel('weight')
plt.legend()
plt.show()

print("For Small : \n  Height => ",kmeans.cluster_centers_[0,0],"\n  Weight => ",kmeans.cluster_centers_[0,1])
print("For Medium : \n  Height => ",kmeans.cluster_centers_[1,0],"\n  Weight => ",kmeans.cluster_centers_[1,1])
print("For Large : \n  Height => ",kmeans.cluster_centers_[2,0],"\n  Weight => ",kmeans.cluster_centers_[2,1])




'''
Q3. This is a pre-crawled dataset, taken as subset of a bigger dataset 
 (more than 4.7 million job listings) that was created by extracting data 
 from Monster.com, a leading job board.
 
 
 
 Remove location from Organization column?
 Remove organization from Location column?
 
 In Location column, instead of city name, zip code is given, deal with it?
 
 Seperate the salary column on hourly and yearly basis and after modification
 salary should not be in range form , handle the ranges with their average
 
 Which organization has highest, lowest, and average salary?
 
 which Sector has how many jobs?
 Which organization has how many jobs
 Which Location has how many jobs?
 '''
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('monster_com-job_sample.csv')

dataset["location"].split(",")

df=dataset.drop(columns=["country","country_code"])

