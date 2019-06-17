from ClassRoute import Route
from Utility import *

def twoOpt(initialRoute):
    route = initialRoute.route
    newRoute = Route(route[:])
    for i in range(len(route)-2):
        for j in range(len(route)):
            d1 = route[j].distance(route[i+1])
            d2 = route[j].distance(route[i+2])

            if d1 > d2:
                print(d1, d2)
                swap(newRoute.route, i+2, i+1)

    newRoute.totalDistance()
    print(newRoute.distance)
    if newRoute.distance < initialRoute.distance:
        return newRoute
    else:
        return initialRoute

