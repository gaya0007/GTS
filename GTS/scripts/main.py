from datetime  import date, datetime
try:
	import Queue as queue
except ImportError:
	import queue
from price_handler.price_handler import HistoricalPriceHandler
#from ipc.ipc import IPC
from threading import Thread
import socket
import sys
import json
import io
from datetime import timedelta, date
from http.server import HTTPServer
from web_server.web_server import Server_Thread


#dflist = []

#def run_analyze(instrument, to_date, from_date, timeframe):
#	strt_date = datetime.strptime(to_date, '%a %b %d %Y').date()
#	print(strt_date)
#	end_date = datetime.strptime(from_date, '%a %b %d %Y').date()
#	phdl = HistoricalPriceHandler(instrument, strt_date, end_date)
#	df = phdl.get_df()
#	dflist.append(phdl)
#	
#	print(dflist)

def main():
	m_que = queue.Queue()
	#ipc = IPC("IPC", m_que)
	#ipc.start()
	
	server =  Server_Thread("web server", m_que)
	server.start()

	while True:
		try:
			item = m_que.get(timeout=1)
			pass
			#if item.type == 'ANALYZE':				
				#run_analyze(item.instrument, item.to_date, item.from_date, item.timeframe)

		except queue.Empty:
			pass
		
		except KeyboardInterrupt:
			print("KeyboardInterrupt quit")
			server.stop()
			server.join()
			sys.exit()
			
if __name__ == '__main__':	
	main()


 