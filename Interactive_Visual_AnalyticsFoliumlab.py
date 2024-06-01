#!/usr/bin/env python
# coding: utf-8

# In[1]:


import folium
import pandas as pd


# In[2]:


from folium.plugins import MarkerCluster
from folium.plugins import MousePosition
from folium.features import DivIcon


# In[4]:


spacex_csv_file = wget.download('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_geo.csv')
spacex_df=pd.read_csv(spacex_csv_file)


# In[3]:


import wget


# In[5]:


spacex_df.head()


# In[6]:


spacex_df=spacex_df[['Launch Site', 'Lat', 'Long', 'class']]


# In[7]:


spacex_df.head()


# In[8]:


lau=spacex_df.groupby(['Launch Site']).first()
lau.head()


# In[ ]:





# In[9]:


launch_sites_df=spacex_df.groupby(['Launch Site'], as_index=False).first()
launch_sites_df=launch_sites_df[['Launch Site', 'Lat', 'Long']]
launch_sites_df


# In[10]:


nasa_coordinate = [29.559684888503615, -95.0830971930759]
site_map=folium.Map(location=nasa_coordinate, zoom_start=10)


# In[11]:


site_map


# In[12]:


circle=folium.Circle(nasa_coordinate,radius=1000,color='#d35400',fill=True).add_child(folium.Popup('Nasa Jhonson Space Center'))
marker = folium.map.Marker(
    nasa_coordinate,
    # Create an icon as a text label
    icon=DivIcon(
        icon_size=(20,20),
        icon_anchor=(0,0),
        html='<div style="font-size: 12; color:#d35400;"><b>%s</b></div>' % 'NASA JSC',
        )
    )
site_map.add_child(circle)
site_map.add_child(marker)


# In[13]:


site_map=folium.Map(location=nasa_coordinate,zoom_start=5)
lats_longs=list(zip(list(launch_sites_df['Lat']),list(launch_sites_df['Long'])))
locations=list(launch_sites_df['Launch Site'])

for i in range(0,len(locations)):
    circle = folium.Circle(lats_longs[i], radius=1000, color='#d35400', fill=True).add_child(folium.Popup(f'{locations[i]}'))
    # Create a blue circle at NASA Johnson Space Center's coordinate with a icon showing its name
    marker = folium.map.Marker(
        nasa_coordinate,
        # Create an icon as a text label
        icon=DivIcon(
            icon_size=(20,20),
            icon_anchor=(0,0),
            html='<div style="font-size: 12; color:#d35400;"><b>%s</b></div>' % f'Location',
            )
        )
    site_map.add_child(circle)
    site_map.add_child(marker)


# In[14]:


site_map


# In[15]:


spacex_df.tail(10)


# In[16]:


marker_cluster=MarkerCluster()


# In[17]:


def assign_marker_color(launch_outcome):
    if launch_outcome==1:
        return 'green'
    else:
        return 'red'


# In[18]:


spacex_df['marker_color']=spacex_df['class'].apply(lambda x:'red' if x==0 else 'green')
spacex_df.tail(10)


# In[19]:


site_map.add_child(marker_cluster)

for index, record in spacex_df.iterrows():
    marker=folium.Marker([record['Lat'],record['Long']],
                        icon=folium.Icon(color='white',icon_color=record['marker_color']))
    marker_cluster.add_child(marker)
site_map


# In[20]:


formatter = "function(num) {return L.Util.formatNum(num, 5);};"
mouse_position = MousePosition(
    position='topright',
    seperator='Long: ',
    empty_string='Nan',
    lng_first=False,
    num_digits=20,
    prefix='Lat: ',
    lat_formatter=formatter,
    lng_formatter=formatter,
)
site_map.add_child(mouse_position)
site_map


# In[21]:


from math import sin, cos, sqrt, atan2, radians

def calculate_distance(lat1, lon1, lat2, lon2):
    # approximate radius of earth in km
    R = 6373.0

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance


# In[22]:


distance_railway=calculate_distance(28.56321, -80.57684, 28.57146, -80.58535)


# In[23]:


distance_railway


# In[24]:


coordinates = [
    [28.56342, -80.57674],
    [28.56342, -80.56756]]

lines=folium.PolyLine(locations=coordinates, weight=1)
site_map.add_child(lines)
distance = calculate_distance(coordinates[0][0], coordinates[0][1], coordinates[1][0], coordinates[1][1])
distance_circle = folium.Marker(
    [28.56342, -80.56794],
    icon=DivIcon(
        icon_size=(20,20),
        icon_anchor=(0,0),
        html='<div style="font-size: 12; color:#d35400;"><b>%s</b></div>' % "{:10.2f} KM".format(distance),
        )
    )
site_map.add_child(distance_circle)
site_map


# In[25]:


distance


# In[29]:


coordinates = [
    [28.56342, -80.57674],
    [28.56342, -80.56756]]

lines=folium.PolyLine(locations=coordinates,weight=1)
site_map.add_child(lines)
distance=calculate_distance(coordinates[0][0],coordinates[0][1],coordinates[1][0],coordinates[1][1])
distance_circle=folium.Marker(
    [28.56342, -80.56794],
    icon=DivIcon(
    icon_size=(20,20),
    icon_anchor=(0,0),
    html='<div style="font size: 12; color:#d35400;"><b>%s</b></div>' % "{:10.2f} KM".format(distance),))
site_map.add_child(distance_circle)
site_map


# In[32]:


distance_circle=folium.Marker(
    [28.56342, -80.56794],
    icon=DivIcon(
    icon_size=(20,20),
    icon_anchor=(0,0),
    html='<div style="font size: 12; color:#d35400;"><b>%s</b></div>' % "{:10.2f} KM".format(distance),))
site_map.add_child(distance_circle)
site_map

distance_circle=folium.Marker(
    [28.56342, -80.56794],
    icon=DivIcon(
    icon_size=(20,20),
    icon_anchor=(0,0),
    html='<div style="font size: 12; color:#d35400;"><b>%s</b></div>' % "{:10.2f} KM".format(distance)))

html='<div style="font size=12; color:#d35400;"<b>%s</b></div>' % "{:10.2f} KM".format(distance)))
site_map.add_child(distance_circle)
site_map


# In[33]:


coordinates = [
    [28.56342, -80.57674],
    [28.411780, -80.820630]]

lines=folium.PolyLine(locations=coordinates, weight=1)
site_map.add_child(lines)
distance = calculate_distance(coordinates[0][0], coordinates[0][1], coordinates[1][0], coordinates[1][1])
distance_circle = folium.Marker(
    [28.411780, -80.820630],
    icon=DivIcon(
        icon_size=(20,20),
        icon_anchor=(0,0),
        html='<div style="font-size: 12; color:#252526;"><b>%s</b></div>' % "{:10.2f} KM".format(distance),
        )
    )
site_map.add_child(distance_circle)
site_map


# In[35]:


coordinates = [
    [28.56342, -80.57674],
    [28.5383, -81.3792]]

lines=folium.PolyLine(locations=coordinates, weight=1)
site_map.add_child(lines)
distance=calculate_distance(coordinates[0][0],coordinates[0][1],coordinates[1][0],coordinates[1][1])
distance_circle=folium.Marker(
    [28.5383, -81.3792],
    icon=DivIcon(
    icon_size=(20,20),
    icon_anchor=(0,0),
    html='<div style="font size=12; color=#d252526;"<b>%s</b></div>' % "{:10.2f} KM".format(distance)))
site_map.add_child(distance_circle)
site_map


# In[ ]:




