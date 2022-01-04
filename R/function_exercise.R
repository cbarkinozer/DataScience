set.seed(2018556059)

#1.Write a function that finds a prime number(s) given a set of numbers.
#Your function also provides prime factors of non-prime numbers.
#The function you will write should return the prime number(s) given in this vector and
#the non-prime number(s) with their prime factors.


#For example you have a vector of numbers like (89, 107, 597, 931, 1083).
#Your result will be Prime numbers : 89 107
#Non-prime numbers : 597 [3 199]  931 [7 7 19] 1083 [3 19 19]

prime_vector<-c(89,107,597,931,1083)


flag = 0
is.prime <- function(prime_vector) {
  
  prime<-vector()
  non_prime<-vector()
  
  divider<-0
  for(x in prime_vector ){
    
    if(x > 1) {
      flag = 1
      for(i in 2:(x-1)) {
        if ((x %% i) == 0) {
          flag = 0
          divider=i
          break
        }
      }
    } 
    if(x == 2){flag = 1}
    if(flag == 1) {
      prime<-c(prime,x)
    } else {
      non_prime<-c(non_prime,x)
      previous=x
      while((previous %% divider)==0){
        non_prime<-c(non_prime,paste("[",divider,"]"))
        previous=divider
        divider<-x/divider
        non_prime<-c(non_prime,paste("[",divider,"]"))
      }
      
    }
    
  }
  print("Prime numbers:")
  print(prime)
  print("Non-prime numbers:")
  print(non_prime)
} 

is.prime(prime_vector)

#2. Write a function that finds the letter numbers of all words in a given text and sorts the text according to those numbers from words with few letters to words with many letters.
#Sort the words containing the same number of letters alphabetically. For having text, you may use Sentences in tidyverse.
#Select 5 or 6 sentences randomly from Sentences. For example, you have these sentences. 

library(tidyverse)
library(stringr)
sentence<-stringr::sentences
sentence

sample<-sentence[sample(nchar(sentence), 5)]




