The WebServer will use the python [BaseHTTPServer](https://docs.
python.org/2/library/basehttpserver.html)
library extensively.
The WebServer will have 2 main methods, the **main** and **handler**
methods.
In the main method, the WebServer is instantiated and the port to be
used is specified. In the handler class, the type of http request is
specified.

###### Code Snippet to create and run the server

```
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
def main():
	try:
		""" Create instance of HTTP Server Class """
		port   = 8080
		"""the server address is tuple, contains host & port number for the server """
		server = HTTPServer(('',port), webserverHandler)
		print "Web server running on port %s" % port

		""" Keep the server constantly listening """
		server.serve_forever()


	except KeyboardInterrupt:
		print "^C entered, stopping web server...."
		server.socker.close()

if __name__ == '__main__':
	""" run main method when the python interpreter runs the script """
	main()
```

The above will create a simple web server on port 8080.