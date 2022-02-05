
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river

def run():
    """Requirements for Task 1D"""
    #Part 1
    stations = build_station_list()
    rivers = rivers_with_station(stations)
    rivers_alphabetical = sorted(rivers)
    print(str(len(rivers)) + " stations. First 10 - " + str(rivers_alphabetical[:10]))

    #Part 2
    def alphabetical_stations_on_river(river):
        """Names of the stations located along a river in alphabetical order"""
        stations_along_river = stations_by_river(stations)
        river_names = [station.name for station in stations_along_river[river]]
        return sorted(river_names)

    print("River Aire: " + str(alphabetical_stations_on_river('River Aire')))
    print("River Cam: " + str(alphabetical_stations_on_river('River Cam')))
    print("River Thames: " + str(alphabetical_stations_on_river('River Thames')))

if __name__ == "__main__":
    print("*** Rivers with Monitoring Stations, and Stations Along Various Rivers ***")
    run()
