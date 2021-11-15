install.packages("tidyverse")
library(tidyverse)
#Starwars is in tidyverse

view(starwars)#Show all data

#1. answer

ship_owners<-filter(starwars,starships !="character(0)")

length(ship_owners$name)

(ship_owners$name)

#2. answer

eye_frequency<-starwars %>%
  group_by(eye_color) %>%
  summarize(
    count=n()
  )

arrange(eye_frequency,desc(count))

#3.answer

#When an element of a specie's birth_year is null
#Mean becomes null therefore I deleted NA values

na_deleted=filter(starwars,birth_year !="NA")

mean_age<-na_deleted %>%
  group_by(species) %>%
  summarize(
    mean_birth=mean(birth_year)
  )

specie_mean_age<-arrange(mean_age,desc(mean_birth))

specie_mean_age[c(1,2,3),]

#4. answer

my_character<-rbind(starwars,c(name="cbarkinozer",height=183,mass=70,
                               hair_color="brown",skin_color="light",
                               eye_color="blue",
                               birth_year=22.0,sex="male",gender="masculine",
                               homeworld="Tatooin",species="Human","A New Hope",
                               "Imperial speeder bike","x-wing"))

my_character$height<-as.integer(my_character$height)

my_character$mass<-as.double(my_character$mass)

tail(my_character,1)

#5. answer

my_character<-my_character %>%
  mutate(my_character,BMI=mass/((height/100)^2))

my_character<-my_character %>%
  mutate(my_character,body_type=if_else(BMI<18.5,"underweight",
                                        if_else(BMI<25,"healthy",
                                                if_else(BMI<30,"overweight",
                                                        "obese"))))

(my_character)

#6. answer

my_character$birth_year<-as.integer(my_character$birth_year)

age_below_hundred<-filter(my_character,birth_year<100.0)

ggplot(data=age_below_hundred)+
  geom_point(mapping=aes(x=birth_year,y=BMI))

#7. answer
ggplot(data=my_character)+
  geom_point(mapping=aes(x=birth_year,y=BMI))+
  geom_smooth(mapping=aes(x=birth_year,y=BMI))

ggplot(data=age_below_hundred,mapping=aes(x=birth_year,y=BMI))+
  geom_point()+
  geom_smooth(data=filter(age_below_hundred,birth_year<100 & BMI<100))
