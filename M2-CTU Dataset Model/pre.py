print("\n\t\t\t\t######Running pre.py######")
print("Importing Packages...##",end=" ")
from dataprep import data,np,shuffle
from sklearn.preprocessing import StandardScaler
#from sklearn.utils import shuffle
print("IMPORT DONE.\n")
bots=0
for each in data.loc[:,('Label')]:
    if each==1:
        bots+=1
print("Bot Count in Data: ",bots)

data=shuffle(data)
inputs=data.iloc[:,:4]
targets=data.iloc[:,4:5]
print(inputs)
scale=StandardScaler()
scale.fit(inputs)
scale.transform(inputs)
print(targets)
bots=0
for each in targets.loc[:,('Label')]:
    if each==1:
        bots+=1
print("Bot Count in Targets: ",bots)




## ## ### ##### #### #### #### ### #### # #### ### ## ### ## ## ### #### # ## ## ##
def train_test_split1(data,percent):
    print("\nRunning Train_Test_Split...\n")
    global row;
    test_size= int((percent/100)*row)
    train_size=row-test_size
    print("   The size of Training Data is : ",train_size)
    print("   The size of Test Data is     : ",test_size,)
    print("                          Total : ",(train_size+test_size))
    length=0
    rows_t=[]
    rows_s=[]
    print("\n\tRandomly Choosing Training Data...\n")
    train=pd.DataFrame(rows_t,columns=names)
    while(length<train_size):
        x1=np.random.choice(data['Sn'])
        
        if (((x1==train.Sn).any())==False):
            dict1=(data.iloc[x1-1:x1,:]).to_dict(orient='dict')
            rows_t.append(dict1)########
            length=length+1
            train=pd.DataFrame(rows_t,columns=names)
            #print(np.shape(train))
        else:
            print("",end="")
    length=0
    test=pd.DataFrame(rows_s,columns=names)
    print("\tRandomly Choosing Test Data...\n")
    while(length<test_size):
        x1=np.random.choice(data['Sn'])
        if (((x1==train.Sn).any())==False) and (((x1==test.Sn).any())==False):
             dict2=(data.iloc[x1-1:x1,:]).to_dict(orient='dict')
             rows_s.append(dict2)
             length=length+1
             test=pd.DataFrame(rows_s,columns=names)
    print("\t\tThe Training and Test Data ARE Split")
    return train,test
################################################################################ 






def choser():
    global inputs;global targets;
    choose=str(input("\n\t\tUse Built-IN Splitter(NOT READY!!) ?\nEnter [y/n]:   "))
    if choose=='y':
        print("\n##The Module is not Ready yet...")
        print("##Check the code of this module(train_test_split1) in : 'pre.py' \n")
        choser()
        percent=int(input("\n\t\tEnter the TEST size(IN PERCENTAGE) : "))
        percent=(percent/100)
        train,test=train_test_split1(data,percent)
        print("\nThe Training Data has shape :",np.shape(train))
        print("The Test Data has shape     :",np.shape(test))
        train[names]=train[names].replace({'{':''},regex=True)
        train[names]=train[names].replace({'}':''},regex=True)
        train.to_excel('hello.xlsx')
        #train[names]=train[names].replace({'':''},regex=True)
        x_train = pd.DataFrame([train.InvoiceNo,train.StockCode,train.Quantity]).transpose()
        x_test  = pd.DataFrame([test.InvoiceNo,test.StockCode,test.Quantity]).transpose()
        y_train = pd.DataFrame([train.Country]).transpose()
        y_test  = pd.DataFrame([test.Country]).transpose()
    elif choose=='n':
        percent=int(input("\n\t\tEnter the TEST size(IN PERCENTAGE) : "))
        from sklearn.model_selection import train_test_split
        print("\n\tRandomly Choosing Training and Test Data...\n")
        x_train,x_test,y_train,y_test=train_test_split(inputs,targets,test_size=percent,random_state=0)
        print("\t\tThe Training and Test Data ARE Split")
    else:
        print("Wrong Choice...TRY AGAIN\n")
        choser()
    return x_train,x_test,y_train,y_test

Xtrain,Xtest,Ytrain,Ytest=choser()

print("\n\t##Data PreProcessing Done.") 
print("\t\tExiting pre.py\n")
