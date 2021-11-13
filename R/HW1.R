install.packages("tidyverse")
library(tidyverse)
#Starwars is in tidyverse

view(starwars)#Show all data

#1. answer
ship_owners<-filter(starwars,starships !="character(0)")
(ship_owners$name)

#2. answer
eye_frequency<-starwars %>%
  group_by(eye_color) %>%
  summarize(
    count=n()
  )
arrange(eye_frequency,desc(count))

#3.answer
mean_age<-starwars %>%
  group_by(species) %>%
  summarize(
    mean_birth=mean(birth_year)
  )
a1<-arrange(mean_age,desc(mean_birth))
head(a1,3)


#4. answer
my_character<-rbind(starwars,c("cbarkinozer",183,70,"brown","blue",22.0,"male","masculine","Tatooin","Human","A New Hope","Imperial speeder bike","X-wing"))
tail(my_character,1)

#5. answer
mutate(my_character,BMI=mass/sqrt(height/100))
