import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, datasets

#Import the data set from the predefined libraries of sklearn

iris = datasets.load_iris()

#Consider only the first two features. Reduce the data set to 2 Dimension.

X = iris.data[:, :2]
y = iris.target

#Create an instance for the SVM algorithm. Fit the data.
#Scale the data is not done. The objective is to plot the support vectors.

#SVM Regularization Parameter.
'''
Can vary the value of:
    kernel = poly / rbf
    c = [1:1000]
    gamma = [1:1000]
    
    For large values of c and gamma the performance is degraded.
'''
C = 1.0
svc = svm.SVC(kernel='linear', C=1, gamma=1).fit(X, y)

#Create a mesh to plot.
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
h = (x_max / x_min)/100
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
np.arange(y_min, y_max, h))
plt.subplot(1, 1, 1)
Z = svc.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.8)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.xlim(xx.min(), xx.max())
plt.title('Linear Kernel C = 1 and Gamma = 1')
plt.show()
