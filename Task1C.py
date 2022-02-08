from floodsystem.geo import haversine, stations_within_radius
from floodsystem.stationdata import build_station_list
stations = build_station_list()
def run():
    print(stations_within_radius(stations, (52.2053, 0.1218), 10))

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()