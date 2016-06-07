# This is a program that will iterate through a dictionary of lat/long pairs from a csv
# For each pair, it will check to see if any of the other pairs are within a 50m sqare radius
# It will then add all of the other pairs in that radius to a list that is named after the main point
import csv
data = open('New_Geocodes.csv','r')
d = csv.reader(data)

lines = []
for line in d:
    lines.append(line)
dict = {}
for item in lines[1:]:
    dict[float(item[0])] = float(item[1])
print (dict)
data.close()
