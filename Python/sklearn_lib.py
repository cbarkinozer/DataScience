#Scikit-learn

#Loading iris from scikit-learn
from sklearn.datasets import load_iris

X,y = load_iris(return_X_y=True)
#Just include first 2 attributes
X=X[:,:2]

print(f'First 5 samples in X: \n{X[:5]}')
print(f'Labels:\n{y}')
print()

#Estimators
#Estimators are algorithm implementations

from sklearn.tree import DecisionTreeClassifier,DecisionTreeRegressor
from sklearn.neighbors import KNeighborsClassifier,KNeighborsRegressor
from sklearn.ensemble import RandomForestClassifier,GradientBoostingRegressor
from sklearn.svm import SVC,SVR
from sklearn.linear_model import LinearRegression, LogisticRegression

model= KNeighborsClassifier(n_neighbors=5)
print(model)

#Training a model

#create the model
model= KNeighborsClassifier(n_neighbors=5)

#Fit data to the model
model.fit(X,y)

#Get predictions from the model
y_pred=model.predict(X)

print(y_pred)

#DecisionTreeClassifier
from sklearn.tree import DecisionTreeClassifier
clf= DecisionTreeClassifier(max_depth=2)
clf.fit(X,y)
clf_pred=clf.predict(X)
print(clf_pred)

#Classification metrics
from sklearn.metrics import(accuracy_score,precision_score,
                            recall_score,f1_score,log_loss)
#Regression metrics
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score

y_pred=[0,2,1,3,1]
y_true=[0,1,1,3,2]

print("Accuracy score ",accuracy_score(y_true,y_pred))
print("Mean squared error", mean_squared_error(y_true,y_pred))


#Seperating training and testing sets
from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X,y,
                                                 test_size=0.2,
                                                 random_state=2)
print(f'X.shape={X.shape}')
print(f'X_test.shape={X_test.shape}')
print(f'X_train.shape={X_train.shape}')
print()

clf=DecisionTreeClassifier()
clf.fit(X_train,y_train)
print(f'training accuracy = {accuracy_score(y_train,clf.predict(X_train))}')
print(f'testing accuracy={accuracy_score(y_test,clf.predict(X_test))}')
print()


#Corssvalidation
from sklearn.model_selection import cross_validate

clf= DecisionTreeClassifier(max_depth=2)

scores=cross_validate(clf,X_train,y_train,
                      scoring='accuracy',cv=10,
                      return_train_score=True)
print(scores.keys())
test_scores=scores['test_score']
train_scores=scores['train_score']
print(test_scores)
print(train_scores)
print()

import numpy as np
print('\n10-fold CV scores:')
print(f'training score={np.mean(train_scores)} +/- {np.std(train_scores)}')
print(f'validation score={np.mean(test_scores)} +/-{np.std(test_scores)}')
print()

#GridSearchCv optimizes hyperparameters by scaning all combinations

from sklearn.model_selection import GridSearchCV

#Model
clf=DecisionTreeClassifier()

#Hyperparameters
parameters={'max_depth':range(1,20),
            'criterion':['gini','entropy']}

#Run grid search
gridsearch= GridSearchCV(clf,parameters, scoring='accuracy',cv=10)
gridsearch.fit(X_train,y_train)

#Get best model
print(f'gridsearch.best_params_={gridsearch.best_params_}')
print(gridsearch.best_estimator_)
print()


#Supervised Machine Learning Workflow
#Seperate training and test sets
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=2)

#Optimize hyperparameters via crossvalidation
#model
clf=DecisionTreeClassifier()
#parameters
parameters={'max_depth':range(1,20),
            'criterion':['gini','entropy']}
gridsearch= GridSearchCV(clf,parameters,scoring='accuracy',cv=10)
gridsearch.fit(X_train,y_train)
print(f'gridsearch.best_params_={gridsearch.best_params_}')

best_clf=gridsearch.best_estimator_
print(best_clf)
print()

#Model Performance
y_pred=best_clf.predict(X_test)
test_acc=accuracy_score(y_test,y_pred)
print(f'test_acc={test_acc}')

#Train final model on full dataset

final_model=DecisionTreeClassifier(**gridsearch.best_params_)
final_model.fit(X,y)
final_model.predict(X)
print(accuracy_score(y_test,y_pred))

#Iris classificaiton problem

#Get training and testing datasets
X_train,X_test,y_train,y_test= train_test_split(X,y,test_size=0.3,random_state=2)

#Use GridSearchCV to find optimal hyperparameters
clf=DecisionTreeClassifier(random_state=2)
parameters={'max_depth':range(1,20),
            'criterion':['gini','entropy']}

gridsearch=GridSearchCV(clf,parameters,scoring='accuracy',cv=10)
gridsearch.fit(X_train,y_train)
print(gridsearch.best_params_)

#Get model with hyperparameters
best_clf=gridsearch.best_estimator_

#Get best model performance
y_pred=best_clf.predict(X_test)
test_acc=accuracy_score(y_test,y_pred)
print(test_acc)

#Train final model on full dataset
final_model=DecisionTreeClassifier(random_state=2,**gridsearch.best_params_)
final_model.fit(X,y)

#Exercise
#Dataset:Iris,Model:Knn,Parameters:n_neighbors:1-10,weights:uniform,distance
#Find optimum hyperparameters using GridSearchCV
#Train-test split 0.8-0.2
#Print best model
#Print accuracy score

from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X,y=load_iris(return_X_y=True)

X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=2,test_size=0.2)
knn=KNeighborsClassifier()
parameters={'n_neighbors':range(1,10),
            'weights':['uniform','distance']}
gridsearch=GridSearchCV(knn,parameters,scoring='accuracy',cv=10)
gridsearch.fit(X_train,y_train)

best_knn=gridsearch.best_estimator_
print(best_knn)
print()

y_pred=best_knn.predict(X_test)
test_acc=accuracy_score(y_test,y_pred)
print(test_acc)
print()
