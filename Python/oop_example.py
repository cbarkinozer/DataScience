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
#c.radius(4.0)
#radius=radius(c)

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
