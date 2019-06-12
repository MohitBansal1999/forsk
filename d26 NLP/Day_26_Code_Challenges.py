'''
Q1. Code Challegene (NLP)
Dataset: amazon_cells_labelled.txt
The Data has sentences from Amazon Reviews
Each line in Data Set is tagged positive or negative
Create a Machine learning model using Natural Language Processing that can predict wheter a given review about 
the product is positive or negative
'''
import pandas as pd
dataset = pd.read_csv('amazon_cells_labelled.txt', delimiter = '\t',header=None)

import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

from nltk.stem.porter import PorterStemmer

corpus = []
for i in range(0, 1000):
    review = re.sub('[^a-zA-Z]', ' ', dataset[0][i])
    review = review.lower()
    review = review.split()
    review = [word for word in review if word=="not" or (not word in set(stopwords.words('english')))  ]
    
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review]
    review = ' '.join(review)
    corpus.append(review)

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1000)
features = cv.fit_transform(corpus).toarray()
labels = dataset.iloc[:, 1].values

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.20, random_state = 0)

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier()
classifier.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
print(confusion_matrix(labels_test, labels_pred))
print(classifier.score(features_test,labels_test))

'''
Q2. Code Challenge (Connecting Hearts)

Downlaod Link: http://openedx.forsk.in/c4x/Manipal_University/FL007/asset/Resource.zip

What influences love at first sight? (Or, at least, love in the first four minutes?) This dataset was compiled by 
Columbia Business School Professors Ray Fisman and Sheena Iyengar for their paper Gender Differences in Mate 
Selection: Evidence from a Speed Dating Experiment.

Data was gathered from participants in experimental speed dating events from 2002-2004. During the events, 
the attendees would have a four minute "first date" with every other participant of the opposite sex. 
At the end of their four minutes, participants were asked if they would like to see their date again.

They were also asked to rate their date on six attributes: Attractiveness, Sincerity, Intelligence, Fun, 
Ambition, and Shared Interests.

The dataset also includes questionnaire data gathered from participants at different points in the process.

These fields include: demographics, dating habits, self-perception across key attributes, beliefs on what 
others find valuable in a mate, and lifestyle information.

See the Key document attached for details of every column and for the survey details.


What does a person look for in a partner? (both male and female)


For example: being funny is more important for women than man in selecting a partner! Being sincere on the other 
hand is more important to men than women.

    What does a person think that their partner would look for in them? Do you think what a man thinks a woman 
    wants from them matches to what women really wants in them or vice versa. TIP: If it doesn’t then it will be one sided :)

    Plot Graphs for:
            How often do they go out (not necessarily on dates)?
            In which activities are they interested?
    
    If the partner is from the same race are they more keen to go for a date?
    What are the least desirable attributes in a male partner? Does this differ for female partners?
    How important do people think attractiveness is in potential mate selection vs. its real impact?
'''
import pandas as pd
dataset = pd.read_csv('Resource//Dating_Data.csv',encoding="windows 1252")

    
    
    