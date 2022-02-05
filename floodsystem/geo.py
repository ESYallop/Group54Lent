# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from .utils import sorted_by_key  # noqa

def rivers_with_station(stations):
    """Given list of MonitoringStation objects, returns set with
    names of rivers with a monitoring station."""
    rivers = {x.river for x in stations}
    return rivers

def stations_by_river(stations):
    """Given list of MonitoringStation objects, returns dictionary which
    maps rivers names to station objects along them."""
    rivers = rivers_with_station(stations)
    stations_by_river = {}
    for river in rivers:
        stations_by_river.update(river = None)
        stationsAlong = []
        for station in stations:
            if station.river == river:
                stationsAlong.append(station)
        stations_by_river[river]=stationsAlong
    return stations_by_river
