import random
import json
from SimulatedA import sA
from ClassRoute import *
from ClassCities import *
from GUI import GUI
from tkinter import *
#--------------------------------------------------------GENERATE RANDOM ROUTES---------------------------------------------------------------
def generateRoute(file, num):
    startRoute = readPoints(file)
    randomRoutes = []
    while len(randomRoutes) < num:
        possibleRoute = Route(startRoute[:])
        random.shuffle(possibleRoute.route)
        if possibleRoute.validRoute():
            randomRoutes.append(possibleRoute)
    return shortestRoute(randomRoutes)

def readPoints(file):
    newRoute = []
    newRouteDict = {}
    with open(file+".json") as jsonFile:
        data = json.load(jsonFile)
        for point in data:
            for setCity in data[point]:
                c = data[point][setCity]["coordinates"]
                newCity = City(setCity, c[0], c[1])
                newRoute.append(newCity)
                newRouteDict[setCity] = newCity

            for neighborCity in data[point]:
                for n in data[point][neighborCity]:
                    if n != "coordinates" and data[point][neighborCity][n] == "1":
                        newRouteDict[neighborCity].addNeighbor(newRouteDict[n])
    print(Route(newRoute).connectionAmt())
    return newRoute

def shortestRoute(currRoutes):
    r = 0
    routeDist = 1000

    for route in currRoutes:
        route.totalDistance()
        if route.distance < routeDist:
            r = route
            routeDist = route.distance
    return r

#readPoints("5cities")
#--------------------------------------------------------ROUTE SETUP--------------------------------------------------------------------------
route1 = generateRoute("5cities", 5)
route2 = generateRoute("6cities", 5)
route3 = generateRoute("7cities", 5)
route4 = generateRoute("10cities", 5)
route5 = generateRoute("LeidscheRijn", 3)

routes = {"5":route1, "6":route2, "7":route3, "10":route4, "LeidscheRijn":route5}

for key in routes:
    routes[key].totalDistance()

#--------------------------------------------------------GUI SETUP--------------------------------------------------------------------------
newGui = GUI("Strooi Wagens", "1000x600", routes)
newGui.home()
newGui.root.mainloop()




