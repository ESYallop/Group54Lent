import datetime

from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level


def run():
    stations = build_station_list()
    update_water_levels(stations)
    dt = 3                 # 3 days
    output = stations_highest_rel_level(stations, 5)
    for i in output:
        date, level = fetch_measure_levels(i[0].measure_id, dt=datetime.timedelta(days=dt))
        plot_water_level_with_fit(i[0], date, level, 4)


if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
