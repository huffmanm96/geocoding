import geopy
from geopy.distance import VincentyDistance

# given: lat1, lon1, b = bearing in degrees, d = distance in kilometers
lat1 = 32.773178
lon1 = -79.920094
b = 30
d = 0.05

origin = geopy.Point(lat1, lon1)
destination = VincentyDistance(kilometers=d).destination(origin, b)

lat2, lon2 = destination.latitude, destination.longitude
print ((lat2, lon2))

#Point 2: 32.781666666666666, -79.916666666666671


