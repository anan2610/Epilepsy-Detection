import pandas as pd
import numpy as np

datasets = 'Features_P1.xlsx'

dataset = pd.read_excel(datasets, header=None)

X = dataset.iloc[1:80, 0:76]

y = dataset.iloc[1:80, 76]


# split X and y into training and testing sets
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=None)

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# import the class
from sklearn.linear_model import LogisticRegression

# instantiate the model (using the default parameters)
logreg = LogisticRegression()

# fit the model with data
logreg.fit(X_train,y_train)

#
y_pred=logreg.predict(X_test)


# import the metrics class
from sklearn import metrics

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logreg.score(X_test, y_test)))