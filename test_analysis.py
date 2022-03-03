import datetime
import numpy as np
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit, rising_gradient

def test_polyfit():
    x = np.linspace(0.1,1,100)
    y = x
    p, d0 = polyfit(x,y,1)

def test_rising_gradient():
    pol = np.poly1d([1,2,1])
    assert rising_gradient(pol,2,0) == False
    assert rising_gradient(pol,2,2) == True
    