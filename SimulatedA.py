import random
import time
from ClassRoute import Route

'''
This module contains the algorithm for Simulated Annealing + Two Opt 
'''

def swap(r, i, j):
    """
    :param r: route
    :param i: index
    :param j: index
    :type r: Route
    :type i: integer
    :type j: integer
    :return: void, function swaps the values on index i and index j with eachother
    """
    temp = r[i]
    r[i] = r[j]
    r[j] = temp


def randomIndexes(rand):
    """
    :param rand: range for random.randrange()
    :type rand: integer
    :return: index i and index j
    :rtype: integer
    """
    i = random.randrange(rand)
    j = random.randrange(rand)

    #making sure that i and j are not equal to each other
    #to prevent swapping the same value with itself
    while(i == j):
        j = random.randrange(rand)
    return i, j


def swapCheck(newR, i, j):
    """
    :param newR: new route
    :param i: index i
    :param j: index j
    :type newR: Route
    :type i: integer
    :type j: integer
    :return: void. Function will keep swapping values until a valid route has been made
    """
    swapFound = False
    counter = 0

    #keeps swapping until the route is valid
    while not swapFound and counter < (len(newR.route)*2):
        counter += 1
        swap(newR.route, i, j)
        i, j = randomIndexes(len(newR.route))
        swap(newR.route, i, j)
        swapFound = newR.validRoute()

    if not swapFound:
        swap(newR.route, i, j)



def sA(startRoute):
    """
    :param startRoute: route to improve
    :type startRoute: Route
    :return: returns an improved version of the startRoute and the time it took to find this improved version
    :rtype: Route, float
    """
    startTime = time.monotonic()
    Temp = 1000*len(startRoute.route)
    currentBest = startRoute
    bestRoute = startRoute
    while(Temp > 1):
        #creating a new route to hopefully improve
        newRoute = Route(currentBest.route[:])

        #swapping until a valid route has been made
        i, j = randomIndexes(len(newRoute.route))
        swap(newRoute.route, i, j)
        if not newRoute.validRoute():
            swapCheck(newRoute, i, j)

        newRoute.totalDistance()
        distantDifference = currentBest.distance - newRoute.distance
        acceptance = 1/(10+(distantDifference/Temp)**2)

        #algorithm picks a better solution
        #or a worse solution
        #this is determined by acceptance
        if distantDifference > 0:
            currentBest = newRoute
        elif acceptance > random.uniform(0, 1):
            currentBest = newRoute

        if currentBest.distance < bestRoute.distance:
            bestRoute = currentBest

        decrease = 1
        Temp -= decrease

    bestRoute.toString()
    return bestRoute, time.monotonic()-startTime





