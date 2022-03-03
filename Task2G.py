import datetime
import numpy as np
import matplotlib
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.analysis import polyfit, rising_gradient


def run():
    stations = build_station_list()
    update_water_levels(stations)

    #get rid of stations which are likely not at risk so less to analyse
    threat_stations = stations_highest_rel_level(stations, 50)

    severe = []
    high = []
    moderate = []
    low = []
    failed_stations = []

    for station in threat_stations:
        dt = 2 
        dates, levels = fetch_measure_levels(station.measure_id, dt = datetime.timedelta(days = dt))
        pol = None
        d0 = None

        if dates == []:
            failed_stations.append(station.name)
            continue
        else:
            pol, d0 = polyfit(dates, levels, 4)

        x = datetime.datetime.now()
        y = matplotlib.dates.date2num(x) + 1
        
        if rising_gradient(pol, d0, y):
            if station.relative_water_level() >= 2:
                severe.append(station)
            elif station.relative_water_level() >= 1.5:
                high.append(station)
            elif station.relative_water_level() >= 1:
                moderate.append(station)
            else:
                low.append(station)
        else:
            low.append(station) 

    print("Severe:", str(set(station.town for station in severe)))
    print("High:", str(set(station.town for station in high)))
    print("Moderate:", str(set(station.town for station in moderate)))
    print("Low:", str(set(station.town for station in low)))
    print("Failed stations:", str((failed_stations)))

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
