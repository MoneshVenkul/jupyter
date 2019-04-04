from pandas import read_csv
import numpy
#Import the dataset
dataset = read_csv("train.csv", header=None)
# Problem 1
#print(dataset.describe())
# Problem 2
print((dataset[[1,2,3,4,5,6,7,8]]==0).sum())
#Problem 3
dataset[[1,2,3,4,5]] = dataset[[1,2,3,4,5]].replace(0, numpy.NaN)
print(dataset.isnull().sum())
print(dataset.head(20))
#Problem 4
dataset.dropna(inplace=True)
print(dataset.head(20))
print(dataset.describe)
print(dataset.shape)
#Problem 5
dataset.fillna(dataset.mean(), inplace=True)
print(dataset.isnull().sum())
print(dataset.head(20))
#Problem 6
X = dataset.iloc[:,:-1] # Retrieves all the columns except the last column
Y = dataset.iloc[:, -1] # Retrieves only the last column
print(X)
print(Y)
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)
print(X_test)
