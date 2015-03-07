from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class webServerHandler(BaseHTTPRequestHandler):
	""" class defined in the main method """

	def do_GET(self): 

		try:
			if self.path.endswith("/hello"):
				#sending the response headers
				self.send_response(200)

				#reply with content type as text html
				self.send_header("Content-type", "text/html")
				self.end_headers()

				#content to send back to the client
				output = ""
				output += "<html><body>Hello ! </body></html>"
				self.wfile.write(output)
				print output
				return




		except IOError:
			self.send_error(404, "File Not Found %s" % self.path)


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