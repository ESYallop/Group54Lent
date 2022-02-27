# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        #note: typical range is tuple
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d
    
    def typical_range_consistent(self):
        """Checks whether the typical range data is consistent, 
        returns boolean value"""
        if self.typical_range == None:
            return False
        elif self.typical_range[1] > self.typical_range[0]:
            return True
        else:
            return False

    def relative_water_level(self):
        """Returns latest water level as fraction of the typical range"""
        if MonitoringStation.typical_range_consistent(self) == False or self.latest_level == None:
            return None
        else:
            water_level_range = self.typical_range[1]-self.typical_range[0]
            return (self.latest_level-self.typical_range[0])/water_level_range
        
def inconsistent_typical_range_stations(stations):
    """Given list of MonitoringStation objects, returns a list of stations
    that have inconsistent data."""
    inconsistent_stations = [station.name for station in stations if MonitoringStation.typical_range_consistent(station) == False]
    return inconsistent_stations
