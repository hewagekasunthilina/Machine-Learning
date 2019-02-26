from sklearn import datasets #importing sckit learn datasets (toy dataset)

iris=datasets.load_iris() #importing the iris data set(table)
data=iris.data #spliting the data
target=iris.target  #spliting the targets

import numpy as np

test_smpls=[0,46,121]

train_data=np.delete(data,test_smpls,axis=0)
train_target=np.delete(target,test_smpls)

from sklearn import neighbors

clsfr=neighbors.KNeighborsClassifier() #loading the classifier
clsfr.fit(train_data,train_target)  #training the classifier

test_data=data[test_smpls]

results=clsfr.predict(test_data)

print("Predicted results :",results)

test_target=target[test_smpls]

print("Actual results :",test_target)

