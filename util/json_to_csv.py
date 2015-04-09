#!/user/bin/python
import json
import csv
import sys

input_file = open(sys.argv[1], 'r')
i = 0;

with open(sys.argv[2], 'wb') as output_file:
	csv_writer = csv.writer(output_file, delimiter=',')
	for line in input_file:
		if (i % 1000 == 0):
			print(i)
		j = json.loads(unicode(line, errors='replace'))
		if(j["datasource"]["key"] == 'T'):
			csv_writer.writerow([i, j["date"], j["comment"].encode('utf-8')])
			i = i+1