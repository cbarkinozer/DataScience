#PASS
a=1
b=0
if b<a:
    pass
#empty code blocks cause error use pass

print("\n")
#INPUT
name=str(input('Enter your name: '))
#Forcing to enter string and printing while reading input

print("\n")
#DATATYPES
#boolean,integer,float,complex,none

print("\n")
b=-293929748287398273597238957298375927359
#This works but hard to operato (so don't)

print("Clasic division ",5/4)#1.25
print("Floor division ", 5//4)#1
print("Modulo(remainder) ", 5%4)
print("Power ", 5**4)
print("Floor division ", abs(-5))
print("Division with remainder ", divmod(5,4))
print("exponential notation", 4e5)#400,000

import math
x=30
print("Square root",math.sqrt(x))
print("Sinus",math.sin(x))
print("Cosinus",math.cos(x))
print("Tangent",math.tan(x))
print("Logarithmic",math.log(x))



print("\n")
print("String Representation")

s="Hello World"
print("first ",s[0],"last ",s[-1])
print(s[:5],s[-5:])
len(s)
'he' in s
s*5
str(x)

print("\n")
#File I/O

#Open for read
f=open('foo.txt','r')
#Open for write
g=open('foo.txt','w')

maxbytes=2
data=f.read(maxbytes) #Read up maxbyte data
g.write('some text')

f.close()
g.close()

f=open('foo.txt','r')
while True:
    chunk= f.read(maxbytes)
    if chunk=='':
        break
    print(chunk)
f.close()

with open('foo.txt','r') as f:
    print(f.read())



print("\n")
#Function
def sum(a,b):
    '''Sums input and returns''' #Doc String
    return a+b
print(sum(1,2))#Calling a function
#If you write no return, it will return None
#If you write return with multiple elements
#It will  return tuple

#If a function is not static it has a single parameter called self
#You do not give self as parameter but reaching the method
#By instance is the self parameter

#Global variables are variables outside a function(do not use as much as possible)
#Local variables are variables inside a function code block

print("\n")
#Reading from url
import urllib.request
with urllib.request.urlopen("http://www.python.org") as url:
    u = url.read()
    #print(u) #650 lines of html code :)

print('\n')
#Lists
names=["bark","dark","fark"]
nums=[1,2,3,5,4]

names.append('murphy')#Appends(adding at the end)
names.insert(2,'aretha')#Inserts at index

print("Concatenation of the lists",names+nums)
nums*3 #Not a mathematical operation(use numpy for that)

names.index('bark') #Returns index
names.remove('fark') #or del names[2]

for name in names:
    print(name)

nums.sort(reverse=True)
print(nums)
nums.sort()
print(nums)

print('\n')
#Tuples
#You can not modfiy tuples
#in this case t gets deleted and gets recreated
t=()#Empty tuple
print(t)
t=('Meta',)
print(t)
t=('GOOG',100,490.1)
print(t)

print(t[0])

#t[1]=75 #Tuples can't be modified

t2 = (t[0], 75, t[2]) #You can also create new one with other tuples values
print(t2)


a,b,c=t #Tuple unpacking
#a,b=t #Numble of variables must match

print('\n')
#Dictionaries
#Maps keys to values
s = {
 'name': 'GOOG',
 'shares': 100,
 'price': 490.1
}
print(s['name'])
s['date']='6/6/2007'
#New value added because key not exists
#If key exists it modifies
s['price']=490.2
del s['date'] #Deletes
print(s)

keys=s.keys()
items= s.items()

print('\n')
#Sets
#COllection of unordered unique items
#Useful for duplicate elimination

set1={'123','abc','xyz'}
set2={'cat','fat'}
set1.add('cat')
set1.remove('123')
print("union",set1|set2,"intersection", set1&set2,"difference", set1-set2)#Set operations


print('\n')
#Containers
#Holds containers(Lists,Dicts,Sets)
portfolio=[('a',1),('b',2),('c',3)] #Tuple inside a list
print(portfolio[0])


print('\n')
#String formatting
a='ibm'
b=100
c=91.1
print(f'{a:>10s}{b:>10d}{c:>10f}')
print('{:10s} {:10d} {:10.2f}'.format(a, b, c)
)
print('%5s %-5d%10f'%(a,b,c))


for i, name in enumerate(names):
    print(i,name)

print("\n")
points=[
(1,4),(10,40),(23,14)
]
for x,y in points:
    print(x,y)


print('\n')
#zip()

cols=['a','b','c']
rows=[1,2,3]
pairs=zip(cols,rows)

print('\n')
#List comprehension(lambda functions)
[print(i) for i in pairs]

stocks={'price':101,'shares':51}
a=[print(s) for s in stocks if stocks['price']>100 and stocks['shares']>50]

print('\n')
#Copying
a=[1,2,3]
b=a #They show the same place not a copy
a.append(4)
print(b)
print("b=a:",a is b)#True(List is a pointer)

b=list(a) #Makes a copy
print("b=list(a):",a is b) #False (List is a copy)
print(a[0] is b[0]) #True (values are pointer)

import copy
b=copy.deepcopy(a)#Only safe way of copying
print("b=copy.deepcopy(a):",a is b) #False (list is copy)
print(a[0] is b[0])#True? (isn't it supposed to be False)

print('\n')
#Type
c='Hi World'
print(type(c))
if isinstance(c,(str,tuple)):
    print('c is a string or a tuple')
#Type checking cause excessive code complexity

print("\n")
#Understanding assignment

def foo(items):
 items.append(4)
a = [1, 2, 3]
print(a)
foo(a)
print("after foo items.append()",a)

def bar(items):
    items=[4,5,6]
b=[1,2,3]
print(b)
bar(b)
print("after reassigning inside function",b)
#When you reassign inside a local variable
#It does not change global variable


print("\n")
#Exceptions
try:
    print('Try block')
except Exception as e:
    print('Exception:',e)
except (IOError,LookupError,RuntimeError) as e2:
    print('Only for 3 error type',e2)
finally:
    print('Finally block')

print("\n")
#Special methods
class My_class():

    #for math
    def __add__(self,b):
        pass
    def __sub__(self,b):
        pass
    def __mul__(self,b):
        pass
    def __truediv__(self,b):
        pass
    def __floordiv__(self,b):
        pass
    def __mod__(self,b):
        pass
    def __lshift__(self,b):
        pass
    def __rshift__(self,b):
        pass
    def __and__(self,b):
        pass
    def __or__(self,b):
        pass
    def __xor__(self,b):
        pass
    def __pow__(self,b):
        pass
    def __neg__(self,b):
        pass
    def __invert__(self,b):
        pass
    def __abs__(self,b):
        pass

    #for item access
    def __len__(self):
        pass
    def __getitem__(self,a):
        pass
    def __setitem__(self,a,v):
        pass
    def __delitem__(self,a):
        pass
    
#Check oop_example for further information
