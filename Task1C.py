#uses the function geo.stations_within_radius to build a list of stations 
#within 10 km of the Cambridge city centre (coordinate (52.2053, 0.1218)). 
#Print the names of the stations, listed in alphabetical order.

from floodsystem.geo import haversine, stations_within_radius

def run():
    print(stations_within_radius(stations, (52.2053, 0.1218), 10))
