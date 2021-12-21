library(tidyverse)
set.seed(2018556059) #Seeding for sampling


#Answer the following questions by using the sentences, which are provided in stringr::sentences.
library(stringr)
sentence<-stringr::sentences
sentence


#1_Take a random sample of 100 sentences from this data, then split these sentences into words and take each word as a member of a vector.
#After removing duplicated words (you can use unique() function to remove duplicated words), save this sample as a new data.
sample<-sentence[sample(nchar(sentence), 100)] #Sampling
new_data<-unlist(strsplit(gsub("\\.","",sample)," "))
new_data

new_data<-unique(new_data)
new_data

#2_Find words which are starting with “a” and ending with “e”.

second_result<-str_view_all(new_data,"^a.e$")

second_result
#3_Calculate the number of words which have more than 3 vowels.

third_result<-new_data[str_count(new_data,"[aeiou]")>3]
third_result<-length(third_result)
third_result

#4_List the five longest word in your data

fourth_result<-tail(new_data[order(str_count(new_data,"."))], 5)
fourth_result

#5_Try to find word(s) which contain any of these words: age, any, day, exp, her, pro, the.

words<-c("age","any","day","exp","her","pro","the")
str_match<-str_c(words,collapse="|") #Concat strings
has_str<-str_subset(new_data,str_match)
fifth_result<-has_str

fifth_result
