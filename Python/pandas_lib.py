#Pandas
#High-performance, easy-to-use data structures and data analysis tools
#Works with numpy, matplotlib.
#Provides fast data processing with flexible data manipulation as relational databases
#and spreadsheets

#Series are one dimensional arrays that store various data types
#Rows called index.
#Any list,tuple,dictionary can be converted to list

#Dataframe are 2d series.
#Has 2 indexes column-index and row-index

#Series
import pandas as pd
h=('AA','2012-02-01',100,10.2) #Tuple
s=pd.Series(h) #Converted to a string
print(s)
print()
d={'name':'metan','date':'2021-10-08','shares':100,'price':10.2}
ds=pd.Series(d)#Converted
print(ds)
print()
#Tuple to list conversion indexes are 0,1,2,3.
#We can provide custom index names

f=['façabok','2001-08-02',90,3.2]
f=pd.Series(f,index=['name','date','shares','price']) #indexes changed
print(f)
print()

print(f['shares'])#90
print(f[0]) #façabok
print(f[['shares','price']]) #90 3.2
print()
#DataFrame
#All spreadsheets and text files are read as
#DataFrame so it is a very important data structure of pasdas.

data={'name':['metan','IBBM','GOGO'],
   'date':['2021-10-08','2012-02-10','2010-04-09'],
   'shares':[100,30,90],
   'price':[10.2,12.3,10.]}
df=pd.DataFrame(data)
print(data)
print()

#Additional columns can be added after defining a DataFrame
df['owner']='Unknown'
print(df)
print()

df.index=['one','two','three'] #Row indexes are changed
print(df)
print()

#Data can be accessed using columns and rows

print(df['shares']) #Get column
print()
print(df.loc['one']) #Get index by its name
print()
print(df.iloc[0])    #Get index by its index
print()


#DataFrame indexing exercise
import numpy as np
data=np.arange(9).reshape(3,-1)
print(data)
print()

frame=pd.DataFrame(data,index=['r1','r2','r3'],columns=['c1','c2','c3'])
print(frame)
print()

print(frame['c1'])
print()

print(frame.loc['r1'])
print()

print(frame['c1']['r1'])
print()

print(frame[['c1','c3']])
print()

print(frame.loc[['r1','r3']])
print()

print(frame.iloc[:2]) #2 is not included
print()


#Access all rows for a column
print(df.loc[:,"name"])
print()

print(df.iloc[:,0])
print()

#Any column can be deleted using del or drop commands
del df['owner'] #WORKS
print(df)
print()

df.drop('shares',axis=1) #DOES NOT WORK?? Check later
print(df)
print()


#Reading Files
titles=pd.read_csv('',index_col=None,encoding='utf-8')
