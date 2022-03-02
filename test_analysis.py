import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit

def test_polyfit():
    stations = build_station_list()
    update_water_levels(stations)
    station = stations[0]
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=10))
    poly, d0 = polyfit(dates, levels, 4)