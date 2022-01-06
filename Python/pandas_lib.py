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
titles=pd.read_csv('C:\\Users\\barkin\\Downloads\\titles.csv',index_col=None,encoding='utf-8')
casts=pd.read_csv('C:\\Users\\barkin\\Downloads\\cast.csv',index_col=None,encoding='utf-8')
print(len(titles))
print(titles.head(3))
print()

#Selecting a row or column from DataFrame, makes it a series
print(titles.iloc[0])
print()

#Data can be filtered by providing some boolean expression in DataFrame
after85=titles[titles['year']>1985]
print(after85.head())
print()

t=titles
movies90=t[(t['year']>1990)& (t['year']<2000)]
print(movies90.head())
print()

#Sorting
#Can be performed using sort_index for index
#sort_values for selected column

t=titles
macbeth=t[t['title']=='Macbeth'].sort_index()
print(macbeth.head())
print()

macbeth=t[t['title']=='Macbeth'].sort_values('year')
print(macbeth.head())
print()

#Some data can contain not a numeric values NaN as null
print(casts.iloc[3:5]) #Note: ix is deprecated
print()

#Displaying nulls
print(casts[casts['n'].isnull()].head(3))
print()

#NaN can be fill
c_fill=casts[casts['n'].isnull()].fillna('NA')
c_fill.head(2)

t=titles
print(t[t['title']=='Maa'])
print()

#All the movies starts with Maa
print(t[t['title'].str.startswith("Maa ")].head(3))
print()
#Total number of occurrences can be counted using value_counts()
print(t['year'].value_counts().head())
print()

#Plots
#Pandas supports the matplotlib library cand can be used to plot
#the data as well
import matplotlib.pyplot as plt
t=titles
p=t['year'].value_counts()
p.plot()
#plt.show()
#The plot that is generated from above code is not useful
#We need to sort it first

p.sort_index().plot()
#plt.show()

#Groupby
#Data can be grouped by columns-headers

cg= casts.groupby(['year']).size()
cg.plot()
#plt.show()

#We can take multiple parameters for grouping
c=casts
cf=c[c['name']=='Aaron Abrams']
print(cf.groupby(['year']).size().head())
print()

#Grouping based on max ratings in a year
print(cf.groupby(['year']).n.max().head())
print()

#File operations
#Reading files
#There are 3 methods that has different reading parameters

#pd.read_csv for just reading
df=pd.read_csv('C:\\Users\\barkin\\Downloads\\titles.csv')
print(df)
print()

#pd.DataFrame.from_csv is deprecated

#pd.read_table for reading with seperation symbol defined
df=pd.read_table('C:\\Users\\barkin\\Downloads\\titles.csv',sep=',')
print(df)
print()

#If header is none, default headers will be numeric indexes
a=pd.read_csv('C:\\Users\\barkin\\Downloads\\titles.csv',header=None)
print(a)
print()

#You can specify using "names"
b= pd.read_csv('C:\\Users\\barkin\\Downloads\\titles.csv',names=['a','b','c','d','message'])
print(b)
print()

#You can specify column that has the row index
c=pd.read_csv('C:\\Users\\barkin\\Downloads\\titles.csv',names=['a','b','c','d','message'],index_col='message')
print(c)
print()


#Writing data to a file
c.to_csv('d_out.csv')
#Save without headers
c.to_csv('d_out.csv',header=False,index=False)


#EXERCISE
#Find top 10 years with the highest number of films
casts=pd.read_csv('C:\\Users\\barkin\\Downloads\\cast.csv',index_col=None,encoding='utf-8')
c=casts.groupby('year').size().sort_values(ascending=False).head(10)
print(c)
print()

#Find the top 10 characters with the highest score
c2=casts.groupby('character').mean()
print(c2['n'].sort_values(ascending=False).head(10))
print()


#Concatenating the data
s1= pd.Series([0,1],index=['a','b'])
s2=pd.Series([2,1,3],index=['c','d','e'])
s3=pd.Series([4,7],index=['a','e'])

print(s1)
print()
print(s2)
print()
print(s3)
print()

print(pd.concat([s1,s2],axis=1))
print()

#To identify different pieces of concatenate operation. We provide keys.
print(pd.concat([s1,s2,s3],keys=['one','two','three']))
print()


#Data transformation
#Removing duplicates
data={'name':['metan','IBBM','GOGO','GOGO'],
   'date':['2021-10-08','2012-02-10','2010-04-09','2010-04-09'],
   'shares':[100,30,90,90],
   'price':[10.2,12.3,10.1,10.1]}
df=pd.DataFrame(data)
print(df.duplicated())#Checking duplicates
df2=df.drop_duplicates()
print(df2) #Deleting duplicates
print()
#If there are multiple duplicates the last one also get drop you can add parameter keep="last"
#You can also drop column specific as df.drop_duplicates(['k1'])

#Replacing values
df3=df2.replace('IBBM','IMB')
print(df3)
print()

#IMB->BIM, GOGO->BOGO
df4=df3.replace(['IMB','GOGO'],['BIM','BOGO'])

print(df4)
print()

#Arguments can be passsed as dictionary as well
df4= df4.replace({'BIM':'IMB','BOGO':'BOGOS'})
print(df4)
print()

#We can groupby first something than other thing
df5=df4.groupby([df['shares'],df['price']])

#Iterating over group
#groupby supports iteration for 2 values
for shares,price in df5:
    print(shares)
    print(price)

#Data aggregation
#Data aggregations are applicable on grouped data
print()
print(df5.max())
print(df5.min())
