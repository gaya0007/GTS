from datetime  import date, datetime
try:
	import Queue as queue
except ImportError:
	import queue
from price_handler.price_handler import HistoricalPriceHandler
from ipc.ipc import IPC
from threading import Thread
import socket
import sys
import json
import io
from datetime import timedelta, date

dflist = []

def run_analyze(instrument, to_date, from_date, timeframe):
	strt_date = datetime.strptime(to_date, '%a %b %d %Y').date()
	print(strt_date)
	end_date = datetime.strptime(from_date, '%a %b %d %Y').date()
	phdl = HistoricalPriceHandler(instrument, strt_date, end_date)
	df = phdl.get_df()
	print(df.head())
	dflist.append(phdl)
	print("apended df")

def main():
	m_que = queue.Queue()
	ipc = IPC("IPC", m_que)
	ipc.start()

	while True:
		try:
			print("waiting for evt")
			item = m_que.get()
			if item.type == 'ANALYZE':				
				run_analyze(item.instrument, item.to_date, item.from_date, item.timeframe)

		except queue.Empty:
			pass
			
if __name__ == '__main__':	
	
	try:
		main()
	except KeyboardInterrupt:
		print("Interrupted")
		sys.exit(0)

 