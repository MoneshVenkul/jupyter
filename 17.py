

actualData = [1, 1, 0, 1, 0, 0, 1, 0, 0, 0]

predictedResult = [1, 0, 0, 1, 0, 0, 1, 1, 1, 0]


from sklearn import metrics
cnf_matrix = metrics.confusion_matrix(actualData, predictedResult)
cnf_matrix


print("Accuracy:",metrics.accuracy_score(actualData, predictedResult))
print("Precision:",metrics.precision_score(actualData, predictedResult))
print("Recall:",metrics.recall_score(actualData, predictedResult))
sensitivity1 = cnf_matrix[0,0]/(cnf_matrix[0,0]+cnf_matrix[0,1])
print('Sensitivity : ', sensitivity1 )
specificity1 = cnf_matrix[1,1]/(cnf_matrix[1,0]+cnf_matrix[1,1])
print('Specificity : ', specificity1)


total1=sum(sum(cnf_matrix))
accuracy1=(cnf_matrix[0,0]+cnf_matrix[1,1])/total1
print ('Accuracy : ', accuracy1)


from sklearn.metrics import precision_recall_fscore_support as score

predicted = [1, 0, 0, 1, 0, 0, 1, 1, 1, 0]
y_test = [1, 1, 0, 1, 0, 0, 1, 0, 0, 0]

precision, recall, fscore, support = score(y_test, predicted)

print('precision: {}'.format(precision))
print('recall: {}'.format(recall))
print('fscore: {}'.format(fscore))
print('support: {}'.format(support))

from sklearn.metrics import classification_report
print(classification_report(y_test, predicted))

import numpy as np

import matplotlib.pyplot as plt


x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])
   

n=np.size(x)
mean_x, mean_y = np.mean(x),np.mean(y)

ss_xy = np.sum(y*x - n*mean_y*mean_x)
ss_xx = np.sum(x*x - n*mean_x*mean_x)

b_1 = ss_xy / ss_xx
b_0 = mean_y - b_1*mean_x

print("Estimated coefficients:\nb_0 = {} \nb_1 = {}".format(b_0,b_1))


plt.scatter(x,y, color ="m",marker = "o" , s=30)

y_pred = b_0 + b_1 *x

plt.plot(x,y_pred,color="g")

plt.xlabel('x')
plt.xlabel('y')

plt.show()
    


Stock_Market ={ 'Year':['2017','2017','2017','2017','2017','2017','2017','2017','2017','2017','2017','2017','2016','2016','2016','2016','2016','2016','2016','2016','2016','2016','2016','2016'],

'Month': ['12','11','10','9','8','7','6','5','4','3','2','1','12','11','10','9','8','7','6','5','4','3','2','1'],

'Interest_Rate':['2.75','2.5','2.5','2.5','2.5','2.5','2.5','2.25','2.25','2.25','2','2','2','1.75','1.75','1.75','1.75','1.75','1.75','1.75','1.75','1.75','1.75','1.75'],

'Unemployment_Rate':['5.3','5.3','5.3','5.3','5.4','5.6','5.5','5.5','5.5','5.6','5.7','5.9','6','5.9','5.8','6.1','6.2','6.1','6.1','6.1','5.9','6.2','6.2','6.1'],

'Stock_Index_Price':['1464','1394','1357','1293','1256','1254','1234','1195','1159','1167','1130','1075','1047','965','943','958','971','949','884','866','876','822','704','719']        }

from pandas import DataFrame
df = DataFrame(Stock_Market,columns=['Year','Month','Interest_Rate','Unemployment_Rate','Stock_Index_Price']) 


from pandas import DataFrame 
import matplotlib.pyplot as plt

Stock_Market = {'Year': [2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016],
                'Month': [12, 11,10,9,8,7,6,5,4,3,2,1,12,11,10,9,8,7,6,5,4,3,2,1],
                'Interest_Rate': [2.75,2.5,2.5,2.5,2.5,2.5,2.5,2.25,2.25,2.25,2,2,2,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75],
                'Unemployment_Rate': [5.3,5.3,5.3,5.3,5.4,5.6,5.5,5.5,5.5,5.6,5.7,5.9,6,5.9,5.8,6.1,6.2,6.1,6.1,6.1,5.9,6.2,6.2,6.1],
                'Stock_Index_Price': [1464,1394,1357,1293,1256,1254,1234,1195,1159,1167,1130,1075,1047,965,943,958,971,949,884,866,876,822,704,719]        
                }

y=Stock_Market.get('Stock_Index_Price')
x=Stock_Market.get('Interest_Rate')
print(x)
print(y)
plt.scatter(x,y)
plt.show()


y=Stock_Market.get('Stock_Index_Price')
x=Stock_Market.get('Unemployment_Rate')
print(x)
print(y)
plt.scatter(x,y,color='green')
plt.show()


