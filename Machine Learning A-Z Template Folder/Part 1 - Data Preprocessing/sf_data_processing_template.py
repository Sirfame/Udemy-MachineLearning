# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np # library for mathematical tools
import matplotlib.pyplot as plt # sublibrary for matplotlib for plotting
import pandas as pd #import and manage data sets


#importing the data sets
dataset = pd.read_csv('Data.csv')

X = dataset.iloc[:, :-1].values 
"""
first colon is to take all the lines (since it is on the left of the first comma)
On the right of the comma, we have a colon -1, meaning we take all the columns except for the last one
.values takes all the values

"""

y = dataset.iloc[:, :3].values


# taking care of missing data.
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