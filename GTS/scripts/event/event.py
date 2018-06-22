class Event(object):
	pass


class TickEvent(Event):
	def __init__(self, instrument, time, bid, ask):
		self.type = 'TICK'
		self.instrument = instrument
		self.time = time
		self.bid = bid
		self.ask = ask

	def __str__(self):
		return "Type: %s, Instrument: %s, Time: %s, Bid: %s, Ask: %s" % (
			str(self.type), str(self.instrument), 
			str(self.time), str(self.bid), str(self.ask)
		)

	def __repr__(self):
		return str(self)


class SignalEvent(Event):
	def __init__(self, instrument, order_type, side, time):
		self.type = 'SIGNAL'
		self.instrument = instrument
		self.order_type = order_type
		self.side = side
		self.time = time  # Time of the last tick that generated the signal

	def __str__(self):
		return "Type: %s, Instrument: %s, Order Type: %s, Side: %s" % (
			str(self.type), str(self.instrument), 
			str(self.order_type), str(self.side)
		)

	def __repr__(self):
		return str(self)


class OrderEvent(Event):
	def __init__(self, instrument, units, order_type, side):
		self.type = 'ORDER'
		self.instrument = instrument
		self.units = units
		self.order_type = order_type
		self.side = side

	def __str__(self):
		return "Type: %s, Instrument: %s, Units: %s, Order Type: %s, Side: %s" % (
			str(self.type), str(self.instrument), str(self.units),
			str(self.order_type), str(self.side)
		)

	def __repr__(self):
		return str(self)
		
class AdminEvent(Event):
	def __init__(self, type, instrument):
		self.type = type
		self.instrument = instrument


	def __str__(self):
		return "Type: %s, Instrument: %s" (
			str(self.type), str(self.instrument))

	def __repr__(self):
		return str(self)

class IPC_AnalyzeEvent(Event):
	def __init__(self, type, instrument, from_date, to_date, timeframe):
		self.type = type
		self.instrument = instrument
		self.timeframe = timeframe 
		self.to_date = to_date
		self.from_date = from_date

	def __str__(self):
		return "Type: %s, Instrument: %s timeframe: %s from date: %s to date: %s" (
			str(self.type), str(self.instrument), str(self.timeframe), str(self.from_date), str(self.to_date))

	def __repr__(self):
		return str(self)
