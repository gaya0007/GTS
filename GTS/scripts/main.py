from datetime  import date, datetime
from multiprocessing import Queue
#from price_handler import HistoricalPriceHandler
from ipc.ipc import IPC
from threading import Thread
import socket
import sys
import json
import io
import ipc


	
	
if __name__ == '__main__':	
	
	m_que = Queue()
	ipc = IPC("IPC", m_que)
	
	while True:
		try:
			print(m_que.get())
		except Queue.Empty:
			pass
 