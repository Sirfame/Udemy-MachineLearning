# Data Preprocessing

# Importing the dataset
dataset = read.csv('Data.csv')
# dataset = dataset[, 2:3] Uncomment when needed to take a subset of our dataset

# Splitting the dataset into the Training set and Test set
# install.packages('caTools') (Uncomment here to install package)
library(caTools)
set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Feature scaling.
# training_set[, 2:3] = scale(training_set[, 2:3])
# test_set[, 2:3] = scale(test_set[, 2:3])