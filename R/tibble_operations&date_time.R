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

x1<-c("Dec","Apr","Jan","Mar","Mat")

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

#Shows the error
y1<-parse_factor(x2,levels=month_levels)

#Omits levels
factor(x1)

install.packages("lubridate")

library(lubridate)

today() #Day of today

now() #Current day and time

#Date-time types y:year, m:month, d:day, h:hour, m:minute, s:second

ymd("2021-11-25")

mdy("November 25th, 2021")

dmy("25-Nov-2021")

ymd(20211125)

ymd_hms("2021-11-25 21:54:45")

mdy_hm("11/25/2021 21:54")

library(nycflights13)

flights %>%
  select(year,month,day,hour,minute) %>%
  make_datetime(year,month,day,hour,minute) %>%
  mutate(
    departure= make_datetime(year,month,day,hour,month,hour,minute)
  )

datetime<-ymd_hms("2021-11-25 22:05:25")  

year(datetime)

mont(datetime)

mday(datetime)

yday(datetime)

wday(datetime)

hour(datetime)

month(datetime,label=TRUE) #Shows month order in Turkish as abbreviation(abbr)

wday(datetime,label=TRUE,abbr=FALSE) #Shows days of the week in Turkish no abbr

year(datetime)<-2022

datetime

month(datetime)<-12

hour(datetime)<-13

datetime

update(datetime,year=2021,month=11,mday=28,hour=20)

#Update date
ymd("2015-02-01") %>%
  update(mday=30)

# If values are too big, it will be divided to month count
#And remainder will be found

ymd("2015-02-01") %>%
  update(mday = 30)

ymd("2015-02-01") %>%
  update(hour = 400)

# Calculating the age of our university 
Uni_age <- today() - ymd(19731130)
Uni_age

#Converting date-time type
as.duration(Uni_age)

# to construct a date/time, use period functions
seconds(15)
minutes(10)
hours(c(12, 24))
days(7) 
months(1:6)
weeks(3)
years(1)

# we can do addition and multiplication operations on date-time
10 * (months(6) + days(1))
days(50) + hours(25) + minutes(2)
