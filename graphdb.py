from neomodel import db
from neomodel import (StructuredNode,StringProperty, IntegerProperty,FloatProperty,UniqueIdProperty, RelationshipTo,RelationshipFrom)

# Neo4j DB Connection URL
url = 'bolt://neo4j:rocks-egg-block@52.86.174.147:34333'

# Graph Databse (Neo4j) connection established
db.set_connection(url)

class County(StructuredNode):
    Name = StringProperty(unique_index=True ,required=True)
    County_Label = StringProperty(required = True)
    
