from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import risk_calculator
from floodsystem.flood import stations_highest_rel_level


def run():
    stations = build_station_list()
    update_water_levels(stations)

    N = 100      # Number of stations to test, due to long processing time
    dt = 4      # Days in the past to base prediction off
    dtf = 1     # Days forward to predict
    p = 4       # Number of polynimial
    p2 = 2
    relLevel = stations_highest_rel_level(stations, N)  # Get just the top 100 stations based on relative level
    stationList = []
    for relatives in relLevel:      # Getting the stations
        stationList.append(relatives[0])

    risk_calculator(stationList, dt, p, p2, dtf)    # Creates the risk levels for the objects

    townDict = {}
    for j in stations:      # Makes a dictionary of the towns using the highest risk as the towns risk
        if j.risk is not None:
            if j.town in townDict:
                if j.risk < townDict[j.town]:
                    townDict[j.town] = j.risk
            else:
                townDict[j.town] = j.risk
    riskAlert = ['Severe', 'High', 'Moderate', 'Low']       # Used to convert risk level as number to word

    for town in sorted(townDict, key=townDict.get):         # Prints a sorted list of towns and risk level
        print(town, riskAlert[townDict[town]])

if __name__ == "__main__":
    print("*** Task 1G: CUED Part IA Flood Warning System ***")
    run()
