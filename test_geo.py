"""Unit test for the geo module"""

from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_distance, stations_by_river, rivers_by_station_number, stations_within_radius, haversine

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

def test_rivers_by_station_number():
    #build list of stations and sorted list of rivers
    stations = build_station_list()
    top_7_rivers = [v for k,v in rivers_by_station_number(stations, 7)]

    #check that list is sorted properly
    assert all(top_7_rivers[i] >= top_7_rivers[i + 1] for i in range(len(top_7_rivers)-1))

    #check that max value is correct
    stations_along_river = stations_by_river(stations)
    station_numbers_along_river = [len(station) for river, station in stations_along_river.items()]
    assert top_7_rivers[0] == max(station_numbers_along_river)


def test_stations_by_distance(stations, p):
    #build list of stations and sorted by haversine distance
    stations = build_station_list()
    test_stations_by_distance = stations_by_distance(stations, (52.2053, 0.1218))
    #check that list is sorted properly
    assert all(test_stations_by_distance[i] >= test_stations_by_distance[i + 1] for i in range(len(test_stations_by_distance)-1))


def test_stations_within_radius(stations, centre, r):
    #build list of stations
    stations = build_station_list()
    #check how many stations are within the radius
    radius_station_number = 0
    for station in stations:
        if haversine(station, r) < 10:
            radius_station_number +=1
    #compare with number given by function
    stations_and_towns_by_distance = stations_by_distance(stations)
    assert radius_station_number == len(stations_by_distance)