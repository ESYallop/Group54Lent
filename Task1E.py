from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river, rivers_by_station_number

def run():
    stations = build_station_list()
    print("Rivers with the N-highest Number of Stations" + str(rivers_by_station_number(stations, 9)))

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()