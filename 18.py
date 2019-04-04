
#import the python libraries
import pandas as pd
import sklearn
import nltk
import re
import numpy as np


#Read the data
import pandas as pd
from sklearn.model_selection import train_test_split
data1 = pd.read_csv('tweets.csv', header=0)
data1.head(10)


#Divide the data into training and test sets
y = data1.id
X = data1.drop('id', axis=1)


X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2)
print("X_train:\n")
print(X_train.head())
print(X_train.shape)

print("\nX_test:\n")
print(X_test.head())
print(X_test.shape)


X_train.head(2)



#Remove the twitter handles
combi = X_train.append(X_test, ignore_index=True)


def remove_pattern(input_txt, pattern):
    r = re.findall(pattern, input_txt)
    for i in r:
        input_txt = re.sub(i, '', input_txt)
        
    return input_txt    


import numpy as np
combi['tidy_tweet'] = np.vectorize(remove_pattern)(combi['tweet'], "@[\w]*")


#Remove Punctuation, Numbers and Special Character
combi['tidy_tweet'] = combi['tidy_tweet'].str.replace("[^a-zA-Z#]", " ")

#Remove words of length less than or equal to three
combi['tidy_tweet'] = combi['tidy_tweet'].apply(lambda x: ' '.join([w for w in x.split() if len(w)>3]))


combi.head(100)


#Tokenize the words
tokenized_tweet = combi['tidy_tweet'].apply(lambda x: x.split())
tokenized_tweet.head()



#Process Word Stemming
from nltk.stem.porter import *
stemmer = PorterStemmer()

tokenized_tweet = tokenized_tweet.apply(lambda x: [stemmer.stem(i) for i in x]) # stemming
tokenized_tweet.head()



for i in range(len(tokenized_tweet)):
    tokenized_tweet[i] = ' '.join(tokenized_tweet[i])

combi['tidy_tweet'] = tokenized_tweet


print(combi['tidy_tweet'])

