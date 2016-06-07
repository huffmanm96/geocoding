# This is a program that will iterate through a dictionary of lat/long pairs from a csv
# For each pair, it will check to see if any of the other pairs are within a 50m sqare radius
# It will then add all of the other pairs in that radius to a list that is named after the main point
import csv
import numpy as np

data = open('New_Geocodes.csv','r')
d = csv.reader(data)

lines = []
for line in d:
    lines.append(line)
data.close()
dict = {}
for item in lines[1:]:
    dict[float(item[0])] = float(item[1])
data.close()

vals = {}
for key in dict:
    current = key
    new_dict = {}
    for each_key in dict:
        if each_key != current:
            if each_key in range((key-0.0005),(key+0.0005)) and dict[each_key] in range((dict[key]-0.0005),(dict[key]+0.0005)):
            #if each_key >=((key-0.0005) and each_key <= (key+0.0005)) and dict[each_key] >= dict[key]-0.0005 and dict[each_key] <= dict[key]+0.0005:

                new_dict[each_key] = dict[each_key]
            else: 
                pass
        else:
            pass
    vals[(key, dict[key])] = new_dict
print (vals)

