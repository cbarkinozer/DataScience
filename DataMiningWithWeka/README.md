# DataMiningWithWeka

Markdown version of my report. You can find full analyze on "DataMiningReport.docx" .

## Abstract
In this article, two distinct datasets were chosen based on data size, number of features, and missing values.
These datasets were trained using four distinct types of algorithms, and the accuracy, model build times, and causes of the results were examined.

## Introduction
Data mining is extracting information from data by finding patterns.
In this Project, data mining techniques were used for 2 different data sets.
To obtain the datasets, mushroom.arff from Github [3] (there is also a Kaggle page [1] of the mushroom dataset in CSV format) and Student_por.csv,
taken from the Kaggle students' performance analysis dataset webpage[2].
4 classification algorithms are used for comparement. These are:
Bayes->NaiveBayes (Naive Bayes classifier)
 Tree->J48 (Decision tree classifier)
 Rules->OneR (Rule based classifier)
 Lazy->IBk(k-Nearest neighbor classifier)
To apply these algorithms Weka application is used. [4]
Weka is a data mining system developed by the University of Waikato in New Zealand that implements data mining algorithms.
Weka uses ARFF file formatted datasets that consist of independent, unordered instances and do not involve relationships among instances.[4]

## CHAPTER I: Dataset Descriptions
In this chapter, datasets context, content, inspiration, acknowledgments, and attributes will be explained for both of the datasets.
### Mushroom Dataset Description[1]
### Context
Although this dataset was originally contributed to the UCI Machine Learning repository nearly 30 years ago, mushroom hunting (otherwise known as "shrooming") is enjoying new peaks in popularity. Learn which features spell certain death and which are most palatable in this dataset of mushroom characteristics. And how certain can your model be?
Content
This dataset includes descriptions of hypothetical samples corresponding to 23 species of gilled mushrooms in the Agaricus and Lepiota Family Mushroom drawn from The Audubon Society Field Guide to North American Mushrooms (1981). Each species is identified as definitely edible, definitely poisonous, or of unknown edibility and not recommended. This latter class was combined with the poisonous one. The Guide clearly states that there is no simple rule for determining the edibility of a mushroom; no rule like "leaflets three, let it be'' for Poisonous Oak and Ivy.
Time period: Donated to UCI ML 27 April 1987
Inspiration
What types of machine learning models perform best on this dataset?
Which features are most indicative of a poisonous mushroom?

### Acknowledgements
This dataset was originally donated to the UCI Machine Learning repository. 
Number of Instances: 8124
### Attributes
 Number of Attributes: 22 (all nominally valued)
Attribute Information: (classes: edible=e, poisonous=p)
1. cap-shape: bell=b,conical=c,convex=x,flat=f, knobbed=k,sunken=s
2. cap-surface: fibrous=f,grooves=g,scaly=y,smooth=s
3. cap-color: brown=n,buff=b,cinnamon=c,gray=g,green=r,
pink=p,purple=u,red=e,white=w,yellow=y
4. bruises?:bruises=t,no=f
5. odor: almond=a,anise=l,creosote=c,fishy=y,foul=f,
musty=m,none=n,pungent=p,spicy=s
6. gill-attachment: attached=a,descending=d,free=f,notched=n
7. gill-spacing: close=c,crowded=w,distant=d
8. gill-size: broad=b,narrow=n
9. gill-color: black=k,brown=n,buff=b,chocolate=h,gray=g,
green=r,orange=o,pink=p,purple=u,red=e,
white=w,yellow=y
10. stalk-shape: enlarging=e,tapering=t
11. stalk-root: bulbous=b,club=c,cup=u,equal=e,
rhizomorphs=z,rooted=r,missing=?
12. stalk-surface-above-ring: ibrous=f,scaly=y,silky=k,smooth=s
13. stalk-surface-below-ring: ibrous=f,scaly=y,silky=k,smooth=s
14. stalk-color-above-ring:   brown=n,buff=b,cinnamon=c,gray=g,orange=o, pink=p,red=e,white=w,yellow=y
15. stalk-color-below-ring:   brown=n,buff=b,cinnamon=c,gray=g,orange=o,
pink=p,red=e,white=w,yellow=y
16. veil-type: partial=p,universal=u
17. veil-color: brown=n,orange=o,white=w,yellow=y
18. ring-number: none=n,one=o,two=t
19. ring-type: cobwebby=c,evanescent=e,flaring=f,large=l,
none=n,pendant=p,sheathing=s,zone=z
20. spore-print-color: black=k,brown=n,buff=b,chocolate=h,green=r,
orange=o,purple=u,white=w,yellow=y
21. population: abundant=a,clustered=c,numerous=n,
scattered=s,several=v,solitary=y
22. habitat: grasses=g,leaves=l,meadows=m,paths=p,
urban=u,waste=w,woods=d
23.mushroom_class: edible, poisonous
Missing Attribute Values: 2480 of them (denoted by "?"), all for attribute #11.
### Class Distribution
edible: 4208 (51.8%)
poisonous: 3916 (48.2%)
total: 8124 instances

