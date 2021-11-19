install.packages("tidyverse")

installed.packages("nyclfights13")

library(tidyverse)

ggplot(data=diamonds)+
    geom_bar(mapping=aes(x=cut))

diamonds %>%
    count(cut)

#Histogram-bar difference: columns in histogram are conjoin to each other
ggplot(data=diamonds) +
  geom_histogram(mapping=aes(x=carat),binwidth = 0.5)


diamonds %>% 
  count(cut_width(carat,0.5))

smaller<-diamonds %>% 
  filter(carat<3)

#We realize actually there are more distributions that are different
ggplot(data=smaller,mapping=aes(x=carat))+
  geom_histogram(binwidth = 0.1)

ggplot(data=smaller,mapping=aes(x=carat,color=cut))+
  geom_freqpoly(binwidth=0.1)

#Canvas is wide because there are outliers even at y=60
ggplot(data=diamonds)+
  geom_histogram(mapping=aes(x=y),binwidth=0.5)

#To zoom in canvas
ggplot(data=diamonds)+
  geom_histogram(mapping=aes(x=y),binwidth=0.5)+
  coord_cartesian(ylim=c(0,50))

#We tried to find outlier's rows
unusal<-diamonds %>%
  filter(y<3|y>20)%>%
  arrange(y)
unusal

#To delete outliers
diamonds %>%
  filter(between(y,3,20))

#Statistics do not condone deleting outliers
#We should change outliers with NA

diamonds2<-diamonds %>%
  mutate(y=ifelse(y<3|y>20,NA,y))

diamonds2%>%
  filter(is.na(y))

# %>% carries the data to the up line

#If we add na.rm=TRUE, na values are deleted warning will be surpressed
ggplot(data=diamonds2,mapping=aes(x=x,y=y))+
  geom_point()


#Returns the wanted dataset without downloading the all package
nycflights13::flights %>%
  mutate(
    cancelled=is.na(dep_time),
    sched_hour = sched_dep_time %/% 100, #böl
    sched_min = sched_dep_time %% 100, #Modunu al
    sched_dep_time= sched_hour + sched_min /60
  ) %>%
  ggplot(mapping = aes(sched_dep_time,y=..density..))+
  geom_freqpoly(
    mapping = aes(color= cancelled),
    binwidth=1/4
  )


#After the hour 15 retardation is much longer because a plane flies many times a day
#All retardations stack each other and affect late flights

ggplot(data=diamonds,mapping = aes(x=price))+
  geom_freqpoly(mapping = aes(color=cut),binwidth=500)

ggplot(data=diamonds,mapping = aes(x=price,y=..density..))+
  geom_freqpoly(mapping = aes(color=cut),binwidth=500)

ggplot(data=diamonds,mapping = aes(x=cut,y=price)) +
  geom_boxplot()

ggplot(data=mpg,mapping=aes(x=class,y=hwy))+
  geom_boxplot()

ggplot(data=mpg)+
  geom_boxplot(
    mapping=aes(x=reorder(class,hwy,FUN=median),
                y=hwy)
  )

ggplot(data=diamonds)+
  geom_count(mapping=aes(x=cut,y=color))


diamonds %>%
  count(color,cut) %>% 
  arrange(desc(n))

#Heatmap
diamonds %>%
  count(color,cut)%>%
  ggplot(mapping=aes(x=cut,y=color))+
  geom_tile(mapping = aes(fill=n))

#Carat-price relationship, data overlaps
ggplot(data=diamonds)+
  geom_point(mapping=aes(x=carat,y=price))

#make it faint to see overlapping values
ggplot(data=diamonds)+
  geom_point(mapping=aes(x=carat,y=price),alpha=1/100)

#If you have too much data do not use scatter plot

ggplot(data = smaller,mapping = aes(x=carat,y=price))+
  geom_boxplot(mapping = aes(group=cut_width(carat,0.1)))

#Exponentially increasing(decreasingly increasing)
ggplot(data = smaller,mapping = aes(x=carat,y=price))+
  geom_boxplot(mapping = aes(group=cut_number(carat,20)))
