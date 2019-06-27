import random
import json
from SimulatedA import sA
from ClassRoute import *
from ClassCities import *
from GUI import GUI
from tkinter import *
#--------------------------------------------------------GENERATE RANDOM ROUTES---------------------------------------------------------------
def generateRoute(file, num):
    """
    :param file: file used to generate a route
    :param num: amount of routes to generate
    :type file: JSON-file
    :type num: integer
    :return: returns the shortest route out of all generated routes
    :rtype: Route
    """
    startRoute = readPoints(file)
    randomRoutes = []
    while len(randomRoutes) < num:
        possibleRoute = Route(startRoute[:])
        random.shuffle(possibleRoute.route)
        if possibleRoute.validRoute():
            randomRoutes.append(possibleRoute)
    return shortestRoute(randomRoutes)

def readPoints(file):
    """
    :param file: file used to generate a Route
    :type file: JSON-file
    :return: new route
    :rtype: Route
    """
    newRoute = []
    newRouteDict = {}
    with open(file+".json") as jsonFile:
        data = json.load(jsonFile)
        for point in data:
            #making instances of class City
            for setCity in data[point]:
                c = data[point][setCity]["coordinates"]
                newCity = City(setCity, c[0], c[1])
                newRoute.append(newCity)
                #adding the City to a dictionary
                #so that it's possible to later on add this City easily to another City as a neighbor
                newRouteDict[setCity] = newCity

            #adding neighbors to City
            for neighborCity in data[point]:
                for n in data[point][neighborCity]:
                    if n != "coordinates" and data[point][neighborCity][n] == "1":
                        newRouteDict[neighborCity].addNeighbor(newRouteDict[n])
    print(Route(newRoute).connectionAmt())
    return newRoute

def shortestRoute(currRoutes):
    """
    :param currRoutes: current routes
    :type currRoutes: list containing several instances of Route
    :return: smallest route is returned
    :rtype: Route
    """
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
route1 = generateRoute("TestCases/5cities", 5)
route2 = generateRoute("TestCases/6cities", 5)
route3 = generateRoute("TestCases/7cities", 5)
route4 = generateRoute("TestCases/10cities", 5)
route5 = generateRoute("TestCases/LeidscheRijn", 3)

#dictionary containing several generated routes
routes = {"5":route1, "6":route2, "7":route3, "10":route4, "LeidscheRijn":route5}

#pre-calculating each route's totalDistance
for key in routes:
    routes[key].totalDistance()

#--------------------------------------------------------GUI SETUP--------------------------------------------------------------------------
newGui = GUI("Strooi Wagens", "1000x600", routes)
newGui.home()
newGui.root.mainloop()




