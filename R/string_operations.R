install.packages("tidyverse")
library(tidyverse)

str1<-"This is a string"
string2<-"To put 'quote', use single quote"

"\u00b5" #special unicode symbol

?"'" #Show options

str_length(c("a","R for data science",NA)) #Length of these values

str_c("x","y","z") #concatenate

str_c("Letter",seq_along(letters),letters,sep=":")

str_c(str_c(seq_along(letters),"Letter"),letters,sep=":")

x<-c("abc",NA)
str_c("|-",x,"-|")#Adding variable inside string

str_c("|-",str_replace_na(x),"-|")


name<-"Data"
time_of_day<-" Evening"
birthday<-TRUE
str_c(
  "Good", time_of_day," ",name,",",
  if(birthday) " Happy Birthday"
)

str_c(letters,collapse=",") #letters are defined as all letters in alphabet

x<-c("Apple","Banana","Pear")

str_sub(x,1,3) #substring

str_sub(x,-3,-1)

str_sub("a",1,5) #Don't give index out of bound error just gives result

str_sub(x,1,1)<-str_to_lower(str_sub(x,1,1))
x

str_to_upper(c("ý","i"),locale="tr") #Turkish
x<-c("inci","ýþýk","ýslak")
str_sort(x,locale="tr")

install.packages("htmlwidgets")
library(htmlwidgets)
x<-c("Apple","Banana","Pear")
str_view(x,"an")
str_view(x,".a.")#There are letters before and after a
str_view_all(x,"an")

str_view(c("abc","a.c","def"),"\\.") #To search . in string
str_view(c("a\\b"),"\\\\") #To search \ in string

str_view(x,"^A")#To search  starts with A
str_view(x,"a$")#To search ends with a

x<-c("apple pie","apple","apple cake")
str_view(x,"^apple$") #I just want apple so I show start and end

x<-c("Apple","Banana","Pear")
sum(str_detect(x,"e")) #Find how many of them has it
#detect turns boolean

sum(str_detect(words,"^t")) #Show count

mean(str_detect(words,"[aeiou]$")) #%27 has it

no_vovels<-!str_detect(words,"[aeiou]")
no_vovels_2<-str_detect(words,"^[^aeiou]+$")

identical(no_vovels,no_vovels_2)#They are identical

words[no_vovels_2] #Ones with no vowels

words[str_detect(words,"x$")]
str_subset(words,"x$")

df<-tibble(
  word=words,
  i=seq_along(word)
)
df%>%
  filter(str_detect(words,"x$"))


str_count(x,"a")#how many a char exist?

mean(str_count(words,"[aeiou]"))

df %>%
  mutate(
    vovels =str_count(word,"[aeiou]"),
    consonants= str_count(word,"[^aeiou]")
  )

str_count("abababa","aba")
str_view_all("abababa","aba")


colors<-c(" red "," orange "," yellow "," green "," blue "," purple "," brown ")
color_match<-str_c(colors,collapse="|")


has_color<-str_subset(sentences,color_match) #Find sentences who has colors in them

str_extract(has_color,color_match)

more<-sentences[str_count(sentences,color_match)>1]
str_view_all(more,color_match)

str_extract_all(more,color_match,simplify = TRUE)

x<-c("a","a b","a b c")
str_extract_all(words,"[a-z]",simplify = TRUE)

noun<-"(a|the|an|A|The) ([^ ]+)"
has_noun<-sentences %>%
  str_subset(noun) %>%
  head(10)

has_noun %>% 
  str_extract(noun)

has_noun %>% 
  str_match(noun)

tibble(sentence=sentences) %>%
  extract(
    sentence,c("article","noun","(a|the) ([^ ]+)"),
    remove=FALSE
  )

has_noun %>%
  str_match_all(noun)

x<-c("Apple","Banana","Pear")
str_replace(x,"[aeiou]","-")
str_replace_all(x,"[aeiou]","-")

sentences %>%
  head(5) %>%
  str_split(" ")

"a|b|c|d" %>%
  str_split("\\|")%>%
  .[[1]]

sentences %>%
  head(5) %>%
  str_split(" ",simplify=TRUE)

sentences %>%
  head(5) %>%
  str_split(" ") %>%
  simplify()


fields<-c("Name:Hadley:ADC","Country:NZ","Age:35")
fields %>%
  str_split(":",simplify=TRUE)

x<-"This is a sentence. This is another sentence"

str_view_all(x,boundary("word"))
str_split(x," ")
str_split(x,boundary("word"))
