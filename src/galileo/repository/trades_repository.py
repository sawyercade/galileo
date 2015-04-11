from pymongo import MongoClient
from trade import Trade
import datetime

class TradesRepository:
	field_start_of_date = "start_of_date" #the datetime of the start of the day a trade occurred
	field_timestamp = "timestamp"
	field_price = "price"
	field_amount = "amount"

	def __init__(self, database, collection):
		self.client = MongoClient()
		self.db = self.client[database]
		self.collection = self.db[collection]

	def get_start_of_date(self, timestamp):
		date = datetime.date.fromtimestamp(timestamp)
		return date.strftime("%s")

#	def __init__(self, database, collection, host, port):
#		self.client = MongoClient(host, port)
#		self.db = client[database]
#		self.collection = collection

	def upsert(self, trade):
		start_of_date = self.get_start_of_date(trade.timestamp)

		self.collection.update({ TradesRepository.field_start_of_date : start_of_date }, { "$push" : { str(trade.timestamp) : { 
								 TradesRepository.field_timestamp : trade.timestamp, TradesRepository.field_price : trade.price,
								 TradesRepository.field_amount : trade.amount}}}, upsert = True)

		#self.collection.update({ TradesRepository.field_start_of_date : start_of_date }, { "$push" : { TradesRepository.field_timestamp : trade.timestamp,
							#	TradesRepository.field_prices : trade.price,  TradesRepository.field_amounts : trade.amount}}, upsert = True)
		