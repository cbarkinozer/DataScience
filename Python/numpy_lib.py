#NUMPY
#Do not name this file numpy.py because it gives error :)
import numpy as np

#Creating an 1D array
b=np.array([0,1,2,3])
print(b,len(b))
#Creating an 2D array
a=np.array([[1,2,3],[4,5,6]],dtype=np.float32)
#Printing basic properties
print(a,a.ndim,a.shape,a.dtype)
print("Returns size of the first dimension",len(a))

#Create 10 numbers (0-9)
a = np.arange(10)
#start,end,step
b = np.arange(1, 9, 2)
#Create 6 numbers (0-1)
c = np.linspace(0, 1, 6)
#Creat 5 numbers (1-5) do not take the last value
d = np.linspace(0, 1, 5, endpoint=False)
print(a,b,c,d)

#Create 3x3 matrix full of 1s
a=np.ones((3,3))
print("ones",a)

#Create 3x3 matrix full of 0s
b=np.zeros((3,3))
print("zeros",b)

#Array Creating functions create type of float default

#Make random print same thing
np.random.seed(1234)
#Create 4 random value (0-1)
a = np.random.rand(4)

#Create 4 random value (0-1) with respect to gaussian distribution
b = np.random.randn(4)
print(a,b)

#Get max value in 0th axis
#Axis 0 means in row direction (work on colums)
#Axis 1 means column direction (work on rows)

x=np.array([[5,1],
            [7,2]])
print(x.max(axis=0))
print(x.max(axis=1))

x=np.array([[1,1],[2,2]])
print(x.sum(axis=0))
print(x.sum(axis=1))

#Index slicing
x=np.arange(10)
print(x[0],x[9])
print(x[0:9:2]) #Start,end,step
print(x[:4])#Last index is not included because starts from 0
a=np.array([[0,1,2,3,4,5],
            [10,11,12,13,14,15],
            [20,21,22,23,24,25],
            [30,31,32,33,34,35],
            [40,41,42,43,44,45],
            [50,51,52,53,54,55]])
print(a[0,3:5],a[4:,4:],a[:,2],a[2::2,::2])

#You can also combine assignment and slicing
a=np.arange(10)
a[5:]=10
print(a)
b=np.arange(5)
a[5:]=b[::-1]
#At a after 5 to end copy from start to end reverse order
print(a)

#Slicing operaiton creates a view
#When modifying view the original array is modified too

print(np.may_share_memory(a,b))
b[0]=12
print(a) #a is also changed
c=a[::2].copy() #Copys to other memory

#Fancy indexing  masks and not creates views
#So does not share memory

a=np.random.randint(0,21,15)
new_a=a[a%3==0] #Extract a sub-array with mask
print(new_a)
a[a%3==0]=-1 #You can also assing new value
print(a)

#Change values at these indexes
a[[9,7]]=-100
print(a)

#Various fancy indexing applicaitons
a=np.array([[0,1,2,3,4,5],
            [10,11,12,13,14,15],
            [20,21,22,23,24,25],
            [30,31,32,33,34,35],
            [40,41,42,43,44,45],
            [50,51,52,53,54,55]])
#These given values are python arrays
#Other multiple values in paranthesis are tuples
#Showing indexes
print(a[(0,1,2,3,4),(1,2,3,4,5)],a[3:,[0,2,5]],a[np.array([1,0,1,0,0,1],dtype=bool),2])

#Elementwise operations
a=np.array([1,2,3,4])
print(a+1,2**a)
b=np.ones(4)+ 1
print(a-b,a*b)

#These operaitons are much faster than python implementaitons
#Warning: array multiplicaiton is not matrix multiplicaiton

c=np.ones((3,3))
print(c*c) #array multiplicaiton
print(c.dot(c)) #matrix multiplcaiton

#Comparison
print(a==b,a>b,np.array_equal(a,b))
#Logical operators
print(np.logical_or(a,b),np.logical_and(a,b))
print(np.sin(a),np.log(a),np.exp(a))

#To be able to do artihmetic operaitons shapes must match

#Reductions
x=np.array([1,3,2])
#arg values gives index of the value
print(x.min(),x.max(),x.argmin(),x.argmax())
#You can use arg methods to get index and use it as a mask
print(x[x.argmax()])

#Logical operations can be used for array comparisons
a=np.zeros((100,100))
print(np.any(a!=0))
print(np.all(a==a))

#Statistic methods
x=np.array([1,2,3,1])
y=np.array([[1,2,3],[5,6,1]])
print(x.mean(),np.median(x),x.std(),np.median(y,axis=-1))#last axist)


#Broadcasting
#Basic operaitons in numpy are element-wise these works on arrays of the same s size
#It’s also possible to do operations on arrays of different
#sizes if NumPy can transform these arrays so that they all have the
#same size:(boradasting)


a=np.ones((4,5))
a[0]=2
print(a) #This is a bradcast of dimension 0 to 1

#Adding a dimension with newaxis
a=np.array([2,0,1,8])
print(a.shape)
print(a[np.newaxis,:])
print(a.shape)
print(a[:,np.newaxis])
print(a.shape)

a=np.array([[1,2,3],[4,5,6]])
print(a.ravel()) #Flattening
print(a.T)
print(a.T.ravel())
#Reshaping is the inverse operaiton of flattening
b=a.reshape((2,3))

#Size of an array can be changed with ndarray.size
a=np.arange(4)
a.resize((8,))
print(a)

#resize is not wirking if it is referred to somewhere else
b=a
#a.resize((4,))
#error cannot resize an array that has been  referenced

a=np.array([[4,3,5],[1,2,1]])
b=np.sort(a,axis=1)
print(b)
print(a.sort(axis=1))
#Sorting with fancy indexing
a=np.array([4,3,1,2])
j=np.argsort(a)
print(a[j])

#Finding minima and maxima(a functions minimum and maximum vlaues)

a=np.array([4,3,1,2])
print(np.argmax(a),np.argmin(a))

#Rounding
b=np.round(a)
