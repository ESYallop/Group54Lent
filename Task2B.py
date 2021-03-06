from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():
    stations = build_station_list()
    update_water_levels(stations)
    stations_over_four_fifths = stations_level_over_threshold(stations,0.8)
    for (station,level) in stations_over_four_fifths:
        print(station.name + " " + str(level))

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()