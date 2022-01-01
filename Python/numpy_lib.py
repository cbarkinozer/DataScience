#NUMPY
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
