import pickle

with open('geo_data.txt', 'rb') as handle:
  b = pickle.loads(handle.read())


def point_lookup(lat, lon):
    return b[(lat, lon)]

print (point_lookup(42.203024, -83.405848))
