from SimulatedA import sA
from ClassRoute import *
from ClassCities import *

#--------------------------------------------------------TEST CASE: 1--------------------------------------------------------------------------
#CITIES: 5
#MISSING EDGES: 1

#city set-up
A = City("A", 0, 10)
B = City("B", 10, 15)
C = City("C", 15, 10)
D = City("D", 10, 10)
E = City("E", 10, 0)

#adding neighbors to city A
A.addNeighbor(B)
A.addNeighbor(E)
A.addNeighbor(D)
A.addNeighbor(C)

#adding neighbors to city B
B.addNeighbor(A)
B.addNeighbor(C)
B.addNeighbor(E)

#adding neighbors to city C
C.addNeighbor(A)
C.addNeighbor(B)
C.addNeighbor(D)
C.addNeighbor(E)

#adding neighbors to city D
D.addNeighbor(A)
D.addNeighbor(C)
D.addNeighbor(E)

#adding neighbors to city E
E.addNeighbor(A)
E.addNeighbor(B)
E.addNeighbor(C)
E.addNeighbor(D)

#route set-up
route = Route([A, B, E, C, D])
route.totalDistance()
print(route.distance)

sA(route)