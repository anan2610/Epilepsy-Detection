import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import RandomForestRegressor
from sklearn import metrics


datasets = 'Features_P1.xlsx'

dataset = pd.read_excel(datasets, header=None)

feature_names = dataset.iloc[0,0:76]
# attributes
X = dataset.iloc[1:80, 0:76]

# label(result)
y = dataset.iloc[1:80, 76]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0) 

# Scaling to bring values to the same range

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Training

regressor = RandomForestRegressor(n_estimators=50, random_state=0) # n_estimators is the no. of trees
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

regressor = RandomForestRegressor(n_estimators=50, random_state=0) # n_estimators is the no. of trees
regressor.fit(X_train, y_train)

#Predict from test data
y_pred = regressor.predict(X_test)

#Accuracy
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

#Precision
print("Precision:",metrics.precision_score(y_test, y_pred))