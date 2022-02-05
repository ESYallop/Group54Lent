
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station

def run():
    """Requirements for Task 1D"""
    stations = build_station_list()
    rivers = rivers_with_station(stations)
    rivers_alphabetical = sorted(rivers)
    print(str(len(rivers)) + " stations. First 10 - " + str(rivers_alphabetical[:10]))

if __name__ == "__main__":
    print("*** Rivers with Monitoring Stations ***")
    run()
