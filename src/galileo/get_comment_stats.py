import csv
import sys

comments_filepath = sys.argv[1]
count = 0
min_time = 9999999999
max_time = 0

with(open(comments_filepath, 'rb')) as comments_file:
        comments_reader = csv.reader(comments_file)
        for line in comments_reader:
                count += 1
                time = int(line[1])/1000
                if (time > max_time):
                        max_time = time
                if (time < min_time):
                        min_time = time

print("min: " + str(min_time))
print("max: " + str(max_time))
print("count: " + str(count))
