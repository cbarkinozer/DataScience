install.packages("tidyverse")
library(tidyverse)

read_csv("C:/Users/lab2/Desktop/Book1.xlsx")
read_csv2("C:/Users/lab2/Desktop/Book1.xlsx")

#Creates a table with a,b,c are col names, and rest as row
read_csv("a,b,c
         1,2,3
         4,5,6")

read_csv("The first line of metadata
The second line of metadata
a,b,c
1,2,3
         4,5,6",skip=2) #Skip first rows

read_csv("x,y,z
         #A comment I want to skip 
         1,2,3",comment="#") #Skip by symbol

read_csv("1,2,3
         4,5,6",col_names=FALSE)

read_csv("1,2,3
         4,5,6",col_names=c("x","y","z"))

read_csv("1,2,3\n4,5,6",col_names=c("x","y","z"))

x<-read_csv("a,b,c\n1,2,.\nA,3,4",na=".") #Make "." as NA

parse_integer(x$b)
