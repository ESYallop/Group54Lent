# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from .utils import sorted_by_key  # noqa

def rivers_with_station(stations):
    """For a list of MonitoringStation objects, returns set with 
    the names of rivers with a monitoring station."""
    rivers = {x.river for x in stations}
    return rivers

def stations_by_river(stations):
    """For a list of MonitoringStation objects, returns a dictionary 
    which maps rivers names to station objects along them."""
    rivers = rivers_with_station(stations)
    stations_by_river = {}
    for river in rivers:
        stations_by_river.update(river = [])
        stationsAlong = []
        for station in stations:
            if station.river == river:
                stationsAlong.append(station)
        stations_by_river[river]=stationsAlong
    return stations_by_river

def rivers_by_station_number(stations, N):
    """For a list of MonitoringStation objects and integer N, determines 
    the N rivers with the greatest number of monitoring stations, 
    returning a list of (river name, number of stations) tuples."""
    stations_along_river = stations_by_river(stations)
    station_numbers_along_river = {river: len(station) for river, station in stations_along_river.items()}

    top_N_rivers = {}
    #set ensures no duplicates. turned back into list so can be indexed
    top_values = list(set(sorted(station_numbers_along_river.values())))[:-N-1:-1]
    print(type(station_numbers_along_river.values()))
    for k, v in station_numbers_along_river.items():
        if v in top_values:
            top_N_rivers[k] = v
    return list(({k: v for k, v in sorted(top_N_rivers.items(), key=lambda item: item[1], reverse = True)}).items())
