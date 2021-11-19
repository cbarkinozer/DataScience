class Shape():
    pass
class Circle(Shape,object):
    #Makes attributes unchangable
    __slots__=('_radius')

    #constructor
    def __init__(self,radius):
        self._radius=radius
    #"_" before the attribute name means
    #it is a private attribute(but actually it is public)

    @property #getter
    def area(self):
        return math.pi*(self.radius**2)

    @property
    def perimeter(self):
        return 2*math.pi*self.radius

    @radius.setter #setter
    def radius(self,radius):
        if not isinstance(radius,float):
            raise TypeError('Expected float')
        self._radius=radius
    
    def main():
        print("Classes inherit the object class by default.")
        print("You can do multiple inheritance. Python searches first and second")
        print("childeren first than goes for parent until the object class.")
        
        

if __name__ == "__main__":
    main()

print("If you run the program from this script __name__== __main_")
print("Else __name__== "oop_example")

c=Circle(4.0)

a=c.area()
p=c.perimeter()
r=c.radius

print("All data in python are stored in dictionaries")
print("Classes and instances have their own private dict")
print("Classes's dict stores its methods")
print("Instance's dict stores its attributes")

print("Attributes of the instance:"+c.__dict__)
print("Methods of the class:"+Circle.__dict__)
print("Instance class's dict:"+c.__class__)
print("Method resolution order(class search order):"+c.__mro__)
print("Is c instance of the parent class Shape ?"+isinstance(c, Shape))

lookup=c.area
print("This is a lookup: "+lookup)
print("This is a method invocation: "+lookup())

#I could not solve this error.
#File "<string>", line 6, in <module>
#  File "<string>", line 24, in Circle
#NameError: name 'radius' is not defined


