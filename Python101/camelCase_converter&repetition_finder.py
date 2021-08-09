import re #RegEx
#Repetition in array finder
def EquivalentKeypresses(strArr):
  my_str=""
  #Convert array to string and delete ","
  my_str="".join(strArr)
  #Delete comas
  my_str= re.sub(',', '', my_str)
  #concatenate string with itself
  #The find() method finds the first occurrence of the specified value.  
  i = (my_str+my_str).find(my_str, 1, -1)
  return "false" if i == -1 else "true"
  
  
  #Any string to camelCase converter
  #Words must be seperated by non-alphabet elements
  def DifferentCases(strParam):
    strParam= re.sub('[^a-zA-Z]+', ' ', strParam)
    strParam = ''.join(word.title() for word in strParam.split(" "))
    return strParam
  
  
