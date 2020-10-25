#not my code
#all rights belongs to "btkakademi-python ile makine öğrenmesi" course
##Multiple lineer regression exercise
#modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_casv('C:\Users\barkin\Desktop\tennis.csv')
#data= pd.DataFrame(data=data,index=[14])

#testing the file
print(data)

from sklearn import preprocessing
data2=data.apply(preprocessing.LabelEncoder().fit_transform)
c=data2.iloc[:,:1]
ohe=preprocessing.OneHotEncoder()
c=ohe.fit_transform(c).toarray()
print(c)

havadurumu=pd.DataFrame(data=c,index=range(14),columns=['o','r','s'])
sonveriler= pd.concat([havadurumu,data.iloc[:,1:3]],axis=1)
sonveriler=pd.concat([data2.iloc[:,-2:],sonveriler],axis=1)

#Dividing data to test and train
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(sonveriler.iloc[:,:-1],sonveriler.iloc[:,-1:],test_size=0.3)
