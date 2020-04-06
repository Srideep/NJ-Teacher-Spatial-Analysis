import pandas as pd
from pandas.io.json import json_normalize

#counties_df = pd.read_csv('NJ County Profiles.csv',header=0)
teachers_df = pd.read_csv('nj_teachers_profiles.csv', header=0)
towns_df = pd.read_csv('nj_town_profiles.csv',header=0)
us_states_dict = pd.read_json('us_states.json', orient='records')
us_states_json = pd.json_normalize(us_states_dict['features'],  max_level=3)
state_df = {'GEO ID': us_states_json['properties.GEO_ID'], 
     'STATE_ID': us_states_json['properties.STATE'], 
     'STATE_NAME':us_states_json['properties.NAME'],      
     'AREA':us_states_json['properties.CENSUSAREA'], 
     'STATE GEOMETRY':us_states_json['geometry.type'],
     'STATE Coordinates': us_states_json['geometry.coordinates']}
us_states_df = pd.DataFrame(data=state_df)
nj_df = us_states_df.query('STATE_NAME == "New Jersey"')
print(" ")
print('Loading NJ Counties data')
print(" ")
#print(counties_df.head(3))
print(" ")
print('Loading NJ Teachers data')
print(" ")
print(teachers_df.head(3))
print(" ")
print('Loading NJ Towns data')
print(" ")
print(towns_df.head(3))
print(" ")
print('Loading New Jersey State Geo data')
print(" ")
print(nj_df)