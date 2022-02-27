from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level

def run():
    stations = build_station_list()
    update_water_levels(stations)
    top_ten_stations = stations_highest_rel_level(stations,10)
    for station in top_ten_stations:
        print(station.name + " " + str(station.relative_water_level()))

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()