# This is a program that will iterate through a dictionary of lat/long pairs from a csv
# For each pair, it will check to see if any of the other pairs are within a 50m sqare radius
# It will then add all of the other pairs in that radius to dictionary where the  main point
## is the key, and the value is a dictionary of all the other points in it's radius.
import csv
import pickle

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
counter = 1
for key in dict:
    current = key
    new_dict = {}
    for each_key in dict:
        if each_key != current:
            if (each_key>(key-0.00049) and each_key<(key+0.00049))==True and (dict[each_key]>(dict[key]-0.00049) and dict[each_key]<(dict[key]+0.00049))==True:
                new_dict[each_key] = dict[each_key]
            else: 
                pass
        else:
            pass
    vals[(key, dict[key])] = new_dict
    print (str(counter)+" down.")
    counter +=1
print (vals)

with open('geo_data.txt', 'wb') as handle:
  pickle.dump(vals, handle)
