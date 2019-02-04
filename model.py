'''
Developer: Naveen Kambham
This file contains the machine learning models to predict the type of Irises based on two features
'''
import pandas
from sklearn import svm
from sklearn.externals import joblib
from sklearn import datasets

#Loading the data set

iris = datasets.load_iris()
X= iris.data[:,:2] # Two features only
y= iris.target


#Creating and fitting the SVC model
clf = svm.SVC(C=0.01,gamma=0.01)
clf = clf.fit(X,y)   # Need to fit the model otherwise the model throws the error to fit the model first before using it for prediction


#Dumping the trained model to use from Web API
joblib.dump(clf,'model.pkl')
print('Model Dumped')


