from floodsystem.geo import haversine, stations_by_distance
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    p = (52.2053, 0.1218)
    list_stations_by_distance = stations_by_distance(stations, p)
    station_towns = {}
    for station in stations:
        station_towns[station.name] = station.town
    list_stations_by_distance = [(station.name, station_towns[station.name], haversine(p, station.coord)) for station in stations]

    print("Closest 10")
    print(list_stations_by_distance[:10])
    print("Furthest 10")
    print(list_stations_by_distance[-10:])

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()