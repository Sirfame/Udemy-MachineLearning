print("helo world")
#importing the dataset

dataset = read.csv('Data.csv')

#Taking care of missing data
dataset$Age = ifelse(is.na(dataset$Age),
                     ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)),
                     dataset$Age)
#taking column age of the data set

dataset$Salary = ifelse(is.na(dataset$Salary),
                     ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)),
                     dataset$Salary)


# Encoding categorical data
# Factor function will transform categorical values into numeric categories, but it will see the variables as factors.
dataset$Country = factor(dataset$Country,
                         levels = c('France', 'Spain', 'Germany'), #c creates a vector
                         labels = c(1, 2, 3))

dataset$Purchased = factor(dataset$Purchased,
                         levels = c('No', 'Yes'), #c creates a vector
                         labels = c(0, 1))


# Splitting the dataset into the Training set and Test set
#10:45
