from SimulatedA import sA
from ClassRoute import *
from ClassCities import *
from GUI import drawRoute

#--------------------------------------------------------TEST CASE: 1--------------------------------------------------------------------------
#CITIES: 5
#MISSING EDGES: 1

#city set-up
A = City("A", 0, 10)
B = City("B", 10, 20)
C = City("C", 15, 10)
D = City("D", 20, 10)
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
route1 = Route([A, B, E, C, D])
drawRoute(route1.route)
route1.totalDistance()
#print(route1.distance)

route1 = sA(route1)
drawRoute(route1.route)

#--------------------------------------------------------TEST CASE: 2--------------------------------------------------------------------------
#CITIES: 6
#MISSING EDGES: 2
#city set-up
F = City("F", 0, 10)
G = City("G", 10, 15)
H = City("H", 15, 10)
I = City("I", 10, 10)
J = City("J", 5, 0)
K = City("K", 10, 0)

#adding neighbors to city F
F.addNeighbor(G)
F.addNeighbor(H)
F.addNeighbor(I)
F.addNeighbor(J)
F.addNeighbor(K)

#adding neighbors to city G
G.addNeighbor(F)
G.addNeighbor(K)
G.addNeighbor(H)

#adding neighbors to city H
H.addNeighbor(F)
H.addNeighbor(G)
H.addNeighbor(I)
H.addNeighbor(J)
H.addNeighbor(K)

#adding neighbors to city I
I.addNeighbor(F)
I.addNeighbor(H)
I.addNeighbor(J)
I.addNeighbor(K)

#adding neighbors to city J
J.addNeighbor(F)
J.addNeighbor(H)
J.addNeighbor(I)
J.addNeighbor(K)

#adding neighbors to city K
K.addNeighbor(F)
K.addNeighbor(G)
K.addNeighbor(H)
K.addNeighbor(I)
K.addNeighbor(J)

#route set-up
route2 = Route([F, G, H, I, J, K])
route2.totalDistance()
#print(route2.distance)
#sA(route2)

#--------------------------------------------------------TEST CASE: 3--------------------------------------------------------------------------
#CITIES: 7
#MISSING EDGES: 3
L = City("L", 0, 10)
M = City("M", 10, 15)
N = City("N", 15, 10)
O = City("O", 10, 10)
P = City("P", 2.5, 0)
Q = City("Q", 5, 0)
R = City("R", 10, 0)

#adding neighbors to L
L.addNeighbor(M)
L.addNeighbor(N)
L.addNeighbor(O)
L.addNeighbor(P)
L.addNeighbor(Q)
L.addNeighbor(R)

#adding neighbors to M
M.addNeighbor(L)
M.addNeighbor(N)
M.addNeighbor(Q)
M.addNeighbor(R)

#adding neighbors to N
N.addNeighbor(L)
N.addNeighbor(M)
N.addNeighbor(O)
N.addNeighbor(Q)
N.addNeighbor(R)

#adding neighbors to O
O.addNeighbor(L)
O.addNeighbor(N)
O.addNeighbor(P)
O.addNeighbor(Q)
O.addNeighbor(R)

#adding neighbors to P
P.addNeighbor(L)
P.addNeighbor(O)
P.addNeighbor(Q)
P.addNeighbor(R)

#adding neighbors to Q
Q.addNeighbor(L)
Q.addNeighbor(M)
Q.addNeighbor(N)
Q.addNeighbor(O)
Q.addNeighbor(P)
Q.addNeighbor(R)

#adding neighbors to R
Q.addNeighbor(L)
Q.addNeighbor(M)
Q.addNeighbor(N)
Q.addNeighbor(O)
Q.addNeighbor(P)
Q.addNeighbor(Q)

#route set-up
route3 = Route([L, O, N, M, R, Q, P])
route3.totalDistance()
print(route3.distance)
drawRoute(route3.route)
route3 = sA(route3)
drawRoute(route3.route)
route3.toString()

