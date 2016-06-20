# This is a program that will iterate through a dictionary of lat/long pairs from a csv
# For each pair, it will check to see if any of the other pairs are within a 50m sqare radius
# It will then add all of the other pairs in that radius to dictionary where the  main point
## is the key, and the value is a dictionary of all the other points in it's radius.
import csv
import pickle

sm_data = open('GeoCodes_1.csv','r')
sm_d = csv.reader(sm_data)

lines = []
for line in sm_d:
    lines.append(line)
sm_data.close()
sm_list = []
for item in lines[1:]:
    sm_list.append( (float(item[0]), float(item[1])) )

lg_data = open('GeoCodes.csv','r')
lg_d = csv.reader(lg_data)

rows = []
for row in lg_d:
    rows.append(row)
lg_data.close()
clean = rows[1:]
lg_list = []
for thing in clean:
    lg_list.append( (float(thing[0]), float(thing[1])) )



vals = {}
counter = 1
for s_tup in sm_list:
    current = s_tup
    (s_lat, s_long) = s_tup
    new_list = []
    for l_tup in lg_list:
        (l_lat, l_long) = l_tup
        if l_tup != current:
            if (l_lat>(s_lat-0.00049) and l_lat<(s_lat+0.00049))==True and (l_long>(s_long-0.00049) and l_long<(s_long+0.00049))==True:
                new_list.append( (l_lat, l_long) )
            else: 
                pass
        else:
            pass
    if s_tup in vals.keys():
        vals[s_tup].extend(new_list)
    else:
        vals[s_tup] = new_list
    print (str(counter)+" down.")
    counter +=1
print (vals)

with open('geo_data.txt', 'wb') as handle:
  pickle.dump(vals, handle)