## Students Performance Dataset Description[2]
### Context
This Dataset contains the information about the students and their Performance try to predict using the simple machine Learning Algorithm.
### Content
It contains the Specific information about the Schooling,Family issues,personal Relationship of the students,Internet facility and so on.
### Acknowledgements
This data are gathered from numerous sources thanks a lot @uci_repository.
### Inspiration
Try to find out the issues with the Students as they are future Personalities, to save their Schooling and Youth life.
### Attributes
1. school - student's school (binary: "GP" - Gabriel Pereira or "MS" - Mousinho da Silveira)
2. sex - student's sex (binary: "F" - female or "M" - male)
3. age - student's age (numeric: from 15 to 22)
4. address - student's home address type (binary: "U" - urban or "R" - rural)
5. famsize - family size (binary: "LE3" - less or equal to 3 or "GT3" - greater than 3)
6. Pstatus - parent's cohabitation status (binary: "T" - living together or "A" - apart)
7. Medu - mother's education (numeric: 0 - none,  1 - primary education (4th grade), 2 – 5th to 9th grade, 3 – secondary education or 4 – higher education)
8. Fedu - father's education (numeric: 0 - none,  1 - primary education (4th grade), 2 – 5th to 9th grade, 3 – secondary education or 4 – higher education)
9. Mjob - mother's job (nominal: "teacher", "health" care related, civil "services" (e.g. administrative or police), "at_home" or "other")
10. Fjob - father's job (nominal: "teacher", "health" care related, civil "services" (e.g. administrative or police), "at_home" or "other")
11. reason - reason to choose this school (nominal: close to "home", school "reputation", "course" preference or "other")
12. guardian - student's guardian (nominal: "mother", "father" or "other")
13. traveltime - home to school travel time (numeric: 1 - <15 min., 2 - 15 to 30 min., 3 - 30 min. to 1 hour, or 4 - >1 hour)
14. studytime - weekly study time (numeric: 1 - <2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, or 4 - >10 hours)
15. failures - number of past class failures (numeric: n if 1<=n<3, else 4)
16. schoolsup - extra educational support (binary: yes or no)
17. famsup - family educational support (binary: yes or no)
18. paid - extra paid classes within the course subject (Math or Portuguese) (binary: yes or no)
19. activities - extra-curricular activities (binary: yes or no)
20. nursery - attended nursery school (binary: yes or no)
21. higher - wants to take higher education (binary: yes or no)
22. internet - Internet access at home (binary: yes or no)
23. romantic - with a romantic relationship (binary: yes or no)
24. famrel - quality of family relationships (numeric: from 1 - very bad to 5 - excellent)
25. freetime - free time after school (numeric: from 1 - very low to 5 - very high)
26. goout - going out with friends (numeric: from 1 - very low to 5 - very high)
27. Dalc - workday alcohol consumption (numeric: from 1 - very low to 5 - very high)
28. Walc - weekend alcohol consumption (numeric: from 1 - very low to 5 - very high)
29 .health - current health status (numeric: from 1 - very bad to 5 - very good)
30. absences - number of school absences (numeric: from 0 to 93)

