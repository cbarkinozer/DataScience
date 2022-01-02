library(tidyverse)

#Creates a table with a,b,c as column names, and rest as rows
# to read a csv (comma separated) file from a directory
ourdata<-read_csv("data/heightsdata.csv")
ourdata

# read a csv (semicolon separated) file from a directory
ourdata<-read_csv2("data/heightsdata.csv")
ourdata

# create a CSV file
read_csv("a,b,c
1,2,3
4,5,6")

#Basic example
#csv reading,manipulating columns and downloading csv back 

library(tidyverse)

data<-read_csv2("D:/Desktop/student-por.csv")

data<-data %>% mutate( data , pass=if_else(G3>=12,true="yes",false = "no"))

data<-select(data, -G1,-G2,-G3)

write.csv(data, file = "D:/Desktop/student-por2.csv")




# skip the first 2 line when reading from a file
read_csv("The first line of metadata
The second line of metadata
x,y,z
1,2,3", skip = 2) #Skip first 2 rows

# skip a line starting with a symbol
read_csv("# A comment I want to skip
x,y,z
1,2,3", comment = "#") #Skip by symbol

# if the column names are missing, we can automatically assign the names as X1,..,Xn
read_csv("1,2,3
         4,5,6", col_names = FALSE)

# "\n" is a convenient shortcut for adding a new line.
read_csv("1,2,3\n4,5,6", col_names = FALSE)

# assing the column names, a character vector can be used
read_csv("1,2,3\n4,5,6", col_names = c("x", "y", "z"))

# assign the missing values as NA
x<-read_csv("a,b,c\n1,2,.\nA,3,4", na = ".") #Make "." as NA
x

# check values whether they are integer values or not
parse_integer(x$a)

parse_logical(c("TRUE", "FALSE", "T", "1", "9"))
parse_date(c("2020-12-03", "2020-26-11"))

# check the values when you create a vector
y <- parse_integer(c("123", "345", "abc", "123.45"))

# see all parsing failures, use problems()
problems(y)

# working with a large file, you may have lots of parsing failures
challenge <- read_csv(readr_example("challenge.csv"))
problems(challenge)

# to overcome parsing problems, change the column specification
challenge <- read_csv(
  readr_example("challenge.csv"),
  col_types = cols(
    x = col_double(),
    y = col_character()
  )
)

# figure out the type of column y
guess_parser(challenge$y)

# change the column specification of column y to date
challenge <- read_csv(
  readr_example("challenge.csv"),
  col_types = cols(
    x = col_double(),
    y = col_date()
  )
)

# read the other Excel formats, use readxl library
library(readxl)

# read an xls or xlsx file, use read_excel funtion
xlsx_example <- readxl_example("datasets.xlsx")
read_excel(xlsx_example)

# get the list of sheet names
excel_sheets(xlsx_example)

# read data from a sheet
read_excel(xlsx_example, sheet = "mtcars")

# write your data to a csv file
write_csv(challenge, "challenge.csv")

# datasets with different data organization
table1
table2
table3
table4a
table4b

# untidy data example
table4a

# make it tidy, use gather() function
table4a %>%
  gather(`1999`, `2000`, key = "year", value = "cases")


table4b %>%
  gather(`1999`, `2000`, key = "year", value = "population")

# combine the tidied datasets into a single tibble, use dplyr::left_join()
tidy4a <- table4a %>%
  gather(`1999`, `2000`, key = "year", value = "cases")
tidy4b <- table4b %>%
  gather(`1999`, `2000`, key = "year", value = "population")
left_join(tidy4a, tidy4b)

# observations in multiple rows
table2

# spread rows into columns
spread(table2, key = type, value = count)

# data having one column containing two variables
table3

# separate these two variables
table3 %>%
  separate(rate, into = c("cases", "population"), sep = "/")

# convert the data types to correct ones
table3 %>%
  separate(rate, into = c("cases", "population"),
           convert = TRUE
  )

# separate variables according to a specified position
table3 %>%
  separate(year, into = c("century", "year"), sep = 2)
