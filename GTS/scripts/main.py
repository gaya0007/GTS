from datetime  import date, datetime
import queue
#from price_handler import HistoricalPriceHandler
from ipc.ipc import IPC
from threading import Thread
import socket
import sys
import json
import io
import ipc


def main():
	m_que = queue.Queue()
	ipc = IPC("IPC", m_que)
	while True:
		try:
			print("read queue")
			print(m_que.get_nowait())
		except Empty:
			pass
			
if __name__ == '__main__':	
	
	try:
		main()
	except KeyboardInterrupt:
		print("Interrupted")
		sys.exit(0)

 