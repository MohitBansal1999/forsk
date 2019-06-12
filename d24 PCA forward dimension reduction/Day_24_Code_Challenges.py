'''
Q1. (Create a program that fulfills the following specification.)

Import Crime.csv File.

    Perform dimension reduction and group the cities using k-means based on Rape, Murder and assault predictors.
'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('crime_data.csv')
features=dataset.drop(["State","UrbanPop"],axis=1).values

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

features = sc.fit_transform(features)

# Applying PCA
from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
features = pca.fit_transform(features)

from sklearn.cluster import KMeans

'''wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 0)
    kmeans.fit(features)
    wcss.append(kmeans.inertia_)    

#Now plot it        
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()'''

kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features)

plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'low crime')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'medium crime')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1], c = 'green', label = 'high crime')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.legend()
plt.show()





'''
Q2. (Create a program that fulfills the following specification.)

The iris data set consists of 50 samples from each of three species of Iris flower (Iris setosa, Iris virginica and Iris versicolor).



    Four features were measured from each sample: the length and the width of the sepals and petals, in centimetres (iris.data).
    Import the iris dataset already in sklearn module using the following command:\


from sklearn.datasets import load_iris
iris = load_iris()
iris=iris.data


Reduce dimension from 4-d to 2-d and perform clustering to distinguish the 3 species.
'''
from sklearn.datasets import load_iris
iris = load_iris()
iris=iris.data

from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
iris = pca.fit_transform(iris)

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(iris)

plt.scatter(iris[pred_cluster == 0, 0], iris[pred_cluster == 0, 1], c = 'blue', label = 'Cluster 1')
plt.scatter(iris[pred_cluster == 1, 0], iris[pred_cluster == 1, 1], c = 'red', label = 'Cluster 2')
plt.scatter(iris[pred_cluster == 2, 0], iris[pred_cluster == 2, 1], c = 'green', label = 'Cluster 3')
plt.show()

 """
Q3.Code Challenge -
Data: "data.csv"

This data is provided by The Metropolitan Museum of Art Open Access
1. Visualize the various countries from where the artworks are coming.
2. Visualize the top 2 classification for the artworks
3. Visualize the artist interested in the artworks
4. Visualize the top 2 culture for the artworks
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset=pd.read_csv("data.csv")

#1
country=[]
number=[]
a=dataset["Country"].value_counts()
for i in a:
    country.append(a[a == i].index[0])
    number.append(i)
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue',"red",'gold', 'yellowgreen', 'lightcoral', 'lightskyblue',"red",'gold', 'yellowgreen', 'lightcoral', 'lightskyblue',"red",'gold', 'yellowgreen', 'lightcoral', 'lightskyblue',"red",'gold', 'yellowgreen', 'lightcoral', 'lightskyblue',"red",'gold', 'yellowgreen', 'lightcoral', 'lightskyblue',"red",'gold', 'yellowgreen', 'lightcoral', 'lightskyblue',"red",'gold', 'yellowgreen', 'lightcoral', 'lightskyblue',"red",'gold', 'yellowgreen', 'lightcoral', 'lightskyblue',"red",'gold', 'yellowgreen', 'lightcoral', 'lightskyblue',"red",]
explode = [i*0 for i in range(48)]  

plt.pie(number, explode=explode, labels=country, colors=colors, autopct='%1.1f%%', shadow=True, startangle=0)
plt.axis('equal') 
plt.legend()
plt.show()

#2


