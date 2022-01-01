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

