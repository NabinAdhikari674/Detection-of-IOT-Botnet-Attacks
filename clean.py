print("\nImporting Packages...##",end=" ")
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
print("IMPORT DONE.\n")

print("Reading Data...##",end=" ")
cdata=pd.read_csv("Data/SimpleHome_XCS7_1003_WHT-Security_Camera/benign_traffic.csv")
scan=pd.read_csv("Data/SimpleHome_XCS7_1003_WHT-Security_Camera/mirai_attacks/udpplain.csv")
print("Read SucessFull.\n")

print(cdata)
print(scan)

#checking the dimensions
print("Cdata SHape: ",cdata.shape)
#print(cdata.head())
print("Scan Shape : ",scan.shape)

#Marking as 0/1
scan['Out']=1
cdata['Out']=0

#combining two DataFrames
comb=pd.concat([cdata,scan],axis=0)
print("The COMBINED shape : ",comb.shape)

Output=comb['Out']
comb=comb.drop(['Out'],axis=1)
#comb=comb.drop(['HpHp_L0.01_pcc'],axis=1)
comb=comb.iloc[:,:28]
Output=np.array(Output).flatten()
#print("After remove: ",comb_n.shape)
print("\nThe OUTPUt is : \n",Output)
print("\nSHAPE : ",Output.shape)

#Standardization
comb_std=(comb-(comb.mean()))/(comb.std())
comb_std_arra=np.array(comb_std)

#Normalization
comb_norm=(comb-(comb.min()))/((comb.max())-comb.min())
comb_norm_arra=np.array(comb_norm)

print("After Norm : ",comb_norm_arra.shape)


#Testing/Training Data
Xtrain,Xtest,Ytrain,Ytest=train_test_split(comb,Output,test_size=0.3,random_state=1)##########################



#import msvcrt
#print("\n\n\tCHooSE 1)ENTER   or 2)EXIT(0)",end=" ")
#choose = msvcrt.getch()
#choose=input()
#if(choose==0):
#    exit();




