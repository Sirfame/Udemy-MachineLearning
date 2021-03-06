# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np # library for mathematical tools
import matplotlib.pyplot as plt # sublibrary for matplotlib for plotting
import pandas as pd #import and manage data sets


########################################## importing the data sets ########################################################################################
dataset = pd.read_csv('Data.csv')

X = dataset.iloc[:, :-1].values 
"""
first colon is to take all the lines (since it is on the left of the first comma)
On the right of the comma, we have a colon -1, meaning we take all the columns except for the last one
.values takes all the values

"""

y = dataset.iloc[:, 3].values


########################################## taking care of missing data ############################################################################################
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
"""
the missing_values parameter will look for values that are Null, which is represented by NaN, even though the
data says nan in lowercase

Next we have to set the strategy, and in our case, we are calculating the mean.

The third parameter is either 1 or 0, 1 being the mean if the rows, and 0 being the mean of the columns.
"""

imputer = imputer.fit(X[:, 1:3]) #upper bound is excluded.

X[:, 1:3] = imputer.transform(X[:, 1:3])


############################################## Encoding categorical data ############################################################################################
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0]) # This line takes the labelencoder_X object and fits it to country
# Now this line will replace the values with the encoded values.

onehotencoder = OneHotEncoder(categorical_features = [0])

X = onehotencoder.fit_transform(X).toarray()


labelencoder_Y = LabelEncoder()
y = labelencoder_Y.fit_transform(y)

############################################## Splitting the dataset into the Training Set and Test Set ############################################################################################
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0) # test size 0.5 means half the data set is used for test.


############################################## Feature scaling ############################################################################################
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()# the reason why we specify X here is because we might need to create another StandardScaler object for the dependent variable.
X_train = sc_X.fit_transform(X_train) # for training set, we need to fit AND transform, but for our test set, we only transform the data.
X_test = sc_X.transform(X_test)