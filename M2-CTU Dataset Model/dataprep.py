print("######Running dataprep.py######")
print("Importing Packages...##",end=" ")
import numpy as np
import pandas as pd
from sklearn.utils import shuffle
print("IMPORT DONE.\n")
data=pd.DataFrame()
flag=0;bots=0
names=[]
try:
    print("Importing Data from File...##",end=" ")
    data=pd.read_csv('../Data/flowdata.csv')
    flag=2
    print("Read DONE.\n")
except FileNotFoundError:
    print("\n\n\t\tFile(flowdata.csv) not Found!!!")
    def choser():
        global data;global flag
        choose=str(input("\n\t\tOpen File Picker to Choose file to open?\nEnter [y/n]:   "))
        if choose=='y':
            from tkinter import Tk
            from tkinter.filedialog import askopenfilename
            root=Tk()
            ftypes = [('BinetFlow FIle',"*.binetflow"),('CSV File',"*.csv"),('Excel File',"*.xlsx"),('All Types',"*.*")]
            ttl  = "FilePicker"
            filename = askopenfilename(filetypes = ftypes,title = ttl)
            root.withdraw()
            print ("This is Chosen FilePath : ",filename)
            print("\tReading Data from Choosen File...##",end=" ")
            data=pd.read_csv(filename)
            flag=1
            print("Read DONE.\n")
        elif choose=='n':
            print("\n\t\tThere is no File to process")
            print("\n\t\tExiting...")
            exit()
        else:
            print("Wrong Choice...TRY AGAIN\n")
            choser()
    choser()
    print("Chooser DONE")
finally:
    print("Data Ready to Process")



row,col=data.shape
print("Rows and Cols : ",row,col)
for zx in data.columns: 
    #print(zx)
    names.append(zx)
print(names)    
#129832 +- 1
def labeler():
    global bots;j=0
    bots=0
    i=0
    global data
    print("Running Looop for Normal/Background(value=0) or, Botnet Attack(value=1) Label Creation...##\n",end=" ")
    for each in data.loc[:,('Label')]:
        if "Background" in each:
            data.loc[i,('Label')]=0
        elif "Normal" in each:
            data.loc[i,('Label')]=1
        elif "Botnet" in each:
            data.loc[i,('Label')]=2
            bots+=1
        i+=1
        if i==row:
            break
        j+=0.005
        if int(j)==int(np.log(row)):
            print("#",end="")
            j=-1
    print("Labeler LOOP DONE.\nBot Count : ",bots)
if flag==1:
    print("\nCreating Running Labeler Function...##",end=" ")
    labeler()
    #print("DONE.")
else:
    for each in data.loc[:,('Label')]:
        if each==1:
            bots+=1
    print("Bot Count : ",bots)
print(data.head())
#print(data['Unnamed: 0'])
try:
    print("\n\t\tDropping Some Columns with Data shape ...##\r",data.shape)
    data=data.drop(['Unnamed: 0'],axis=1)
    data=data.drop(['StartTime'],axis=1)
    data=data.drop(['sTos'],axis=1)
    data=data.drop(['dTos'],axis=1)
    data=data.drop(['State'],axis=1)
    data=data.drop(['SrcAddr'],axis=1)
    data=data.drop(['DstAddr'],axis=1)
    data=data.drop(['Proto'],axis=1)
    data=data.drop(['Dir'],axis=1)
    data=data.drop(['Dport'],axis=1)
    data=data.drop(['Sport'],axis=1)
    #data
except:
    print("\n\t\tError Raised in Dropping!!!!!")
finally:
    print("DROP DONE.")
data=shuffle(data)

print(data.head())
#print(data['Label'])
#print("Displaying Some : ")
#print(data.Label[48893])
#print(data.Label[48894])
#print(data.Label[48895])
#print("562 : ",data.Label[562])

if flag==1:
    print("It seems that You have choosen a File to load instead of default file")
    def choser1():
        print("Do you want to save the current open file for later use?")
        choose=str(input("\n\t\tOpen File Picker to Choose file to open?\nEnter [y/n]:   "))
        if choose=='y':
            print("\nSaving Data to CSV file (flowdata.csv)...##",end=" ")
            data.to_csv('flowdata.csv')
            print("TO CSV DONE.")
print("\n\nEND\n")
