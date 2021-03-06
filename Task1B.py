from floodsystem.geo import haversine, stations_by_distance
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    p = (52.2053, 0.1218)
    list_stations_by_distance = stations_by_distance(stations, p)
    station_towns = {}
    for station in stations:
        station_towns[station.name] = station.town
    stations_and_towns_by_distance = [(station, station_towns[station], dist) for (station,dist) in list_stations_by_distance]

    print("Closest 10")
    print(stations_and_towns_by_distance[:10])
    print("Furthest 10")
    print(stations_and_towns_by_distance[-10:])

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()