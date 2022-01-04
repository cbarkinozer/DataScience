set.seed(2018556059)

#1.
#Write a function that finds a prime number(s) given a set of numbers.
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
  for(x in prime_vector ){ #For every number in vector
    
    if(x > 1) {
      flag = 1
      for(i in 2:(x-1)) { # i from 2 to last number
        if ((x %% i) == 0) { #Check if i can divide number
          flag = 0           #Flag set to 0
          divider=i          #Divider saved
          break
        }
      }
    } 
    if(x == 2){flag = 1}      #If number is 2, it is prime
    if(flag == 1) {           #If flag is 1, it is prime
      prime<-c(prime,x)       #Add to prime
    } else {                  #Else flag is 0
      non_prime<-c(non_prime,x)  #Add to non_prime. Now add it's dividers.
      non_prime<-c(non_prime,paste("[",divider,"]"))
      divider<-x/divider
      non_prime<-c(non_prime,paste("[",divider,"]")) 
      
    }
    
  }
  print("Prime numbers:")
  print(prime)
  print("Non-prime numbers:")
  print(non_prime)
}
is.prime(prime_vector)

#[1] "Prime numbers:"
#[1]  89 107
#[1] "Non-prime numbers:"
#[1] "597"     "[ 3 ]"   "[ 199 ]" "931"     "[ 7 ]"   "[ 133 ]" "1083"    "[ 3 ]"   "[ 361 ]"




#2.
#Write a function that finds the letter numbers of all words in a given text and sorts the text according to those numbers from words with few letters to words with many letters.
#Sort the words containing the same number of letters alphabetically. For having text, you may use Sentences in tidyverse.
#Select 5 or 6 sentences randomly from Sentences. 

library(tidyverse)
library(stringr)
sentence<-stringr::sentences
sentence

sample<-sentence[sample(nchar(sentence), 5)] #Sampling 5 sentences
sample_words<-vector()
sample<-c(sample_words,unlist(strsplit(gsub("\\.","",sample)," "))) #Add words from sentences

sentence.sort<-function(x){
    x<-tolower(x) #Lower the words
    sorted<-str_sort(x, locale="eng") #Sort alphabetically
    sorted<-x[order(str_count(x,"."))] #Order by word length
    for(i in sorted){
      result<-cat(paste(i," ")) #Concatinate word vector to a single string
    }
    result<-str_replace(result, "NULL","") #Deleting the last NULL
    result #print result
}

sentence.sort(sample)

#a  go  in  of  the  was  the  the  you  out  the  the  the  the  gas  meal  bell  rang  mend  coat  king  days  mesh
#mire  note  size  tank  ruled  state  early  keeps  cooked  before  before  chicks  inside  closely  character(0)
