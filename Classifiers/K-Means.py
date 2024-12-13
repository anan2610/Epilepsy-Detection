import pandas as pd
import numpy as np

datasets = 'Features_P1.xlsx'

dataset = pd.read_excel(datasets, header=None)


# attributes
X = dataset.iloc[1:80, 0:76] #19x4 features 

y = dataset.iloc[1:80, 76]


# Import train_test_split function
from sklearn.model_selection import train_test_split

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)


# Scaling to bring values to the same range

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#Import knearest neighbors Classifier model
from sklearn.cluster import KMeans

#Create KNN Classifier
kmeans = KMeans(n_clusters=2)

#Train the model using the training sets
kmeans.fit(X_train)

#Predict the response for test dataset
y_pred = kmeans.predict(X_test)

#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics

# Model Accuracy, how often is the classifier correct?

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))