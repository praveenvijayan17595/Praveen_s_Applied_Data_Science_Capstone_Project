#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip3 install beautifulsoup4')
get_ipython().system('pip3 install requests')


# In[2]:


import sys
import requests
from bs4 import BeautifulSoup
import re
import unicodedata
import pandas as pd


# In[54]:


def date_time(table_cells):
    return [datetime.strip() for datetime in list(table_cells.strings)][0:2]


# In[55]:


def booster_version(table_cells):
    out=''.join([booster_version for i, booster_version in enumerate(table_cells.strings) if i%2==0][0:-1])
    return out


# In[56]:


def landing_status(table_cells):
    out=[i for i in table_cells.strings][0]
    return out


# In[57]:


def get_mass(table_cells):
    mass=unicodedata.normalize('NFKD',table_cells.text).strip()
    if mass:
        mass.find('kg')
        new_mass=mass[0:mass.find('kg')+2]
    else:
        new_mass=0
    return new_mass


# In[58]:


def extract_column_from_header(row):
    if row.br:
        row.br.extract()
    if row.a:
        row.a.extract()
    if row.sup:
        row.sup.extract()
    column_name=' '.join(row.contents)
    
    if not(column_name.strip().isdigit()):
        column_name=column_name.strip()
        return column_name


# In[59]:


static_url = "https://en.wikipedia.org/w/index.php?title=List_of_Falcon_9_and_Falcon_Heavy_launches&oldid=1027686922"


# In[60]:


data=requests.get(static_url).text


# In[61]:


soup=BeautifulSoup(data,'html5lib')


# In[62]:


print(soup.title)


# In[63]:


html_tables=soup.find_all('table')


# In[64]:


first_launch_table=html_tables[2]
print(first_launch_table)


# In[65]:


column_names=[]
for row in first_launch_table.find_all('th'):
    name=extract_column_from_header(row)
    if (name!=None and len(name)>0):
        column_names.append(name)


# In[66]:


column_names


# In[67]:


launch_dict=dict.fromkeys(column_names)


# In[68]:


del launch_dict['Date and time ( )']
launch_dict['Flight No.'] = []
launch_dict['Launch site'] = []
launch_dict['Payload'] = []
launch_dict['Payload mass'] = []
launch_dict['Orbit'] = []
launch_dict['Customer'] = []
launch_dict['Launch outcome'] = []
# Added some new columns
launch_dict['Version Booster']=[]
launch_dict['Booster landing']=[]
launch_dict['Date']=[]
launch_dict['Time']=[]


# In[69]:


launch_dict


# In[70]:


extracted_row = 0
#Extract each table 
for table_number,table in enumerate(soup.find_all('table',"wikitable plainrowheaders collapsible")):
   # get table row 
    for rows in table.find_all("tr"):
        #check to see if first table heading is as number corresponding to launch a number 
        if rows.th:
            if rows.th.string:
                flight_number=rows.th.string.strip()
                flag=flight_number.isdigit()
        else:
            flag=False
        #get table element 
        row=rows.find_all('td')
        #if it is number save cells in a dictonary 
        if flag:
            extracted_row += 1
            # Flight Number value
            # TODO: Append the flight_number into launch_dict with key `Flight No.`
            launch_dict['Flight No.'].append(flight_number) #TODO-1
            #print(flight_number)
            datatimelist=date_time(row[0])
            
            # Date value
            # TODO: Append the date into launch_dict with key `Date`
            date = datatimelist[0].strip(',')
            launch_dict['Date'].append(date) #TODO-2
            #print(date)
            
            # Time value
            # TODO: Append the time into launch_dict with key `Time`
            time = datatimelist[1]
            launch_dict['Time'].append(time) #TODO-3
            #print(time)
              
            # Booster version
            # TODO: Append the bv into launch_dict with key `Version Booster`
            bv=booster_version(row[1])
            if not(bv):
                bv=row[1].a.string
            launch_dict['Version Booster'].append(bv) #TODO-4
            #print(bv)
            
            # Launch Site
            # TODO: Append the bv into launch_dict with key `Launch site`
            launch_site = row[2].a.string
            launch_dict['Launch site'].append(launch_site) #TODO-5
            #print(launch_site)
            
            # Payload
            # TODO: Append the payload into launch_dict with key `Payload`
            payload = row[3].a.string
            launch_dict['Payload'].append(payload) #TODO-6
            #print(payload)
            
            # Payload Mass
            # TODO: Append the payload_mass into launch_dict with key `Payload mass`
            payload_mass = get_mass(row[4])
            launch_dict['Payload mass'].append(payload_mass) #TODO-7
            #print(payload)
            
            # Orbit
            # TODO: Append the orbit into launch_dict with key `Orbit`
            orbit = row[5].a.string
            launch_dict['Orbit'].append(orbit) #TODO-8
            #print(orbit)
            
            # Customer
            # TODO: Append the customer into launch_dict with key `Customer`
            customer = row[6].text.strip()
            launch_dict['Customer'].append(customer) #TODO-9
            #print(customer)
            
            # Launch outcome
            # TODO: Append the launch_outcome into launch_dict with key `Launch outcome`
            launch_outcome = list(row[7].strings)[0]
            launch_dict['Launch outcome'].append(launch_outcome) #TODO-10
            #print(launch_outcome)
            
            # Booster landing
            # TODO: Append the launch_outcome into launch_dict with key `Booster landing`
            booster_landing = landing_status(row[8])
            launch_dict['Booster landing'].append(booster_landing) #TODO-11
            #print(booster_landing)


# In[71]:


df=pd.DataFrame(launch_dict)


# In[72]:


df


# In[73]:


df.to_csv('spacex_web_scraped.csv', index=False)


# In[ ]:




