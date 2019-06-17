import random
import time
from Utility import *
from ClassCities import City
from ClassRoute import Route
from TwoOpt import *

#temporary city set-up
A = City("A", 0, 10)
B = City("B", 10, 0)
C = City("C", 10, 10)
D = City("A", 5, 15)
E = City("B", 10, 15)
F = City("C", 20, 10)
G = City("A", 2, 10)
H = City("B", 10, 20)
I = City("C", 20, 20)
J = City("A", 6, 10)
K = City("B", 10, 7)
L = City("C", 15, 10)
M = City("A", 15, 35)
N = City("B", 25, 30)
O = City("C", 25, 40)
P = City("A", 25, 65)
Q = City("B", 47, 14)
R = City("C", 20, 40)
S = City("A", 27, 30)
T = City("B", 33, 20)
U = City("C", 35, 20)
V = City("A", 1, 20)
W = City("B", 10, 37)
X = City("C", 15, 16)

#route set-up
route = Route([A, B, C, D, E, F, G, H, I, J, K, L])#, M, N, O, P, Q, R, S, T, U, V, W, X])
route.totalDistance()
print(route.distance)


def randomIndexes(rand):
    i = random.randrange(rand)
    j = random.randrange(rand)

    while(i == j):
        j = random.randrange(rand)
    return i, j


def sA(startRoute):
    startTime = time.monotonic()
    Temp = 10000*len(startRoute.route)
    currentBest = startRoute
    bestRoute = startRoute
    while(Temp > 0):
        #print(currentBest.distance)
        newRoute = Route(currentBest.route[:])

        i, j = randomIndexes(len(newRoute.route))
        swap(newRoute.route, i, j)

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
    bestRoute = twoOpt(bestRoute)
    print("Best route after TwoOpt", bestRoute.distance)
    print("Elapsed time", time.monotonic()-startTime)

sA(route)




