#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df=pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_1.csv")
df.head(10)


# In[6]:


df.isnull().sum()/df.count()*100


# In[9]:


df.dtypes


# In[11]:


df.LaunchSite.value_counts()


# In[12]:


df.Orbit.value_counts()


# In[14]:


landing_outcomes=df.Outcome.value_counts()
landing_outcomes


# In[18]:


for i,outcome in enumerate(landing_outcomes.keys()):
    print(i,outcome)


# In[19]:


bad_outcomes=set(landing_outcomes.keys()[[1,3,5,6,7]])
bad_outcomes


# In[23]:


landing_class = df['Outcome'].replace({'False Ocean': 0, 'False ASDS': 0, 'None None': 0, 'None ASDS': 0, 'False RTLS': 0, 'True ASDS': 1, 'True RTLS': 1, 'True Ocean': 1}, inplace = True)
df['Outcome'] = df['Outcome'].astype(int)
df.info()


# In[26]:


df['Class']=df['Outcome']
df['Class'].head(8)


# In[27]:


df.head(5)


# In[28]:


df['Class'].mean()


# In[29]:


df.to_csv("dataset_part_2.csv", index=False)


# In[ ]:




