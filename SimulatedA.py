import random
import time
from Utility import *
from ClassCities import City
from ClassRoute import Route
from TwoOpt import *


def randomIndexes(rand):
    i = random.randrange(rand)
    j = random.randrange(rand)

    while(i == j):
        j = random.randrange(rand)
    return i, j


def swapCheck(newR, i, j):
    swapFound = False
    counter = 0

    while not swapFound and counter < 5000:
        counter += 1
        swap(newR.route, i, j)
        i, j = randomIndexes(len(newR.route))
        swap(newR.route, i, j)

        if i == 0 and j < len(newR.route) - 1:
            if (newR.route[i] in newR.route[i + 1].neighbors) and (
                    newR.route[j] in newR.route[j + 1].neighbors) and (
                    newR.route[j] in newR.route[j - 1].neighbors):
                swapFound = True
        elif i == 0 and j == len(newR.route) - 1:
            if (newR.route[i] in newR.route[i + 1].neighbors) and (
                    newR.route[j] in newR.route[j - 1].neighbors):
                swapFound = True
        elif j == 0 and i == len(newR.route) - 1:
            if (newR.route[i] in newR.route[i - 1].neighbors) and (
                    newR.route[j] in newR.route[j + 1].neighbors):
                swapFound = True
        elif j > 0 and i == len(newR.route) - 1:
            if (newR.route[i] in newR.route[i - 1].neighbors) and (
                    newR.route[j] in newR.route[j + 1].neighbors) and (
                    newR.route[j] in newR.route[j - 1].neighbors):
                swapFound = True
        elif i > 0 and j == len(newR.route) - 1:
            if (newR.route[i] in newR.route[i - 1].neighbors) and (
                    newR.route[i] in newR.route[i + 1].neighbors) and (
                    newR.route[j] in newR.route[j - 1].neighbors):
                swapFound = True
        elif j == 0 and i < len(newR.route) - 1:
            if (newR.route[j] in newR.route[j + 1].neighbors) and (
                    newR.route[i] in newR.route[i + 1].neighbors) and (
                    newR.route[i] in newR.route[i - 1].neighbors):
                swapFound = True
        elif j > 0 and i < len(newR.route) - 1:
            if (newR.route[j] in newR.route[j + 1].neighbors) and (
                    newR.route[j] in newR.route[j - 1].neighbors) and (
                    newR.route[i] in newR.route[i + 1].neighbors) and (
                    newR.route[i] in newR.route[i - 1].neighbors):
                swapFound = True

    if not swapFound:
        swap(newR.route, i, j)


def sA(startRoute):
    startTime = time.monotonic()
    Temp = 10000*len(startRoute.route)
    currentBest = startRoute
    bestRoute = startRoute
    while(Temp > 1):
        #print(currentBest.distance)
        newRoute = Route(currentBest.route[:])

        i, j = randomIndexes(len(newRoute.route))
        swap(newRoute.route, i, j)

        swapCheck(newRoute, i, j)

        newRoute.toString()
        newRoute.totalDistance()
        distantDifference = currentBest.distance - newRoute.distance
        #acceptance might need some work too
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

        #decrease of temperature. this might still need some work but i have a difficult time
        #finding a suitable function for this
        decrease = 10*0.3
        Temp -= decrease

    print("Best route before TwoOpt", bestRoute.distance)
    #bestRoute = twoOpt(bestRoute)
    print("Best route after TwoOpt", bestRoute.distance)
    print("Elapsed time", time.monotonic()-startTime)
    bestRoute.toString()





