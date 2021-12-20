
library(tidyverse)

ourdata<-read_csv2("D:/Desktop/covid-data-2020.csv") #Reading csv seperated by ";"

set.seed(2018556059) #Seeding for sampling

sample<-ourdata[sample(nrow(ourdata), 1000, replace = FALSE, prob = NULL),] #Sampling


#Filtering negative values in new_case and new_deaths
sample<-filter(sample,new_cases>=0,new_deaths>=0)

#My data looks like this
sample

#1_Calculate the five-number summary statistics (minimum-Q1-median-Q3-maximum) of covid-19 daily new cases for each country within each month.
#(you can use quantile() function to get the quartiles)


five_number_stats<-sample %>%
  group_by(month,location) %>%
  summarize(min=min(new_cases),Q1=quantile(new_cases,0.25,na.rm=TRUE),Q2=quantile(new_cases,0.50,na.rm=TRUE),Q3=quantile(new_cases,0.75,na.rm=TRUE),max=max(new_cases))

five_number_stats

#2_Find the highest daily cases and deaths separately for each country. 

highest_deaths_and_daily_cases<-sample %>%
  group_by(location) %>%
  summarize(max_case=max(new_cases,na.rm=TRUE),max_deaths=max(new_deaths,na.rm=TRUE))

highest_deaths_and_daily_cases

#3_Identify the month in which the mean daily cases is the highest for each country.

#-UNFINISHED-

#temp<-filter(sample,new_cases==max(mean(new_cases,na.rm=TRUE)))
  
month_with_highest_daily_cases<-sample %>%
  group_by(location) %>%
  summarize(Mean_of_dailycases=mean(new_cases,na.rm=TRUE))

month_with_highest_daily_cases
#Select 3 country and plot the distribution of daily cases by month. Use location as clusters (i.e., color=location)
#to show the difference between countries.

#-UNFINISHED-


selected_months<-filter(sample,location ==c("Turkey","Germany","Russia") )

ggplot(data=selected_months,mapping=aes(x=month,y=new_cases))+
  geom_point(mapping=aes(color=location))