These grades are related with the course subject,Porteguese: </br>
31. G1 - first period grade (numeric: from 0 to 20)  </br>
32. G2 - second period grade (numeric: from 0 to 20) </br>
33. G3 - final grade (numeric: from 0 to 20, output target) </br>
</br> **The 31,32,33th attributes got deleted and a new 31th attribute (pass) is created by using the 33th attribute G3(final score).
The new attribute checks if the student’s score is over the character D (%60) in this situation over 12/20.** </br>
35. pass-student’s passing the class(binary: yes or no) </br>

# CONCLUSION

## Comparing Datasets
By data size, the Mushroom Dataset is a lot larger than Student Performance Dataset. Student Performance Dataset, on the other hand, has 8 more attributes than Mushroom Dataset. In contrast to the Mushroom Dataset, the Student Performance Dataset contains missing values; nonetheless, these missing values are insignificant in terms of the dataset. Both datasets are balanced in terms of class types.

## Comparing Algorithms Accuracy
Since both datasets are balanced, we can be sure of their accuracy. If they weren't balanced, we could look at the F-measure, which is the harmonic mean of Precision and Recall. Alternatively, you can use a weighted f-measure to balance the weight between Precision and Recall.


J48 and IBK are the two highest scoring algorithms in the Mushroom Dataset, both with 100 percent accuracy. Normally, 100 % accuracy indicates overfitting (the model memorizes values), which is undesirable, but when stratified cross-validation is applied, it is fair to believe that these methods work perfectly and do not overfit. </br>
The best algorithm for the Students Performance Dataset is Nave Bayes.</br>
J48, IBK, and OneR follow Naïve Bayes with similar scores among themselves.
The reason why Nave Bayes scored best on the Student's Performance Dataset and lowest on the Mushroom Dataset is that Bayesian classifiers perform better on larger datasets. However, naive Bayes assumes that attributes are independent, and if they are dependent, the model's accuracy drops. There are more attributes in the Student's Performance Dataset, and these attributes are mainly independent (except income-related attributes, they are dependent). However, it is safe to presume that the features of the Mushroom Dataset are much more closely related (gill related and stalk related multiple attributes exist). </br>
Because J48 is a decision tree classifier, it performed second best on the Students Performance Dataset. With smaller datasets, decision trees perform better. Decision trees also outperform other models when it comes to categorical values. Whereas other models cannot detect patterns between categorical values, decision trees can. .</br>
Because it is a rule-based classifier, OneR performs similarly but slightly worse than the J48. Decision trees are quite similar to rule-based classifiers (you can also convert trees to rules). Rule-based classifiers provide rules that classify data, and these rules are much easier for people to understand but perform worse (larger the tree, it gets harder to understand by humans). </br>

## Comparing Model Build Time
The IBK algorithm is a lazy learner algorithm that does not require model development (it stores training data), which explains why creating the model for both datasets takes zero seconds. </br>
Bayesian classifiers have high speed on huge datasets. As a result, Nave Bayes performs second fastest on the mushroom dataset.
However, Nave Bayes performs significantly worse on the Students Performance Dataset because, while being smaller, it contains more attributes. .</br>
The Mushroom Dataset is large,and J48 and OneR both have the same build time, but for students performance dataset (which is a smaller dataset), OneR is clearly faster. Which makes sense because we know it is less accurate in comparison to J48 from the "Comparing Accuracy Algorithms Accuracy" table. .</br>


# REFERENCES
[1]UCI Machine Learning,(2017), Mushroom Classification
[https://www.kaggle.com/uciml/mushroom-classification]
[2]Bala Vashan,(Last Update 31,12,2021),Students Performance Dataset
[https://www.kaggle.com/balavashan/students-performance-dataset?select=student-por.csv]
[3]renatopp,(20 December 2012), arff-datasets
[https://github.com/renatopp/arff-datasets/tree/master/classification]
[4]Weka wiki,(view 2 January 2022), weka-wiki
[https://waikato.github.io/weka-wiki]
