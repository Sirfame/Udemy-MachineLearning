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