import random
from ClassCities import City
from ClassRoute import Route

#temporary city set-up
A = City("A", 0, 10)
B = City("B", 10, 0)
C = City("C", 10, 10)

#route set-up
route = Route([A, B, C])
route.totalDistance()
print(route.distance)

#swap function
#swaps two cities with eachother
def swap(r, i, j):
    temp = r.route[i]
    r.route[i] = r.route[j]
    r.route[j] = temp

def randomIndexes(rand):
    i = random.randrange(rand)
    j = random.randrange(rand)

    while(i == j):
        j = random.randrange(rand)
    return i, j


def sA(startRoute):
    T = 10000
    while(T > 0):
        newRoute = startRoute[:]



