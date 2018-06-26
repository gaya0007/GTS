import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import threading
import os

hostName = ""
hostPort = 8000

class WebServer(BaseHTTPRequestHandler):	
	def do_GET(self):
		if self.path=='/favicon.ico':
			return
		f = open(os.getcwd() + self.path, 'rb')
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
		self.wfile.write(f.read())
		f.close()

#	POST is for submitting data.
	def do_POST(self):

		print( "incoming http: ", self.path )

		content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
		post_data = self.rfile.read(content_length) # <--- Gets the data itself
		
		print(post_data)
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()

		
class Server_Thread(threading.Thread):
	def __init__(self, name, dqueue):
		threading.Thread.__init__(self, name=name)
		self.m_server = HTTPServer((hostName, hostPort), WebServer)
		print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))
		
	#thread
	def run(self):
			self.m_server.serve_forever()
			
	def stop(self):
		self.m_server.shutdown()
		