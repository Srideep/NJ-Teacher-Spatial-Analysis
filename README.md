# NJ Teacher Graph DB Builder
This repo will be used to do CRUD operations on building a graph db for NJ Teachers and their info using Neo4j database hosted in cloud. 
CSV files containing County, Town and Teacher information is used to load , clean and insert/update in the database.
Geocoding Information where needed is generated using Mapbox Geocoder API and the updated in the database.
Nodes and Relationships for the Graph Database is defined in graphdb.py file , while data loading and wrangling is done in main.py
