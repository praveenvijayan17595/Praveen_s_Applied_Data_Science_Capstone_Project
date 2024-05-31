#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd
import numpy as np
import datetime
pd.set_option('display.max_columns',None)
pd.set_option('display.max_colwidth',None)


# In[2]:


def getBoosterVersion(data):
    for x in data['rocket']:
        if x:
            response=requests.get("https://api.spacexdata.com/v4/rockets/"+str(x)).json()
            BoosterVersion.append(response['name'])


# In[3]:


def getLaunchSite(data):
    for x in data['launchpad']:
        if x:
            response=requests.get("https://api.spacexdata.com/v4/launchpads/"+str(x)).json()
            Longitude.append(response['longitude'])
            Latitude.append(response['latitude'])
            LaunchSite.append(response['name'])


# In[4]:


def getPayLoadData(data):
    for x in data['payloads']:
        if x:
            response=requests.get("https://api.spacexdata.com/v4/payloads/"+x).json()
            PayloadMass.append(response['mass_kg'])
            Orbit.append(response['orbit'])


# In[5]:


# Takes the dataset and uses the cores column to call the API and append the data to the lists
def getCoreData(data):
    for core in data['cores']:
            if core['core'] != None:
                response = requests.get("https://api.spacexdata.com/v4/cores/"+core['core']).json()
                Block.append(response['block'])
                ReusedCount.append(response['reuse_count'])
                Serial.append(response['serial'])
            else:
                Block.append(None)
                ReusedCount.append(None)
                Serial.append(None)
            Outcome.append(str(core['landing_success'])+' '+str(core['landing_type']))
            Flights.append(core['flight'])
            GridFins.append(core['gridfins'])
            Reused.append(core['reused'])
            Legs.append(core['legs'])
            LandingPad.append(core['landpad'])


# In[6]:


spacex_url="https://api.spacexdata.com/v4/launches/past"
response=requests.get(spacex_url)


# In[7]:


print(response.content)


# In[8]:


static_json_url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/API_call_spacex_api.json"


# In[9]:


response2=requests.get(static_json_url)


# In[10]:


USE_STATIC_RESULT = True

if USE_STATIC_RESULT:
    import json
    data = pd.json_normalize(response2.json())
else:
    data = pd.json_normalize(response.json())


# In[11]:


data.head()


# In[12]:


data=data[['rocket', 'payloads', 'launchpad', 'cores', 'flight_number', 'date_utc']]


# In[13]:


data=data[data['cores'].map(len)==1]


# In[14]:


data=data[data['payloads'].map(len)==1]


# In[15]:


data['cores'] = data['cores'].map(lambda x : x[0])


# In[16]:


data['payloads']=data['payloads'].map(lambda x : x[0])


# In[17]:


data.head()


# In[18]:


data['date']=pd.to_datetime(data['date_utc']).dt.date


# In[19]:


data=data[data['date']<=datetime.date(2020,11,13)]


# In[20]:


data.head()


# In[21]:


#Global variables 
BoosterVersion = []
PayloadMass = []
Orbit = []
LaunchSite = []
Outcome = []
Flights = []
GridFins = []
Reused = []
Legs = []
LandingPad = []
Block = []
ReusedCount = []
Serial = []
Longitude = []
Latitude = []


# In[22]:


BoosterVersion


# In[23]:


getBoosterVersion(data)


# In[24]:


BoosterVersion[0:5]


# In[25]:


getLaunchSite(data)


# In[26]:


LaunchSite[0:5]


# In[27]:


getPayLoadData(data)


# In[28]:


getCoreData(data)


# In[43]:


CoreData


# In[30]:


launch_dict={'FlightNumber':list(data['flight_number']),
'Date':list(data['date']),
'BoosterVersion':BoosterVersion,
'PayloadMass':PayloadMass,
'Orbit':Orbit,
'LaunchSite':LaunchSite,
'Outcome':Outcome,
'Flights':Flights,
'GridFins':GridFins,
'Reused':Reused,
'Legs':Legs,
'LandingPad':LandingPad,
'Block':Block,
'ReusedCount':ReusedCount,
'Serial':Serial,
'Longitude': Longitude,
'Latitude': Latitude}


# In[31]:


data2=pd.DataFrame(launch_dict)


# In[32]:


data2.head()


# In[35]:


data_falcon9=data2.loc[data2['BoosterVersion']!='Falcon 1']


# In[36]:


data_falcon9


# In[49]:


data_falcon9.loc[:,'FlightNumber']=list(range(1,data_falcon9.shape[0]+1))
data_falcon9.head()


# In[42]:


data_falcon9.isnull().sum()


# In[44]:


meanpayloadmass=data_falcon9['PayloadMass'].mean()
data_falcon9.loc[data_falcon9['PayloadMass'].isnull(),['PayloadMass']]=meanpayloadmass


# In[45]:


data_falcon9.isnull().sum()


# In[48]:


data_falcon9.to_csv('data_falcon9.csv',index=False)


# In[ ]:




