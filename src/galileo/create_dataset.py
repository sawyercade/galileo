#!/usr/bin/python
import csv
import sys

#should just use a document-based db for this, like MongoDB
seconds_in_min = 60
mins_in_hour = 60
hours_in_day = 60
seconds_in_day = seconds_in_min * mins_in_hour * hours_in_day

first_trade_day = 1315958400

comments_filepath = sys.argv[1]
split_filepath_format = sys.argv[2] #e.g. ../market/split_trades/split_btceUSD for split_btceUSD_1.csv, split_btceUSD_2.csv, etc
output_filepath = sys.argv[3]

time_period_seconds = int(sys.argv[4]) #length of time over which to get an average price

# this is going to break if we don't have trade data for the period after a comment
def get_average_exchange_rate (start_time):
	total = 0.0
	count = 0
	file_num = (start_time - first_trade_day) / seconds_in_day
	read_next_file = True
	seek = True

	while (read_next_file):
		try:
			with open(split_filepath_format + "_" + str(file_num) + ".csv") as csvfile:
				reader = csv.reader(csvfile)
				for line in reader:
					trade_time = line[0]
					if ((trade_time >= start_time) & (trade_time <= start_time + time_period_seconds)):
						seek = False
						total += float(line[1])
						count += 1
					else:
						if(seek): #first row in first file probably isn't in range
							continue
						else:
							read_next_file = False
							break #think this is the right logic
				file_num += 1
		except IOError as e:
			read_next_file = False
			print("IOError for timestamp " + str(start_time))
			print(e)
			continue
	return total / count

with open(comments_filepath, 'rb') as comments_file:
	with open(output_filepath, 'a') as output_file:
		comments_reader = csv.reader(comments_file)
		i = 0
		for line in comments_reader:
			time = int(line[1]) / 1000 #comments time is in ms, not s
			average = get_average_exchange_rate(time)
			output = line + str(average)
			output_file.write(", ".join(output))
			i += 1
			if (i % 100 == 0):
				print(str(i) + " comments read")





