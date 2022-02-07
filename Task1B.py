from floodsystem.geo import haversine, stations_by_distance
from floodsystem.stationdata import build_station_list

def run(p):
    stations = build_station_list()
    stations_by_distance = stations_by_distance(stations, p)
    p = (52.2053, 0.1218)
    print stations_by_distance[:10]
    print stations_by_distance[-10:]

if __name__ == "__main__":
print("*** Task 1B: CUED Part IA Flood Warning System ***")
run()