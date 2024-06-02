#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier


# In[2]:


def plot_confusion_matrix(y,y_predict):
    from sklearn.metrics import confusion_matrix
    
    cm=confusion_matrix(y,y_predict)
    ax=plt.subplot()
    sns.heatmap(cm,annot=True,ax=ax)
    ax.set_xlabel('Predicted labels')
    ax.set_ylabel('Actual labels')
    ax.set_title('Confusion Matrix')
    ax.xaxis.set_ticklables(['did not land','land']);ax.yaxis.set_ticklabels(['did not land','land'])


# In[3]:


#load the data
data=pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_2.csv')
data.head()


# In[4]:


X = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_3.csv')
X.head()


# In[5]:


#Task 1
Y=data["Class"].to_numpy()
Y


# In[6]:


#task 2
transform=preprocessing.StandardScaler()


# In[7]:


X


# In[8]:


X=transform.fit_transform(X)
X


# In[9]:


#task 3
X_train, X_test, Y_train, Y_test= train_test_split(X, Y, test_size=0.2, random_state=2)


# In[10]:


Y_train.shape


# In[11]:


parameters={"C":[0.01,0.1,1],'penalty':['l2'],'solver':['lbfgs']}
lr=LogisticRegression()
logreg_cv=GridSearchCV(lr,parameters,cv=10)
logreg_cv.fit(X_train,Y_train)


# In[12]:


print("tuned hyperparameters:(best parameters)",logreg_cv.best_params_)
print("accuracy:",logreg_cv.best_score_)


# In[13]:


logreg_cv.score(X_test,Y_test)


# In[14]:


yhat=logreg_cv.predict(X_test)
plot_confusion_matrix(Y_test,yhat)


# In[15]:


parameters={'kernel':('linear','rbf','poly','rbf','sigmoid'),
           'C':np.logspace(-3,3,5),
            'gamma':np.logspace(-3,3,5)}
svm=SVC()


# In[16]:


svm_cv=GridSearchCV(svm,parameters,cv=10)
svm_cv.fit(X_train,Y_train)


# In[17]:


print("tuned hyperprameters:(best parameters) :",svm_cv.best_params_)
print("accuracy :",svm_cv.best_score_)


# In[18]:


svm_cv.score(X_test,Y_test)


# In[19]:


yhat=svm_cv.predict(X_test)
plot_confusion_matrix(Y_test,yhat)


# In[20]:


parameters = {'criterion': ['gini', 'entropy'],
     'splitter': ['best', 'random'],
     'max_depth': [2*n for n in range(1,10)],
     'max_features': ['auto', 'sqrt'],
     'min_samples_leaf': [1, 2, 4],
     'min_samples_split': [2, 5, 10]}

tree=DecisionTreeClassifier()


# In[22]:


tree_cv = GridSearchCV(tree, parameters, cv=10)

# Fit it to the data
tree_cv.fit(X_train, Y_train)


# In[23]:


print("tuned hyperparameters:(best parameters)",tree_cv.best_params_)
print("accuracy:",tree_cv.best_score_)


# In[24]:


tree_cv.score(X_test,Y_test)


# In[25]:


yhat=tree_cv.predict(X_test)
plot_confusion_matrix(Y_test,yhat)


# In[26]:


parameters = {'n_neighbors': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
              'algorithm': ['auto', 'ball_tree', 'kd_tree', 'brute'],
              'p': [1,2]}

KNN=KNeighborsClassifier()


# In[28]:


knn_cv=GridSearchCV(KNN,parameters,cv=10)

knn_cv.fit(X_train, Y_train)


# In[29]:


print("tuned hyperparameters:(best parameters)",knn_cv.best_params_)
print("Accuracy:",knn_cv.best_score_)


# In[30]:


knn_cv.score(X_test,Y_test)


# In[31]:


yhat=knn_cv.predict(X_test)
plot_confusion_matrix(Y_test,yhat)


# In[35]:


predictors = [knn_cv, svm_cv, logreg_cv, tree_cv]
best_predictor = ""
best_result = 0
for predictor in predictors:
    
    predictor.score(X_test, Y_test)


# In[ ]:




