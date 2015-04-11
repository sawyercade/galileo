import csv
import sys
from pymongo import MongoClient
from repository import *

input_path = sys.argv[1]
db_name = sys.argv[2]
col_name = sys.argv[3]

repository = TradesRepository(db_name, col_name)

with open(input_path, 'rb') as csvfile:
	reader = csv.reader(csvfile)
	for line in reader:
		trade = Trade(int(line[0]), float(line[1]), float(line[2]))
		repository.upsert(trade)