#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns  


# In[2]:


df=pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_2.csv")
df


# In[3]:


sns.catplot(y="PayloadMass",x="FlightNumber",hue="Class",data=df,aspect=5)
plt.xlabel("Flight Number",fontsize=20)
plt.ylabel("Payload Mass KG",fontsize=20)
plt.show()


# In[4]:


sns.catplot(y="LaunchSite",x="FlightNumber",hue="Class",data=df,aspect=5)
plt.xlabel("Flight Number",fontsize=20)
plt.ylabel("Launch Site",fontsize=20)
plt.show()


# In[5]:


sns.catplot(x="PayloadMass",y="LaunchSite",hue="Class",data=df)
plt.xlabel("Payload Mass KG",fontsize=10)
plt.ylabel("Launch Site",fontsize=10)
plt.show()


# In[6]:


t=df.groupby(['Orbit','Class'])['Class'].agg(['mean']).reset_index()


# In[7]:


t


# In[8]:


sns.barplot(y="Class",x="Orbit",data=t)
plt.xlabel("Orbit",fontsize=20)
plt.ylabel("Class",fontsize=20)
plt.show()


# In[9]:


sns.catplot(x="FlightNumber",y="Orbit",hue="Class",data=df)
plt.xlabel("Flight number")
plt.ylabel("Orbit")
plt.show()


# In[17]:


sns.catplot(x="PayloadMass",y="Orbit",hue="Class",data=df)
plt.xlabel("Mass")
plt.ylabel("Orbit")
plt.show()


# In[10]:


sns.catplot(y="Orbit",x="PayloadMass",hue="Class",data=df)
plt.xlabel("Payload")
plt.ylabel("Orbit")
plt.show()


# In[11]:


def Extract_year():
    for i in df["Date"]:
        year.append(i.split("-")[0])
    return year


# In[12]:


year=[]
df1=df.copy()
year=Extract_year()
df1["Date"]=year
df1.head()


# In[13]:


sns.lineplot(data=df1, x="Date", y="Class")
plt.xlabel("Date")
plt.ylabel("Success Rate")
plt.show()


# In[14]:


features = df[['FlightNumber', 'PayloadMass', 'Orbit', 'LaunchSite', 'Flights', 'GridFins', 'Reused', 'Legs', 'LandingPad', 'Block', 'ReusedCount', 'Serial']]
features.head()


# In[15]:


features_one_hot=pd.get_dummies(features,columns=['Orbit', 'LaunchSite', 'LandingPad', 'Serial'])
features_one_hot.head()


# In[16]:


features_one_hot.astype(float)


# In[17]:


features_one_hot.to_csv('dataset_part3.csv', index=False)


# In[ ]:




