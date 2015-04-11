from pymongo import MongoClient
from trade import Trade
from trades_repository import TradesRepository

trade = Trade(0)
trade.setTrade(500)
repo = TradesRepository("test", "testData")

repo.upsert(trade)