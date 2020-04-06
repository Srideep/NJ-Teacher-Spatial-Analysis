from neomodel import db
from neomodel import (StructuredNode,StringProperty, IntegerProperty,FloatProperty,UniqueIdProperty, RelationshipTo,RelationshipFrom)

# Neo4j DB Connection URL
url = 'bolt://neo4j:rocks-egg-block@52.86.174.147:34333'

# Graph Databse (Neo4j) connection established
db.set_connection(url)

class County(StructuredNode):
  county_id = IntegerProperty(required=True)
  County = StringProperty(required=True)
  County_Label = StringProperty(required = True)
  Latitude = FloatProperty()
  Longitude = FloatProperty()
  Acres = FloatProperty()
  Sq_Miles = FloatProperty()
  Region = StringProperty()
  Shape_Length = FloatProperty()
  Shape_Area = FloatProperty()


class Town(StructuredNode):
  town_id = IntegerProperty(required=True)
  town = StringProperty(required=True)
  County = StringProperty(required=True)
  Zipcode = IntegerProperty()
  Latitude = FloatProperty()
  Longitude = FloatProperty()
  Region = StringProperty()

  county = RelationshipTo(County, 'In_County')
  teacher = RelationshipFrom(Teacher, 'Has_Teacher')






class Teacher(StructuredNode):
  teacher_id = IntegerProperty(required=True)
  Last_Name = StringProperty(required=True)
  First_Name = StringProperty(required=True)
  County = StringProperty()
  District = StringProperty()
  School = StringProperty()
  Primary_Job = StringProperty()
  FTE = FloatProperty()
  Salary = FloatProperty()
  Certification = StringProperty()
  Subcategory = StringProperty()
  Teaching_Route = StringProperty()
  Highly_Qualified = StringProperty()
  Experience_District = FloatProperty()
  Experience_NJ = FloatProperty()
  Experience_Total = FloatProperty()

  town = RelationshipTo(Town, 'Teaching_Town')
  county = RelationshipTo(County, 'Teaching_County')
  
