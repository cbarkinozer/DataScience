import math
class Shape():
    pass
class Circle(Shape,object):
    #Makes attributes unchangable
    __slots__=('_radius')

    #constructor
    def __init__(self,radius):
        self._radius=radius
    #"_" before the attribute name means
    #it is a private attribute(but tehnically it is public)

    def area(self):
        return math.pi * pow(self._radius,2)

    def perimeter(self):
        return 2*math.pi*self._radius

    #Getter
    @property
    def radius(self):
        return self._radius

    #Setter
    @radius.setter
    def radius(self,radius):
        if not isinstance(radius,float):
            raise TypeError('Expected float')
        self._radius=radius
    
        

def main():
        print("Classes inherit the object class by default.")
        print("You can do multiple inheritance. Python searches first and second")
        print("childeren first than goes for parent until the object class.")
        print("\n")

if __name__ == '__main__':
    main()

print("If you run the program from this script __name__== __main_")
print("Else __name__== 'oop_example' ")
print("\n")

c=Circle(4.0)

area=c.area()
perimeter=c.perimeter()
radius=c.radius
print("\n")

print(area,perimeter,radius)#50.26548245743669 25.132741228718345 4.0
c.radius=5.0
print(c.radius)#5.0
print("\n")


print("All data in python are stored in dictionaries")
print("Classes and instances have their own private dict")
print("Classes's dict stores its methods")
print("Instance's dict stores its attributes")
print("\n")

print("Attributes of the instance:",c.__dict__)
print("Methods of the class:",Circle.__dict__)
print("Instance class's dict:",c.__class__)
print("Method resolution order(class search order):",Circle.__mro__)
print("Is c instance of the parent class Shape? ",isinstance(c, Shape))
print("\n")

lookup=c.area
print("This is a lookup: ",lookup)
print("This is a method invocation: ",lookup())
print("\n")

''' SOME OF THE OUTPUT:
Attributes of the instance: {}
Methods of the class: {'__module__': '__main__', '__slots__': '_radius', '__init__': <function Circle.__init__ at 0x000001F857AA4E50>, 'area': <function Circle.area at 0x000001F857AA4EE0>, 'perimeter': <function Circle.perimeter at 0x000001F857AA4F70>, 'radius': <property object at 0x000001F857A9CEF0>, '_radius': <member '_radius' of 'Circle' objects>, '__doc__': None}
Instance class's dict: <class '__main__.Circle'>
Method resolution order(class search order): (<class '__main__.Circle'>, <class '__main__.Shape'>, <class 'object'>)
Is c instance of the parent class Shape?  True


This is a lookup:  <bound method Circle.area of <__main__.Circle object at 0x000001F857AAFFC0>>
This is a method invocation:  50.26548245743669
'''
