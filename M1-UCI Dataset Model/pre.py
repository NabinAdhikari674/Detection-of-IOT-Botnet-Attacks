print("\nImporting Packages...##",end=" ")
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.utils import shuffle
print("IMPORT DONE.\n")

print("Reading Data...##",end=" ")
cdata=pd.read_csv("../Data/benign_traffic.csv")
scan=pd.read_csv("../Data/scan.csv")
print("Read SucessFull.\n")

print(cdata)
print(scan)

#checking the dimensions
print("Cdata SHape: ",cdata.shape)
#print(cdata.head())
print("Scan Shape : ",scan.shape)

#Tagging Clean Traffic as 0 and Threat Traffic as 1
scan['Out']=1
cdata['Out']=0

#combining two DataFrames
comb=pd.concat([cdata,scan],axis=0)
print("The COMBINED shape : ",comb.shape)
comb=shuffle(comb)
Output=comb['Out']
comb=comb.drop(['Out'],axis=1)
comb=comb.drop(['HpHp_L0.01_pcc'],axis=1)
comb1=comb.iloc[:,:28] # Removing all the Outlier Columns

#Output.to_csv('Output.csv')

Output=np.array(Output).flatten()
print("After remove: ",comb.shape)
print("\nThe OUTPUt is : \n",Output)
print("\nOutput SHAPE : ",Output.shape)

#Standardization
comb_std=(comb-(comb.mean()))/(comb.std())
comb_std_arra=np.array(comb_std)

#Using SKLearn
scale=StandardScaler()
scale.fit(comb1)
scale.transform(comb1)
#comb1.to_csv('comb1.csv')

#Normalization
comb_norm=(comb-(comb.min()))/((comb.max())-comb.min())
#comb_norm_arra=np.array(comb_norm)

#print("After Norm : ",comb_norm_arra.shape)


#Testing/Training Data
Xtrain,Xtest,Ytrain,Ytest=train_test_split(comb1,Output,test_size=0.3,random_state=1)##########################




