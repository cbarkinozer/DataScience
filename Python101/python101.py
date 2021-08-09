#FIRST PROBLEM
#Flattening 3d and higher dimensions irregular lists
my_list1=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
import collections
#Only 2D or 1D can be flattened with itertools.chain.from_iterable() 
def flatten(x):
    for elem in x:a
        if isinstance(elem, list): #Check if elem is a list
            yield from flatten(elem) #yield makes the function construction and returns value
        else:
            yield elem

my_list1 = [a for a in flatten(my_list)] #For every sub list
flatten(my_list1)
print(my_list1)
#>>> [5, 4, 3, 'dog', 1, 'a', 'cat', 2]

#SECOND PROBLEM
my_list2=[[1, 2], [3, 4], [5, 6, 7]]
#Reverse the list
my_list2.reverse()
#Reverse sub lists
my_list2 = [ i[::-1] for i in my_list2]
print(my_list2)
#>>>[[7, 6, 5], [4, 3], [2, 1]]