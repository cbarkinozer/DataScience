install.packages("tidyverse")
install.packages("nycflights13")

library(tidyverse)
library(nycflights13)

flights
help("nycflights13")

#We will use dplyr 5 functions(filter(row),arrange,select(col),mutate(define new)
#,summarize). Also groupby(categorize the data).
#tibble: shows data depending on screen size
#Shows columns data type(int,chr,dbl,fctr,dttm,date)

view(flights)#Show all data

filter(flights,month==1,day==1)

jan1<-filter(flights,month==1,day==1)

(dec25<-filter(flights,month==12,day==25))#Parenthesis shows data

#Popular mistake using "=" instead "=="

filter(flights,month==11|month==12)#Select both months

filter(flights,month %in% c(1,3,6))#Select multiple months

arrange(flights,year,month,day) #Arrange column order

arrange(flights,desc(arr_delay))#Descending order

select(flights,year,month,day)

select(flights,(year:day))#Select except unwanted

rename(flights,tail_num=tailnum)

select(flights,time_hour,air_time,everything())#First these columns then remaining

flights_sml<-select(flights,year:day,ends_with("delay"),distance,air_time)#select by this format

flights_sml

mutate(flights_sml,gain=arr_delay-dep_delay,speed=distance/air_time*60)#select with formulated new columns

transmute(flights_sml,gain=arr_delay-dep_delay,speed=distance/air_time*60)#only select mutate columns

summarize(flights,delay=mean(dep_delay,na.rm=TRUE))#Summarize all

by_day<-group_by(flights,year,month,day)#Group by yar, month, day

summarize(by_day,delay=mean(dep_delay,na.rm=TRUE))#Summarize by group

by_dest<-group_by(flights,dest)

delay<-summarize(by_dest,
                 count=n(),
                 dist=mean(dist,na.rm=TRUE),
                 delay=mean(arr_delay,na.rm=TRUE))

ggplot(data=delay,mapping=aes(x=distance,y=delay))+
      geom_point(aes(size=count),alpha=1/3)+
      geom_smooth(se=FALSE)

delay<-filter(delay,count>20,dest!="HNL")

ggplot(data=delay,mapping=aes(x=dist,y=delay))+
  geom_point(aes(size=count),alpha=1/3)+
  geom_smooth(se=FALSE)

#%>% is called the forward pipe operator in R. It provides a mechanism for chaining commands with a new forward-pipe operator

delay<-flights %>%
  group_by(dest) %>%
  summarize(
    count=n(),
    dist=mean(distance,na.rm=TRUE),
    delay=mean(arr_delay,na.rm=TRUE)
  ) %>%
  filter(count>20,dest!="HNL")

flights %>%
  group_by(year,month,day) %>%
  summarize(mean=mean(dep_delay,na.rm=TRUE))

#If you are receiving na answer , this means there are empty data
#Some flights cancelled so there are na in their delay time etc.

not_cancalled<-flights %>%
  filter(!is.na(dep_delay), !is.na(arr_delay))

not_cancalled %>%
  group_by(year,month,day) %>%
  summarize(mean=mean(dep_delay))
#Negative delay time means the plane is early

not_cancalled %>%
  group_by(year,month,day) %>%
  summarize(
    avg_delay1=mean(arr_delay),
    avg_delay2=mean(arr_delay[arr_delay>0])
)


not_cancalled %>%
  group_by(dest) %>%
  summarize(delay_mean=mean(arr_delay),
            delay_sd=sd(arr_delay) #Standard deviation
)%>% arrange(desc(delay_sd))

not_cancalled %>%
  group_by(year,month,day) %>%
  summarize(n_early=sum(dep_time<500))

daily<-group_by(flights,year,month,day)
(per_day<-summarize(daily,flights=n()))

(per_month<-summarize(per_day,flights=sum(flights)))

(per_year<-summarize(per_month,flights=sum(flights)))

daily%>%
  ungroup()%>%
  summarize(flights=n()) #Delete group and summarize

flights %>%
  group_by(year,month,day) %>%
  arrange(desc(arr_delay)) %>%
  select(year,month,day,dest,dep_delay,arr_delay)
  
popular_dests<-flights %>%
  group_by(dest) %>%
  filter(n()>365) %>%
  select(year,month,day,dest,dep_delay,arr_delay)

popular_dests

popular_dests%>%
  filter(arr_delay>0) %>%
  mutate(prop_elay=arr_delay/sum(arr_delay)) %>%
  arrange(desc(prop_delay))

df<-tibble(x=1:3,y=3:1) #How to create a tibble


#Tibble add row
df%>%
  add_row(x=4,y=0)

df%>%
  add_case(x=4,y=0)

df%>%
  rows_insert(tibble(x=4,y=0))

#Adding tibble as a row
df%>%
  add_row(tibble(x=4,y=0))

#It is suggested that you do not delete data
df%>%
  rows_delete(tibble(x=3))

#Instead filter the data
df%>%
  filter(x!=3)



cat_flights<-flights %>%
  mutate(delay_gr=cut(arr_delay,breaks=c(-Inf,0,Inf),labels=c("Early arrivals","Delayed arrivals"))) %>%
  select(dest,delay_gr)
  
#There are 2 ways

gather(cat_flights,dest,delay_gr) %>%
  count(dest,delay_gr) %>%
  spread(delay_gr,n,fill=0)

table(cat_flights$dest,cat_flights$delay_gr)
