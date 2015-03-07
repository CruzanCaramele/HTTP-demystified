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

				#Read and list out restaurants from database
				restaurants = session.query(Restaurant).all()

				output = ""
				output += "<html><body>"
				output += "<h1>Restaurants</h1>"

				for restaurant in restaurants:
					output += restaurant.name
					output += "</br></br>"

				output += "</body></html>"
				self.wfile.write(output)
				print output
				return

		except IOError:
			self.send_error(404, "File Not Found %s" % self.path)


	def do_POST(self):
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