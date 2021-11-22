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
    return a+b
print(sum(1,2))#Calling a function
#If you write no return, it will return None
#If you write return with multiple elements
#It will  return tuple


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

