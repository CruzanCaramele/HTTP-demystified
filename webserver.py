import cgi
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

#import module for ORM
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Restaurant, MenuItem, Base

#create and connect to database
engine = create_engine("sqlite:///restaurantmenu.db")
Base.metadata.bind=engine
DBSession = sessionmaker(bind=engine)
session=DBSession()

class webServerHandler(BaseHTTPRequestHandler):
	""" class defined in the main method """

	def do_GET(self): 

		try:
			if self.path.endswith("/restaurants"):
				#sending the response headers
				self.send_response(200)

				#reply with content type as text html
				self.send_header("Content-type", "text/html")
				self.end_headers()

				#content to send back to the client
				output = ""
				output += "<html><body>Hello !"
				output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
		 		output += "</body></html>"
				self.wfile.write(output)
				print output
				return

			if self.path.endswith("/hola"):
				#sending the response headers
				self.send_response(200)

				#reply with content type as text html
				self.send_header("Content-type", "text/html")
				self.end_headers()

				#content to send back to the client
				output = ""
				output += "<html><body>&#161Hola"
				output += "<a href='/hello' >Back to Hello</a>"
				output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
				output += "</body></html>"
				self.wfile.write(output)
				print output
				return

		except IOError:
			self.send_error(404, "File Not Found %s" % self.path)


	def do_POST(self):
		try:

		 	self.send_response(301)
		 	self.end_headers()

		 	#cgi.parse_header function parses html form header like content-typ
		 	#into a main value and dictionary of parameters
		 	ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))

		 	#check if content-type is form data being recieved
		 	if ctype == "multipart/form-data":
		 		#collect all fields in the form into fields dictionary
		 		fields = cgi.parse_multipart(self.rfile, pdict)

		 		#collect the value of specific filed from the form
		 		messagecontent = fields.get("message")

		 	output = ""
		 	output += "<html><body>"
		 	output += "<h2>Okay, How about this: </h2>"
		 	output += "<h1> %s </h1>" % messagecontent[0]

		 	output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''

		 	output += "</body></html>"

		 	self.wfile.write(output)
		 	print output
		 	return




		except:
		 	pass






def main():
	try:
		port = 8080
		server = HTTPServer(("", port), webServerHandler)
		print "web server running on port %s" % port
		server.serve_forever()


	except KeyboardInterrupt:
		print "^C entered, stopping web server....."
		server.socket.close()



if __name__ == '__main__':
	main()