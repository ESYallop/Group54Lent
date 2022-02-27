"""This module contains a collection of functions related to flooding.

"""

from floodsystem.station import MonitoringStation

def stations_level_over_threshold(stations, tol):
    """returns a list of tuples with (i) a station where the latest 
    relative water level > tol and (ii) this relative water level"""
    high_water_level_stations = []
    for station in stations:
        relative_water_level = MonitoringStation.relative_water_level(station)
        if relative_water_level == None:
            pass
        elif relative_water_level > tol:
            high_water_level_stations.append((station, relative_water_level))
    high_water_level_stations = sorted(high_water_level_stations, key=lambda tup: tup[1], reverse = True)
    return high_water_level_stations
