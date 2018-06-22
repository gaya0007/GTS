from event import event
from downloader.downloader import DownloadMgr
import pandas as pd
import os

class HistoricalPriceHandler():
	def __init__(self, pair, start_date, end_date):
		self.start_date = start_date
		self.end_date = end_date
		self.pair = pair
		self.dmgr = DownloadMgr()
		self.df = pd.DataFrame()
		
	def get_df(self):
		files = self.dmgr.download_historical_data(self.pair, self.start_date, self.end_date)
		print(os.getcwd())
		for file in files:
			pd.read_pickle(file).head()
			#self.df.append(pd.read_pickle(file))
		print(self.df.head())	
		return self.df
		
	def stream_df(self):	
		strat_date_ts = pd.Timestamp(self.start_date)
		end_date_ts = pd.Timestamp(self.end_date)

		for index, row in df.iterrows():
			if index >= strat_date_ts and index <= end_date_ts:
				ev = event.TickEvent(self.pair, index, row[0], row[1])
				node_send_event(ev)
			else:
				if index > end_date_ts:
					break
				else:
					continue 					