#uses geo.stations_by_distance and prints a list of tuples (station name, town, distance)
#for the 10 closest and the 10 furthest stations from the Cambridge city centre, (52.2053, 0.1218).

from floodsystem.geo import haversine, stations_by_distance
from floodsystem.stationdata import build_station_list

def run(p):
    stations = build_station_list()
    stations_by_distance = stations_by_distance(stations, p)
    p = (52.2053, 0.1218)
    print stations_by_distance[:10]
    print stations_by_distance[-10:]