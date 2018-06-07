import time
import socket
import signal

UDP_PORT = 5867
UDP_IP = 'localhost'

def main():
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	client_socket.bind((UDP_IP, UDP_PORT))
	print("listening...")
	try:
		while True:
			start = time.time()

			try:
				data, server = client_socket.recvfrom(1024)
				end = time.time()
				elapsed = end - start
				print(data);
			except socket.timeout:
				print('REQUEST TIMED OUT')
	except KeyboardInterrupt:	
			print("interrupted")
			
if __name__ == '__main__':
	main()