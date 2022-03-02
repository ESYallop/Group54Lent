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

def derivSolve(station, a, p, now):     # Finds the derivatives of a set of data
    try:
        dates, levels = fetch_measure_levels(station.measure_id, dt=a)
        poly, d0 = polyfit(dates, levels, p)    # Creating the polynomial
        polyder1 = poly.deriv()     # Getting the actual derivative
        polyder2 = polyder1.deriv()
        return tuple((station, polyder1(now), polyder2(now)))
    except:
        return None


def derivativesSolve(stations, dt, p):      # Gets the first and second derivatives of all stations inputted
    derivList = []
    now = matplotlib.dates.date2num(datetime.datetime.now()) 
    a = datetime.timedelta(days=dt)
    counter = 0
    for station in stations:
        counter += 1
        print(counter)
        if counter > 20:
            break
        try:
            x = derivSolve(station, a, p, now)
            derivList.append(x)
        except:
            print("error {}".format(station.name))
    return sorted_by_key(derivList, 2, reverse=True)    # Returns a list of stations and derivatives sorted by max derivative

def level_predictor(dates, levels, p, dtf):     # Returns the extended values of the polynomial into the future
    #dtf is number of days forward
    dtfm = round(dtf * 96)

    dif = dates[0]-dates[1]
    datef = [dates[0]]
    for i in range(dtfm):       # Gets the dates of the future time
        datef.insert(0, datef[0]+dif)
    
    poly, d0 = polyfit(dates, levels, p)    # Finds the polynomial of old dates
    x0 = matplotlib.dates.date2num(datef)
    x1 = np.linspace(x0[0], x0[-1], 30)
    predictLevel = poly(x1 - d0)        # Using polynomial of old dates gets future dates
    print(predictLevel)
    return (predictLevel)

def risk_calculator(stationList, dt, p, p2, dtf):   # Finds risk level for the objects
    for station in stationList:
        """try:
            dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
            print("a")
            futureHeights = level_predictor(dates, levels, p, dtf)      # Finds the predicted heights 
            print("b")
            maxHeight = max(futureHeights)      # Finds the maximum height in the time frame
            print("c")
            maxRelative1 = station.relative_water_level(maxHeight)
            print("d")
            futureHeights = level_predictor(dates, levels, p2, dtf)     # Repeats the same thing with differnt number of polynomials
            print("e")
            maxHeight = max(futureHeights)
            print("f")
            maxRelative2 = station.relative_water_level(maxHeight)
            if maxRelative1 > maxRelative2:     # Uses the highest realtive level
                maxRelative = maxRelative1
            else:
                maxRelative = maxRelative2
            if maxRelative > 2:     #  And assigns a risk level
                station.risk = 0
            elif maxRelative > 1:
                station.risk = 1
            elif maxRelative > 0.5:
                station.risk = 2
            else:
                station.risk = 3
        except:
            pass"""
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        if dates == []:
            pass
        else:
            print("a")
            futureHeights = level_predictor(dates, levels, p, dtf)      # Finds the predicted heights 
            print("b")
            maxHeight = max(futureHeights)      # Finds the maximum height in the time frame
            print("c")
            maxRelative1 = station.latest_level/maxHeight
            print("d")
            futureHeights = level_predictor(dates, levels, p2, dtf)     # Repeats the same thing with differnt number of polynomials
            print("e")
            maxHeight = max(futureHeights)
            print("f")
            maxRelative2 = station.latest_level/maxHeight

            if maxRelative1 > maxRelative2:     # Uses the highest realtive level
                maxRelative = maxRelative1
            else:
                maxRelative = maxRelative2
            if maxRelative > 2:     #  And assigns a risk level
                station.risk = 0
            elif maxRelative > 1:
                station.risk = 1
            elif maxRelative > 0.5:
                station.risk = 2
            else:
                station.risk = 3    