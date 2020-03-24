import pandas as pd
import googlemaps as maps

towns_df = pd.read_csv('New Jersey Diners - Towns Profiles.csv', header=0)
towns_df.drop(columns=['LONGITUDE', 'LATITUDE'])
central_df_towns = towns_df[towns_df['REGION']=='CENTRAL']['TOWNS']
central_df_zipcode = towns_df[towns_df['REGION']=='CENTRAL']['ZIPCODE']
print(central_df_zipcode)

def geocoder(zip):
  gmaps = maps.Client(key='AIzaSyA9jKRCNusg0gGVUS5LpauQicua0DDLDjg')
  geocode_result = gmaps.geocode("0"+str(zip))[0]
  geometry = geocode_result['geometry']
  location = geometry['location']
  return location

def latitude(zip):
  lat = geocoder(zip)['lat']

  return lat

def longitude(zip):
  lng = geocoder(zip)['lng']

  return lng


n = 20  #chunk row size
batch_df = [towns_df[i:i+n] for i in range(0,towns_df.shape[0],n)]
def batch_processor_lat(i):
  batch_n = batch_df[i]
  zipcode_batch_n = batch_n['ZIPCODE']
  batch_n_lat = zipcode_batch_n.apply(latitude)
  return batch_n_lat

def batch_processor_lng(i):
  batch_n = batch_df[i]
  zipcode_batch_n = batch_n['ZIPCODE']
  batch_n_lng = zipcode_batch_n.apply(longitude)
  return batch_n_lng


def batch_dataframe(i):
  lat = batch_processor_lat(i)
  lng = batch_processor_lng(i)
  data = {'LATITUDE': lat,'LONGITUDE': lng}
  batch_df = pd.DataFrame(data)

  return batch_df
