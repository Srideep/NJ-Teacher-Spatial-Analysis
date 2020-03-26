import pandas as pd

counties_df = pd.read_csv('NJ County Profiles.csv', header=0)
teachers_df = pd.read_csv('NJ Teachers Salaries 2016.csv', header=0)
towns_df = pd.read_csv('NJ Towns Profiles.csv',header=0)

print(" ")
print('Loading NJ Counties data')
print(" ")
print(counties_df.head(3))
print(" ")
print('Loading NJ Teachers data')
print(" ")
print(teachers_df.head(3))
print(" ")
print('Loading NJ Towns data')
print(" ")
print(towns_df.head(3))