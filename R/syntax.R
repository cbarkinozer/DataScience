a<-c(1,2,3,4,5,6,7) #Create a vector
a[2] #Select second element of the vector
a[c(1,3,5)]
max(a) #Maximum element
a==3
which(a==3)
min(a)
length(a)
#print from 1 to 8
1:8
ids<-1:length(a)
ids[a==3]
(1:length(a))[a==max(a)]
seq(10,20,2)
#c() function creates vector
a<-c(a,8,9,10,11)
a[12]<-12
sample(a,5) #Randomly samples
sample(a,5,replace=TRUE) #Repeatable
a$a
summary(a) #Gives a brief summary about data
a<-list(a=c(1:10),b=c("a"),c=c(T,F,F,T))
e<-data.frame(a=c(1:5),b=rnorm(5),d=c("a","b","c"))
#Dataframes are matrices that hold different type of values
e$a[3] #Select 3rd feature from e
data.entry(e)
rnorm(5)
e<-cbind(e,ff=c(6:10))
na.omit(e)
ls()
rm(a)
rm(list=ls())
install.packages("pacman")