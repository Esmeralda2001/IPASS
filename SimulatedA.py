import random
from ClassCities import City
from ClassRoute import Route

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
M = City("A", 15, 25)
N = City("B", 25, 0)
O = City("C", 25, 10)
P = City("A", 25, 15)
Q = City("B", 17, 14)
R = City("C", 20, 30)
S = City("A", 27, 10)
T = City("B", 13, 20)
U = City("C", 30, 20)
V = City("A", 3, 10)
W = City("B", 10, 7)
X = City("C", 15, 10)

#route set-up
route = Route([A, B, C, D, E, F, G, H, I, J, K, L])
route.totalDistance()
print(route.distance)

#swap function
#swaps two cities with eachother
def swap(r, i, j):
    temp = r[i]
    r[i] = r[j]
    r[j] = temp

def randomIndexes(rand):
    i = random.randrange(rand)
    j = random.randrange(rand)

    while(i == j):
        j = random.randrange(rand)
    return i, j


def sA(startRoute):
    Temp = 100000
    currentBest = startRoute
    while(Temp > 0):
        print(currentBest.distance)
        newRoute = Route(currentBest.route[:])

        i, j = randomIndexes(len(newRoute.route))
        swap(newRoute.route, i, j)

        newRoute.totalDistance()
        distantDifference = currentBest.distance - newRoute.distance
        #prob = 
        if distantDifference > 0:
            currentBest = newRoute
        elif (distantDifference/Temp) > random.uniform(0, 1):
            print("passing")
            currentBest = newRoute

        #print(T)
        decrease = 10*0.3
        Temp -= decrease



sA(route)




