import random
import time
from ClassCities import City
from ClassRoute import Route

#swap function
#swaps two cities with eachother
def swap(r, i, j):
    temp = r[i]
    r[i] = r[j]
    r[j] = temp

#finds two random indexes
def randomIndexes(rand):
    i = random.randrange(rand)
    j = random.randrange(rand)

    while(i == j):
        j = random.randrange(rand)
    return i, j

#checks if a swap is valid or not
#a swap is valid if the order of the elements in the array
#are all connected to eachother properly
def swapCheck(newR, i, j):
    swapFound = False
    counter = 0

    while not swapFound and counter < (len(newR.route)*2):
        counter += 1
        swap(newR.route, i, j)
        i, j = randomIndexes(len(newR.route))
        swap(newR.route, i, j)

        #many if-statements to account for the first/last element being swapped
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

    #reverts the swap if no valid swap was found
    if not swapFound:
        swap(newR.route, i, j)


def sA(startRoute):
    startTime = time.monotonic()
    Temp = 1000*len(startRoute.route)
    currentBest = startRoute
    bestRoute = startRoute
    while(Temp > 1):
        newRoute = Route(currentBest.route[:])

        i, j = randomIndexes(len(newRoute.route))
        swap(newRoute.route, i, j)

        swapCheck(newRoute, i, j)

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

        decrease = 1
        Temp -= decrease


    return bestRoute, time.monotonic()-startTime





