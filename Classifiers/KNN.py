import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import KNeighborsClassifier
from sklearn import metrics

datasets = 'Features_P1.xlsx'

dataset = pd.read_excel(datasets, header=None)


# attributes
X = dataset.iloc[1:80, 0:380] 
#print(X)
# label(result)
y = dataset.iloc[1:80, 380] #target

# Split dataset into training set and test set

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)


# Scaling to bring values to the same range

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

knn = KNeighborsClassifier(n_neighbors=5)

#Train the model

knn.fit(X_train, y_train)

#Predict from test data

y_pred = knn.predict(X_test)

# Model Accuracy

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

#Precision
print("Precision:",metrics.precision_score(y_test, y_pred))