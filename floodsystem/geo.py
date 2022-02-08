# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from .utils import sorted_by_key  # noqa
import numpy as np

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


#for 1B
from math import radians, cos, sin, asin, sqrt

def haversine(coord1, coord2):
    """
    Calculate the great circle distance in kilometers between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    radians_coord1 = np.array(coord1) * np.pi/180
    radians_coord2 = np.array(coord2) * np.pi/180

    # haversine formula 
    dlon = radians_coord2[1] - radians_coord1[1] 
    dlat = radians_coord2[0] - radians_coord1[0] 
    a = sin(dlat/2)**2 + cos(radians_coord1[0]) * cos(radians_coord2[0]) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    return c * r


def stations_by_distance(stations, p):
    """function that, given a list of station objects and a coordinate p, 
    returns a list of (station, distance) tuples, where distance (float) 
    is the distance of the station (MonitoringStation) from the coordinate p. 
    The returned list should be sorted by distance."""
    stations_by_distance = [(station.name, haversine(p, station.coord)) for station in stations]
    stations_by_distance = sorted(stations_by_distance, key=lambda tup: tup[1])
    return stations_by_distance

#1C:
def stations_within_radius(stations, centre, r):
    """function that returns a list of all stations (type MonitoringStation) 
    within radius r of a geographic coordinate x."""
    close_stations = []
    for station in stations:
        if haversine(station.coord, centre) < r:
         close_stations.append(station)
    return close_stations.sort()