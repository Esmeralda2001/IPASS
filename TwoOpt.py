from ClassRoute import Route
from Utility import *

def twoOpt(initialRoute):
    route = initialRoute.route
    newRoute = Route(route[:])
    for i in range(len(route)-2):
        for j in range(len(route)):
            d1 = route[i].distance(route[i+1])
            d2 = route[i+1].distance(route[i+2])

            if d1 > d2:
                tempRoute = Route(newRoute.route[:])
                swap(tempRoute.route, i+2, i+1)
                tempRoute.totalDistance()
                newRoute.totalDistance()
                #print(newRoute.distance, tempRoute.distance)
                if tempRoute.distance < newRoute.distance:
                    swap(newRoute.route, i+2, i+1)

    newRoute.totalDistance()
    if newRoute.distance < initialRoute.distance:
        return newRoute
    else:
        return initialRoute

def test():
    print("test")