import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import threading
import os
from cgi import parse_header, parse_multipart, parse_qs
from ipc.ipc import handle_request


hostName = ""
hostPort = 8000

def make_request_handler_class(mq):
	
	m_queue = mq
	
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
			ctype, pdict = parse_header(self.headers.get('content-type'))
			if ctype == 'multipart/form-data':
				postvars = parse_multipart(self.rfile, pdict)
				print(postvars)
			elif ctype == 'application/x-www-form-urlencoded':
				length = int(self.headers.get('content-length'))
				postvars = parse_qs(self.rfile.read(length), keep_blank_values=1)
				print(postvars)				
			else:
				postvars = {}
			ret = handle_request(postvars)	
			self.send_response(200)
			self.send_header('Content-type', 'text/html')
			self.end_headers()

	return WebServer
	
class Server_Thread(threading.Thread):
	def __init__(self, name, dqueue):
		threading.Thread.__init__(self, name=name)
		RequestHandlerClass = make_request_handler_class(dqueue)
		self.m_server = HTTPServer((hostName, hostPort), RequestHandlerClass)
		print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))
		
	#thread
	def run(self):
			self.m_server.serve_forever()
			
	def stop(self):
		self.m_server.shutdown()
		