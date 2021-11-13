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
my_character<-rbind(starwars,c(name="cbarkinozer",height=183,mass=70,hair_color="brown",skin_color="light",eye_color="blue",birth_year=22.0,sex="male",gender="masculine",homeworld="Tatooin",species="Human","A New Hope","Imperial speeder bike","x-wing"))
my_character$height<-as.integer(my_character$height)
my_character$mass<-as.double(my_character$mass)
tail(my_character,1)

#5. answer
my_character %>%
  mutate(name,BMI=mass/((height/100)^2))
(my_character)
