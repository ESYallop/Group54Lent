"""Unit test for the flood module"""

from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level

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

def test_stations_highest_rel_level():
    # Create some stations with different relative water levels
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    river = "River X"
    town = "My Town"
    
    half = MonitoringStation(s_id, m_id, "half", coord, (1,2), river, town)
    quarter = MonitoringStation(s_id, m_id, "quarter", coord, (2,6), river, town)
    eigth = MonitoringStation(s_id, m_id, "eigth", coord, (1,2), river, town)
    one = MonitoringStation(s_id, m_id, "one", coord, (3, 6), river, town)
    nope = MonitoringStation(s_id, m_id, "nope", coord, (3, 6), river, town)
    half.latest_level = 1.5
    quarter.latest_level = 3
    eigth.latest_level = 1.125
    one.latest_level = 6
    nope.latest_level = None

    stations = [half,quarter,eigth,one,nope]
    top_3_stations = stations_highest_rel_level(stations,3)
    top_3_stations_names = [station.name for station in top_3_stations]
    assert top_3_stations_names == ["one","half","quarter"]