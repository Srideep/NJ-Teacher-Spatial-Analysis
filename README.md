# NJ Teachers Graph DataBase 
This repo will be used to do CRUD operations on building a graph database for sample New Jersey based Teachers and their info using Neo4j database hosted in cloud. 
- CSV files containing County, Town and Teacher information is used to load , clean and insert/update in the database.
- Geocoding Information where needed is generated using Mapbox Geocoder API and the updated in the database.
- Nodes and Relationships for the Graph Database is defined in graphdb.py file , while data loading and wrangling is done in main.py
