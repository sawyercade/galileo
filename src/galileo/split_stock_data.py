#!/usr/bin/python
import csv
import sys

seconds_in_day = 86400
first_trade_day = 1313280000 #start of day for which first trade occurred
file_num = 0
input_path = sys.argv[1]
split_path = sys.argv[2]
output_file = open(split_path + "_" + str(file_num) + ".csv", 'a');

lines = 0
with open(input_path, 'rb') as csvfile:
	reader = csv.reader(csvfile)
	for line in reader:
		time = int(line[0]) #unix/posix time
		if ((time - first_trade_day) / seconds_in_day != file_num): #start new file
			output_file.close()
			file_num = (time - first_trade_day) / seconds_in_day
			output_file = open(split_path + "_" + str(file_num) + ".csv", 'a')
		output_file.write(", ".join(line))
		output_file.write("\n")
		lines += 1
		if (lines % 100000 == 0):
			print("lines: " + str(lines) + "\ntime: " + str(time))

