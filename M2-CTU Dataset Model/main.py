print("\n********Importing to main.py ...**********")
from pre import Xtrain,Xtest,Ytrain,Ytest,np
from sklearn.metrics import accuracy_score
from matplotlib import pyplot as plt
print("\n\n\tRunning main.py\n")

Ytrain=np.ravel(Ytrain)
Ytest=np.ravel(Ytest)
#Training
print("\n\tRunning Logistic Regression . . . \n")
from sklearn.linear_model import LogisticRegression
model1=LogisticRegression(solver='lbfgs',max_iter=10000)
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
print("Number of mislabeled points out of a total %d points : %d"%(Xtrain.shape[0],(prediction3 != Ytest).sum()))
print("Accuracy Score MODEL 3 is : ",accuracy_score(prediction3,Ytest))


#Training
print("\n\tRunning Gaussian Naive Bayes . . . \n")
from sklearn.naive_bayes import GaussianNB
model4=GaussianNB()
model4.fit(Xtrain,Ytrain)
prediction4=model4.predict(Xtest)
#print(model4.score(Xtest,Ytest)*100)
#print("Accuracy Score MODEL 4 is : ",accuracy_score(prediction4,Ytest))
print("Number of mislabeled points out of a total %d points : %d"%(Xtrain.shape[0],(prediction4 != Ytest).sum()))


#Training
print("\n\tRunning KNN Classifier . . .\n")
from sklearn.neighbors import KNeighborsClassifier
model5=KNeighborsClassifier()
model5.fit(Xtrain,Ytrain)
prediction5=model5.predict(Xtest)
print(model5.score(Xtest,Ytest)*100)
print("Accuracy Score MODEL 4 is : ",accuracy_score(prediction5,Ytest))

'''######  TAKES A LOT OF TIME  ###
#Training
print("\n\tRunning Neural Network Model . . .\n")
from keras.models import Sequential
from keras.layers import Dense,Activation
from keras.optimizers import SGD
model6=Sequential()
model6.add(Dense(10, input_dim=114, activation="sigmoid"))
model6.add(Dense(10, activation='sigmoid'))
model6.add(Dense(1))
sgd = SGD(lr=0.01, decay=0.000001, momentum=0.9, nesterov=True) 
model6.compile(optimizer=sgd, loss='mse')
model6.fit(Xtrain,Ytrain,batch_size=100,verbose=0)
score=model6.evaluate(Xtest,Ytest,verbose=0)
print("Accuracy Score MODEL 4 is : ",score*100)
'''


Ytest_p=Ytest[:100]
prediction1_p=prediction1[:100]
plt.xlabel('X(Time->)')
plt.ylabel('0 For Clean Traffic(LOW) and Threat Traffic as 1(HIGH)')
plt.plot(Ytest_p,c='b',label="Test Data")
plt.plot(prediction1_p,c='r',label="Predicted Attack")
plt.legend(loc='upper left')
plt.show()




