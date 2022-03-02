"""This module provides functions to generate plots from data.

"""
import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

import numpy as np
"""from numpy import polyfit"""
from floodsystem.analysis import polyfit

def plot_water_levels(station, dates, levels):
    """displays a plot of the water level data against time for a station, 
    including plot lines for the typical low and high levels"""
    if dates == []:
        print(station.name + " has no data available")
    else:
        plt.plot(dates, levels, label = "measured level") #data
        plt.axhline(y=station.typical_range[0], color='r', linestyle='-', label = "typical lower bound")
        plt.axhline(y=station.typical_range[1], color='r', linestyle='-', label = "typical upper bound")
        plt.legend()

        #pretty
        plt.xlabel("date")
        plt.ylabel("water level (m)")
        plt.xticks(rotation = 45)
        plt.title("Station: " + station.name)
        plt.show()
    return "No Error"

def plot_water_level_with_fit(station, dates, levels, p):
    if dates == []:
        print(station.name + " has no data available")
    else:
        poly, d0 = polyfit(dates, levels, p)     # gathers the polyfit and offset
        x0 = matplotlib.dates.date2num(dates)   # converts dates to float form
        x1 = np.linspace(x0[0], x0[-1], 30)     # chooses 30 points in the date range to plot the polynomial for
        plt.plot(x1, poly(x1 - d0), c='k', label=("Best Fit, {} terms".format(p)))    # plots the polynomial with the offset
        plot_water_levels(station, dates, levels)   # plots the real data

def plotpoly(station, dates, levels, p):
    poly, d0 = polyfit(dates, levels, p)
    polyder1 = poly.deriv()
    x0 = matplotlib.dates.date2num(dates)   
    x1 = np.linspace(x0[0], x0[-1], 30)
    plt.plot(matplotlib.dates.num2date(x1), polyder1(x1-d0), c='r')
    polyder2 = polyder1.deriv()    
    plt.plot(matplotlib.dates.num2date(x1), polyder2(x1-d0), c='k', label=("Best Fit, {} terms".format(p)))
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    #plt.tight_layout()  # This makes sure plot does not cut off date labels
    #plt.legend(loc='best')
    plt.show()