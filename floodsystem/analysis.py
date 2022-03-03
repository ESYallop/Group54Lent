import matplotlib
import matplotlib.dates
import numpy as np
import datetime
from .datafetcher import fetch_measure_levels
from .utils import sorted_by_key

def polyfit(dates, levels, p):
    x0 = []
    for i in dates:
        x0.append(matplotlib.dates.date2num(i)) #converting date to float here
    x1 = []
    for i in x0:
        x1.append(i - x0[0])    # makes a list of dates shifted to a reasonable number
    poly_coeff = np.polyfit(x1, levels, p)   # fits the data to a polynomial of degree p
    poly = np.poly1d(poly_coeff)     # converts to a useful data type, poly1d
    return poly, x0[0]      # returns the polyfit and the date shift

def rising_gradient(pol, d0, x):   
    grad_poly = np.polyder(pol)
    grad = grad_poly (x - d0)
    if grad > 0: 
        return True
    else :
        return False   