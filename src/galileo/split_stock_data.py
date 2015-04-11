#!/usr/bin/python
import csv
import sys

seconds_in_day = 86400
first_trade_day = 1315958400
file_num = 0
split_path = sys.argv[2]
output_file = open(split_path + "_" + str(file_num), 'a');

with open(sys.argv[1], 'rb') as csvfile:
	reader = csv.reader(csvfile)
	for line in reader:
		time = int(line[0])
		if ((time - first_trade_day) / seconds_in_day != file_num):
			output_file.close()
			file_num = (time - first_trade_day) / seconds_in_day
			output_file = open(split_path + "_" + str(file_num) + ".csv", 'a')
		output_file.write(", ".join(line))
		output_file.write("\n")

