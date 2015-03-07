#Restaurant

This is a small project demonstrating the use of the BaseHTTPServer class to create a server that performs [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) operations. The webserver uses GET and POST operations to perform operations on a sqlite database.

##Contents
1. *database_setup.py file* : this is the database configuration file. This has 4 components including the configuration part, class definition part, table definition part for tables in the database and the mapper which defines the columns in the database
2.  *lotsofmenu.py file* : this populates data into the database
3. *restaurantmenu.db file* : this is the database file 
4. *webserver.py file* : the webserver file


*Before running the webserver, get all requirements listed in [this](https://github.com/CruzanCaramele/MenuDatabase/blob/master/README.md) repository

### Running the Webserver

1. On your preferred bash program navigate to the restaurant directory
2. type in the command *python webserver.py* 
3. open you browser and navigate to the link http://localhost:8080/restaurants to perform CRUD operations directly from the browser