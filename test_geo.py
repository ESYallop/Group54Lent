"""Unit test for the geo module"""

from struct import pack
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list

from floodsystem.geo import haversine, stations_by_distance, stations_within_radius, rivers_with_station, stations_by_river, rivers_by_station_number

def test_haversine():
    x = haversine((45.7597, 4.8422), (48.8567, 2.3508))
    assert round(x,2) == 392.22

def test_stations_by_distance():
    # Create a list of station with varying coords
    s_id = "test-s-id"
    m_id = "test-m-id"
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s1 = MonitoringStation(s_id, m_id, "one", (50, 1), trange, river, town)
    s2 = MonitoringStation(s_id, m_id, "two", (60,1), trange, river, town)
    s3 = MonitoringStation(s_id, m_id, "three", (70,1), trange, river, town)
    stations = [s1,s2,s3]

    #check listed in correct order by distance from point p 
    p = (40,1)
    station_names = [station for (station, dist) in stations_by_distance(stations,p)]
    assert station_names == [s1.name,s2.name,s3.name]

def test_stations_within_radius():
    # Create a list of station with varying coords
    s_id = "test-s-id"
    m_id = "test-m-id"
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s1 = MonitoringStation(s_id, m_id, "one", (50, 1), trange, river, town)
    s2 = MonitoringStation(s_id, m_id, "two", (60,1), trange, river, town)
    s3 = MonitoringStation(s_id, m_id, "three", (70,1), trange, river, town)
    s4 = MonitoringStation(s_id, m_id, "four", (55, 3), trange, river, town)
    s5 = MonitoringStation(s_id, m_id, "five", (55,-2), trange, river, town)
    stations = [s1,s2,s3,s4,s5]
    
    #check only stations within certain distance (in multiple directions) from p included
    p = (55,1)
    r = 600
    stations_within_range = stations_within_radius(stations, p, r)
    assert s1, s2 in stations_within_range
    assert s4, s5 in stations_within_range
    assert not s3 in stations_within_range
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

