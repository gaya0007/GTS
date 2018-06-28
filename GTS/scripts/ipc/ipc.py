import socket
import signal
import threading
import select
try:
	import Queue as queue
except ImportError:
	import queue
from event.event import IPC_AnalyzeEvent

def dummy(parms):
	return 1

def create_df(parms):
	print("create_df")
	return 
	
requests = {
	'CREATE' 	: create_df,
	'NONE'		: dummy
}

def handle_request(input):
	cmd = input.get("cmd", "NONE")
	print(cmd)
	return requests[cmd](input)

UDP_RCV_PORT = 5868
UDP_IP = 'localhost'
UDP_SND_PORT = 5867


class IPC(threading.Thread):
	__instance = None

	@staticmethod
	def getInstance():
		""" Static access method. """
		if IPC.__instance == None:
			raise Exception("Not yet instantiated")
		return IPC.__instance 
		
	def __init__(self, name, dqueue):
		threading.Thread.__init__(self, name=name)
		self.name = name
		self.mdataqueue = dqueue
		self.rcv_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.rcv_socket.bind((UDP_IP, UDP_RCV_PORT))
		self.mqueue = queue.Queue()
		self.rcv_socket.settimeout(0.000001) # non blocking mode doesn't work, hence the timeout set to a min value
		#self.rcv_socket.setblocking(False)
		self.__instance = self
		print("listening for IPC...")
		
	def run(self):
		try:
			while True:
				try:
					data, server = self.rcv_socket.recvfrom(1024)
					if data:
						self.handle_input(data)
					else:
						try:
							self.rcv_socket.sendto(self.mqueue.get_nowait(), (UDP_IP, UDP_SND_PORT))
						except queue.Empty:	
							pass
					
				except socket.timeout:
					pass
		except KeyboardInterrupt:	
				print("interrupted")
	
	def ipc_send(self, data):
		self.mqueue.put(data)
		
	def analyze_ipc(input):
		return IPC_AnalyzeEvent(input[0], input[1], input[2], input[3], input[4])	
		
	switcher = {
		'ANALYZE' : analyze_ipc,
	}
	
	def handle_input(self, data):
		ipc_inputs = data.decode("utf-8").split(";")
		print(ipc_inputs)
		ipc_parm_length = len(ipc_inputs)
		cmd = ipc_inputs[0]
		
		print("CMD {}".format(cmd))
		evt = self.switcher[cmd](ipc_inputs)
		self.mdataqueue.put(evt)
		

		
if __name__ == '__main__':
	raise ValueError("module not to be used directly.")