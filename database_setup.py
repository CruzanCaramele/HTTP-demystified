#sys, used to manipulate different parts
#of the python run-time environment
import sys

#importing classes from sqlalchemy module
from sqlalchemy import Column, ForeignKey, Integer, String

#delcaritive_base , used in the configuration
# and class code, used when writing mapper
from sqlalchemy.ext.declarative import declarative_base

#relationship in order to create foreign key relationship
#used when writing the mapper
from sqlalchemy.orm import relationship

#create_engine to used in the configuration code at the
#end of the file
from sqlalchemy import create_engine


#this object will help set up when writing the class code
Base = declarative_base()



class Restaurant(Base):
	"""
	class Restaurant corresponds to restaurant table
	in the database to be created.

	table representation for restaurant which
	is in the database 
	"""
	__tablename__ = 'restaurant'


	#column definitions for the restaurant table
	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)



class MenuItem(Base):
	"""
	class MenuItem corresponds to restaurant table
	

	table representation for menu_item which
	is in the database 		
	"""
	__tablename__ = 'menu_item'

	#column definitions for the restaurant table
	name = Column(String(80), nullable=False)
	id = Column(Integer, primary_key=True)
	course = Column(String(250))
	description = Column(String(250))
	price = Column(String(8))
	restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
	restaurant = relationship(Restaurant)

	@property
	def serialize(self):
		#Returns object data in easily serializable format
		return {
			"name" : self.name,
			"description" : self.description,
			"id" : self.id, 
			"course" : self.course,
			"price" : self.price,
		}



#create an instance of create_engine class
#and point to the database to be used
engine = create_engine('sqlite:///restaurantmenu.db')

#goes into the database and adds our new tables
#that will soon be added into the database. makes
#the engine
Base.metadata.create_all(engine)