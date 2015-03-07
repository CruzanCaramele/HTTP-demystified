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
				output += "<h3>\
				    	     <a href='restaurants/new'>Add A new Restaurant</a>\
					    </h3>"

				for restaurant in restaurants:
					output += restaurant.name
					output += "<div>\
						       <a href='#'>Edit</a>\
						       <a href='#'>Delete</a>\
						    </div>"
					output += "</br></br>"

				output += "</body></html>"
				self.wfile.write(output)
				print output
				return


			if self.path.endswith("/restaurants/new"):
				output = ""
				self.send_response(200)
				self.send_header("Content-type", "text/html")
				self.end_headers()

				output += "<html><body>"
				output += "<h1>New Restaurant Name</h1>"
				output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/new'>"
				output += "<input name='newRestaurantName' type='text'>"
				output += "<input type='submit' value='Create'>"
				output += "</form>"
				output += "</body></html>"

				self.wfile.write(output)
				print output
				return



		except IOError:
			self.send_error(404, "File Not Found %s" % self.path)


	def do_POST(self):
		
		try:
			if self.path.endswith("/restaurants/new"):

				ctype, pdict = cgi.parse_header(self.headers.getheader("content-type"))

				#check of content-type is form
				if ctype == "multipart/form-data":

					#collect all fields from form, fields is a dictionary
					fields = cgi.parse_multipart(self.rfile, pdict)

					#extract the name of the restaurant from the form
					messagecontent = fields.get("newRestaurantName")

					newRestaurant = Restaurant(name=messagecontent[0])
					session.add(newRestaurant)
					session.commit()

					#response headers
					self.send_response(301)
					self.send_header("Content-type", "text/html")
					self.send_header('Location','/restaurants')
					self.end_headers()



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