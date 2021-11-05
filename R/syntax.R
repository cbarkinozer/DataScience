a<-c(2,3,0,3,1,0,0,1)      # creating a vector
a

sum(a)    # using a function, sum function, to sum up of all values in the vector a.

b<-sum(a)  # assigning the result of a function to another object.
b

str(a)   #  returns the structure of an object

plot(a)  # gives scatter plot of an object


mode(a)   # returns type of data

b<-"a"
mode(b) # character

c<-TRUE
mode(c) # logical

mode(sum)  # function

a1<-c(2,3,0,3,1,0,0,1)
a2<-a1   # make a copy
a2[1]<-0  # assign the first entry 0


a2 			# print out the value
a2[2] 		# print 2nd entry value
a2[-4] 		# all but the 4th entry
a2[c(1,2,3)] 	# print 1st, 2nd and 3rd.


max(a)  # maximum value of a
a == 3  # returns True of false whether entry is equal to 3
which(a==3) # returns the indices of entries which are equal to 3


length(a) # gives the number of the entries in the vector a.


a3<-c(1:8)  # gives a vector of the numbers from 1 to 8
a4<-seq(10,20,2)  # gives a vector of the numbers from 10 to 20 increasing by 2.

n<-length(a2) # how many entries do we have?
ids<-1:n      # how do we get the ids of the entries? 
ids           
ids[a2==3]    # what are the ids of entries which are equal to 3?


(1:length(a2))[a2 == max(a2)] # starting with creating a vector of numbers from 1 to length of a2
                              # then creating TRUE-FALSE vector depending on whether if the entries of a2 are equal to maximum value of a2.
                              # finally it returns the numbers corresponding to TRUE entries from the vector of numbers.


a2>0    # returns TRUE/FALSE vector depending on whether if the entry is greater than 0 or not
sum(a2>0) # sum of the entries whose values are greater than 0.


x<-c(45,43,46,48,51,46,50,47,46,45)
length(x)
x<-c(x,48,49,51,50,49)  # append values to x
length(x)    # how long is x now

x[16]<-41  # add to a specified index
x[17:20]<-c(40,38,35,40)  # add to many specified indices

sample(c(1:10),size=10,replace=TRUE)  # taking sample with replacement
sample(c(1:10), size = 5, replace = FALSE) # taking sample without replacement

a<-c(TRUE, FALSE, T, F)       # logical (true/false) vector
a
b<-c("Ceng","cen429")    # vector of characters
b
class(b)               # type of vector (mode(b), typeof(b),str(b))

d<-matrix(c(1:12),nrow=4,ncol=3)   # a 4x3 matrix
d
d<-matrix(c(1:12),nrow=4,ncol=3,byrow=TRUE)  # a matrix filled by rows
d
d<-matrix(c(1:12),nrow=4,ncol=3,byrow=FALSE) # a matrix filled by columns, the default
d

a <- list(a=c(1:10), b = c("a"), c = c(TRUE, FALSE, TRUE, FALSE))   # list of vectors
summary(a)

aa <- array(c(1:12), dim = c(6, 2))     # same as a matrix with 6 rows and 2 columns
aa
bb <- array(c(1:24), dim = c(4, 3, 2))	# a multidimensional object
bb

e <- data.frame(a = c(1:5), b = rnorm(5), d = c("a", "b", "c", "d", "e"))  # well known data format
e
names(e)
e<-cbind(e,F=c(6:10))   # adding a variable (column) to data
e
e<-rbind(e,c(6,0.5,"f",11)) # adding a case (row) to data
e
e$F<-NULL  # deleting a variable
e


data.entry(x) # Pops up spreadsheet to edit data
x

na.omit(x)  # delete the NA values

ls()   # list of all objects

rm(a)   # remove an object
ls()
rm(list=ls())    # remove all objects in the environment
ls()
