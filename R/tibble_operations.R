library(tidyverse)

as_tibble(iris) # to convert a data frame to a tibble

iris

# to create a tibble
tibble(
  x=1:5,
  y=1,
  z=x^2+y
)
# to create a tibble, with `` any kind of column names can be created
tb<-tibble(
  `:)`="smile",
  ` `="space",
  `2000`="number"
)
tb

#Creating a tibble in another way
tribble(
  ~x,~y,~z,
  "a",2,3.6,
  "b",1,8.5
)

# to print more output than the default display
nycflights13::flights %>%
  print(n=10,width=Inf)#Row and column(infinite) size

# to print more output than the default display
options(tibble.print_min=15,tibble.widht=100)

nycflights13::flights

df<-tibble(
  x=runif(5),
  y=rnorm(5)
  )
df


# Extract by name
df$x

# Extract by position
df[["x"]]

# Extract by position
df[[1]]

# Extract by name using pipe using dot
df %>%
  .$x

# Extract by name using pipe using dot
df %>%
  .[[1]]

x1<-c("Dec","Apr","Jan","Mar")

#Sorts in alphabetical order but we want to sort by month number
sort(x1)

month_levels<-c("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep",
                "Oct","Nov","Dec")

#Sorts by defined sequence
y1<-factor(x1,levels=month_levels)
# any values not in the levels will be NA
y1

#Now sorts correctly
sort(y1)
