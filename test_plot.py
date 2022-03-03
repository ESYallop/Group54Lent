"""Unit test for the plot module"""
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels, plot_water_level_with_fit
import matplotlib.pyplot as plt
import datetime
from floodsystem.datafetcher import fetch_measure_levels

def test_plot_water_levels():
    stations = build_station_list()
    update_water_levels(stations)
    station = stations[0]
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=5))
    plot_water_levels(station, dates, levels)

def test_plot_water_level_with_fit():
    stations = build_station_list()
    update_water_levels(stations)
    station = stations[0]
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=5))
    plot_water_level_with_fit(station, dates, levels, 3)