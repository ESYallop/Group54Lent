"""This module provides functions to generate plots from data.

"""
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.datafetcher import fetch_measure_levels


def plot_water_levels(station, dates, levels):
    """displays a plot of the water level data against time for a station, 
    including plot lines for the typical low and high levels"""
    if dates == []:
        print(station.name + " has no data available")
    else:
        plt.plot(dates, levels)
        plt.xlabel("date")
        plt.ylabel("water level (m)")
        plt.xticks(rotation = 45)
        plt.title("Station: " + station.name)
        plt.show()
    return "No Error"