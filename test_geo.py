"""Unit test for the geo module"""

from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river

def test_rivers_with_station():
    #build list of stations and rivers
    stations = build_station_list()
    rivers = rivers_with_station(stations)

    #check every river occurs in the list exactly once
    for station in stations:
        rivers_list = list(rivers)
        river_occurrences = rivers_list.count(station.river)
        if river_occurrences != 1:
            raise AssertionError

def test_stations_by_river():
    #build list of stations
    stations = build_station_list()

    #count how many stations along River Cam independently
    cam_station_number = 0
    for station in stations:
        if station.river == 'River Cam':
            cam_station_number += 1
    
    #compare with number given by function
    stations_along_river = stations_by_river(stations)
    assert cam_station_number == len(stations_along_river['River Cam'])
