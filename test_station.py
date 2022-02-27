# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from numpy import half
from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations
from floodsystem.flood import stations_level_over_threshold


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_typical_range_consistent():
    # Create some stations with different typical ranges
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    river = "River X"
    town = "My Town"

    consistent = MonitoringStation(s_id, m_id, label, coord, (1,2), river, town)
    no_trange = MonitoringStation(s_id, m_id, label, coord, None, river, town)
    inconsistent = MonitoringStation(s_id, m_id, label, coord, (5.2, 4.9), river, town)

    assert MonitoringStation.typical_range_consistent(consistent) == True
    assert MonitoringStation.typical_range_consistent(no_trange) == False
    assert MonitoringStation.typical_range_consistent(inconsistent) == False

def test_inconsistent_typical_range_stations():
    # Create some stations with different names and typical ranges
    s_id = "test-s-id"
    m_id = "test-m-id"
    coord = (-2.0, 4.0)
    river = "River X"
    town = "My Town"

    consistent = MonitoringStation(s_id, m_id, "Consistent", coord, (1,2), river, town)
    no_trange = MonitoringStation(s_id, m_id, "No Typical Range", coord, None, river, town)
    inconsistent = MonitoringStation(s_id, m_id, "Inconsistent", coord, (5.2, 4.9), river, town)
    stations = [consistent, no_trange, inconsistent]
    inconsistent_stations = inconsistent_typical_range_stations(stations)

    assert "No Typical Range", "Inconsistent" in inconsistent_stations
    assert not "Consistent" in inconsistent_stations

def test_relative_water_level():
    # Create some stations with different latest levels and typical ranges
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    river = "River X"
    town = "My Town"
    
    half = MonitoringStation(s_id, m_id, label, coord, (1,2), river, town)
    no_trange = MonitoringStation(s_id, m_id, label, coord, None, river, town)
    inconsistent = MonitoringStation(s_id, m_id, label, coord, (5.2, 4.9), river, town)
    half.latest_level = 1.5
    no_trange.latest_level = 1.5
    inconsistent.latest_level = 1.5
    assert half.relative_water_level() == 0.5
    assert no_trange.relative_water_level() == None
    assert inconsistent.relative_water_level() == None

    half.latest_level = None
    assert half.relative_water_level() == None

def test_stations_level_over_threshold():
    # Create some stations with different relative water levels
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    river = "River X"
    town = "My Town"
    
    half = MonitoringStation(s_id, m_id, "half", coord, (1,2), river, town)
    quarter = MonitoringStation(s_id, m_id, "quarter", coord, (2,6), river, town)
    one = MonitoringStation(s_id, m_id, "one", coord, (3, 6), river, town)
    nope = MonitoringStation(s_id, m_id, "nope", coord, (3, 6), river, town)
    half.latest_level = 1.5
    quarter.latest_level = 3
    one.latest_level = 6
    nope.latest_level = None

    stations = [half,quarter,one,nope]
    high_water_level_stations = stations_level_over_threshold(stations, 0.3)
    high_water_level_stations_names = [(station.name, level) for (station,level) in high_water_level_stations]

    assert high_water_level_stations_names == [("one",1),("half",0.5)]


