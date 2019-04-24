print("\nImporting to main.py ...##")
from pre import Xtrain,Xtest,Ytrain,Ytest
from sklearn.metrics import accuracy_score
from matplotlib import pyplot as plt
print("\n\n\tRunning main.py\n")

#Training
print("\n\tRunning Logistic Regression . . . \n")
from sklearn.linear_model import LogisticRegression
model1=LogisticRegression(solver='lbfgs',max_iter=1000)
model1.fit(Xtrain,Ytrain)
prediction1=model1.predict(Xtest)
print(model1.score(Xtest,Ytest)*100)
print("Accuracy Score MODEL 1 is : ",accuracy_score(prediction1,Ytest))


#Training
print("\n\tRunning Preceptron . . . \n")
from sklearn.linear_model import Perceptron
model2=Perceptron(eta0=0.2,max_iter=1000,tol=1e-3,verbose=0,early_stopping = True ,validation_fraction=0.1)
model2.fit(Xtrain,Ytrain)
prediction2=model2.predict(Xtest)
print(model2.score(Xtest,Ytest)*100)
print("Accuracy Score MODEL 2 is : ",accuracy_score(prediction2,Ytest))


#Training
print("\n\tRunning DecisionTreeRegressor . . . \n")
from sklearn.tree import DecisionTreeRegressor
model3=DecisionTreeRegressor()
model3.fit(Xtrain,Ytrain)
prediction3=model3.predict(Xtest)
print(model3.score(Xtest,Ytest)*100)
#print("Accuracy Score MODEL 3 is : ",accuracy_score(prediction3,Ytest))
#Accuracy cannot be shown as this regression model

#Training
print("\n\tRunning Gaussian Naive Bayes . . . \n")
from sklearn.naive_bayes import GaussianNB
model4=GaussianNB()
model4.fit(Xtrain,Ytrain)
prediction4=model4.predict(Xtest)
print(model4.score(Xtest,Ytest)*100)
print("Accuracy Score MODEL 4 is : ",accuracy_score(prediction4,Ytest))


#Training
print("\n\tRunning KNN Classifier . . .\n")
from sklearn.neighbors import KNeighborsClassifier
model5=GaussianNB()
model5.fit(Xtrain,Ytrain)
prediction5=model5.predict(Xtest)
print(model5.score(Xtest,Ytest)*100)
print("Accuracy Score MODEL 4 is : ",accuracy_score(prediction5,Ytest))

Ytest_p=Ytest[:100]
prediction1_p=prediction1[:100]
plt.xlabel('X(Time->)')
plt.ylabel('0 For Clean Traffic(LOW) and Threat Traffic as 1(HIGH)')
plt.plot(Ytest_p,c='b',label="Test Data")
plt.plot(prediction1_p,c='r',label="Predicted Attack")
plt.legend(loc='upper left')
plt.show()

