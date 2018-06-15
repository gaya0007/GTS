import socket
import signal
import threading
import select
import queue

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
		self.mqueue = queue.Queue()
		rcv_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		rcv_socket.bind((UDP_IP, UDP_RCV_PORT))
		rcv_socket.setblocking(0)
		self.__instance = self
		print("listening for IPC...")
		
	def run(self):
		try:
			while True:
				try:
					data, server = rcv_socket.recvfrom(1024)
					if data:
						self.mdataqueue.put(data)
					else:
						try:
							rcv_socket.sendto(self.mqueue.get_nowait(), (UDP_IP, UDP_SND_PORT))
						except Queue.Empty:	
							pass
					
				except socket.timeout:
					print('REQUEST TIMED OUT')
					
		except KeyboardInterrupt:	
				print("interrupted")
	
	def ipc_send(self, data):
		self.mqueue.put(data)
		
if __name__ == '__main__':
	raise ValueError("module nbot to be used directly.")