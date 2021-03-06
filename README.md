## About

This is a small project demonstrating the use of the BaseHTTPServer class to create an HTTP web server that performs [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) operations. 

The goal of this project is to use Python code to explain how the webserver uses GET and POST operations to perform operations on a sqlite database.



##### Basics of HTTP GET and POST methods

* [Clients,Servers and Protocols](docs/Clients_Servers_Protocols.md)
* [The Web Server](docs/1.Simple_WebServer.md)
* [HTTP GET method](docs/2.WebServerHandler_GET.md)
* [HTTP POST method](docs/3.WebServerHandler_POST.md)



##### Complete Web Server (CRUD Operations)

* [Web Server](code/)

* Before running the webserver, get all requirements listed in [this](https://github.com/CruzanCaramele/MenuDatabase/blob/master/README.md) repository



##### Running the Webserver

1. On your preferred bash program navigate to the restaurant directory
2. type in the command *python webserver.py* 
3. open you browser and navigate to the link http://localhost:8080/restaurants to perform CRUD operations directly from the browser