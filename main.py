import random
import json
from SimulatedA import sA
from ClassRoute import *
from ClassCities import *
from GUI import GUI
from tkinter import *

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
R.addNeighbor(L)
R.addNeighbor(M)
R.addNeighbor(N)
R.addNeighbor(O)
R.addNeighbor(P)
R.addNeighbor(Q)

#--------------------------------------------------------TEST CASE: 4--------------------------------------------------------------------------
#CITIES: 10
#MISSING EDGES: UNKNOWN
S = City("S", 0, 10)
T = City("T", 15, 5)
U = City("U", 15, 9)
V = City("V", 20, 20)
W = City("W", 2.5, 20)
X = City("X", 5, 0)
Y = City("Y", 10, 0)
Z = City("Z", 10, 10)
A1 = City("A1", 7.5, 5)
B1 = City("B1", 15, 15)

#adding neighbors to S
S.addNeighbor(T)
S.addNeighbor(U)
S.addNeighbor(V)
S.addNeighbor(W)
S.addNeighbor(X)
S.addNeighbor(Y)
S.addNeighbor(Z)
S.addNeighbor(A1)
S.addNeighbor(B1)

#adding neighbors to T
T.addNeighbor(S)
T.addNeighbor(U)
T.addNeighbor(V)
T.addNeighbor(W)
T.addNeighbor(X)
T.addNeighbor(Y)
T.addNeighbor(Z)
T.addNeighbor(A1)
T.addNeighbor(B1)

#adding neighbors to U
U.addNeighbor(S)
U.addNeighbor(T)
U.addNeighbor(V)
U.addNeighbor(W)
U.addNeighbor(X)
U.addNeighbor(Y)
U.addNeighbor(Z)
U.addNeighbor(A1)
U.addNeighbor(B1)

#adding neighbors to V
V.addNeighbor(S)
V.addNeighbor(T)
V.addNeighbor(U)
V.addNeighbor(W)

#adding neighbors to W
W.addNeighbor(S)
W.addNeighbor(T)
W.addNeighbor(V)
W.addNeighbor(U)
W.addNeighbor(X)

#adding neighbors to X
X.addNeighbor(S)
X.addNeighbor(T)
X.addNeighbor(U)
X.addNeighbor(W)
X.addNeighbor(Y)

#adding neighbors to Y
Y.addNeighbor(S)
Y.addNeighbor(T)
Y.addNeighbor(U)
Y.addNeighbor(X)
Y.addNeighbor(Z)

#adding neighbors to Z
Z.addNeighbor(S)
Z.addNeighbor(T)
Z.addNeighbor(U)
Z.addNeighbor(Y)
Z.addNeighbor(A1)

#adding neighbors to A1
A1.addNeighbor(S)
A1.addNeighbor(T)
A1.addNeighbor(U)
A1.addNeighbor(Z)
A1.addNeighbor(B1)

#adding neighbors to B1
B1.addNeighbor(S)
B1.addNeighbor(T)
B1.addNeighbor(U)
B1.addNeighbor(A1)


#--------------------------------------------------------LEIDSCHE RIJN------------------------------------------------------------------------
#POINTS: 15

Bo = City("Bonen", 0, 13)
Di = City("Dille", 2, 13)
Wi = City("Winterkers", 4, 13)
Ka = City("Karwij", 6, 11)
Pe = City("Pepper", 8, 13)
La = City("Lavender", 10, 15)
Pi = City("Pimper", 14, 8)
Se = City("Selderie", 16, 11)
Ko = City("Koriander", 18, 6)
Bi = City("Biel", 20, 5)
Ba = City("Basilikum", 21, 4)
Mi = City("Mierikswortel", 16, 0)
Ma = City("Maanzaad", 16, 4)
Na = City("Naamloos", 10, 5)
Me = City("Melisse", 6, 2)

Bo.addNeighbor(Me)
Bo.addNeighbor(Di)

Di.addNeighbor(Bo)
Di.addNeighbor(Wi)

Wi.addNeighbor(Di)
Wi.addNeighbor(Ka)
Wi.addNeighbor(Me)

Ka.addNeighbor(Wi)
Ka.addNeighbor(Pe)
Ka.addNeighbor(Na)
Ka.addNeighbor(Me)

Pe.addNeighbor(Ka)
Pe.addNeighbor(Na)
Pe.addNeighbor(La)
Pe.addNeighbor(Me)

La.addNeighbor(Pe)
La.addNeighbor(Pi)
La.addNeighbor(Se)
La.addNeighbor(Na)

Pi.addNeighbor(La)
Pi.addNeighbor(Na)
Pi.addNeighbor(Me)
Pi.addNeighbor(Ma)
Pi.addNeighbor(Se)

Se.addNeighbor(Pi)
Se.addNeighbor(Ko)
Se.addNeighbor(La)

Ko.addNeighbor(Se)
Ko.addNeighbor(Ma)
Ko.addNeighbor(Bi)
Ko.addNeighbor(Mi)
Ko.addNeighbor(Me)

Bi.addNeighbor(Ko)
Bi.addNeighbor(Ba)
Bi.addNeighbor(Mi)
Bi.addNeighbor(Ma)

Ba.addNeighbor(Bi)
Ba.addNeighbor(Mi)

Mi.addNeighbor(Ba)
Mi.addNeighbor(Ko)
Mi.addNeighbor(Pi)
Mi.addNeighbor(Ma)
Mi.addNeighbor(Me)
Mi.addNeighbor(Na)
Mi.addNeighbor(Bi)

Ma.addNeighbor(Pi)
Ma.addNeighbor(Ko)
Ma.addNeighbor(Mi)
Ma.addNeighbor(Bi)

Na.addNeighbor(Pi)
Na.addNeighbor(Pe)
Na.addNeighbor(Mi)
Na.addNeighbor(Ka)
Na.addNeighbor(La)

Me.addNeighbor(Bo)
Me.addNeighbor(Wi)
Me.addNeighbor(Pe)
Me.addNeighbor(Pi)
Me.addNeighbor(Ko)
Me.addNeighbor(Ba)
Me.addNeighbor(Mi)
Me.addNeighbor(Ka)
#--------------------------------------------------------GENERATE RANDOM ROUTES---------------------------------------------------------------
def generateRoute(file):
    startRoute = readPoints(file)
    randomRoutes = []
    while len(randomRoutes) < 5:
        possibleRoute = Route(startRoute[:])
        random.shuffle(possibleRoute.route)
        if possibleRoute.validRoute():
            randomRoutes.append(possibleRoute)
    for i in range(len(randomRoutes)):
        randomRoutes[i].toString()
    return randomRoutes[0]

def readPoints(file):
    newRoute = []
    newRouteDict = {}
    with open(file+".json") as jsonFile:
        data = json.load(jsonFile)
        for point in data:
            for setCity in data[point]:
                c = data[point][setCity]["coordinates"]
                newCity = City(setCity, c[0], c[1])
                newRoute.append(newCity)
                newRouteDict[setCity] = newCity

            for neighborCity in data[point]:
                for n in data[point][neighborCity]:
                    if n != "coordinates" and data[point][neighborCity][n] == "1":
                        newRouteDict[neighborCity].addNeighbor(newRouteDict[n])
    return newRoute

#readPoints("5cities")
#--------------------------------------------------------ROUTE SETUP--------------------------------------------------------------------------
route1 = generateRoute("5cities")#([A, B, C, D, E])
route2 = generateRoute("6cities")#([F, G, H, I, J, K])#Route([F, G, H, I, J, K])
route3 = generateRoute("7cities")#([L, M, N, O, P, Q, R])#Route([L, O, N, M, R, Q, P])
route4 = generateRoute("10cities")#([S, T, U, V, W, X, Y, Z, A1, B1])#Route([A1, U, S, B1, V, W, X, Y, T, Z])
#route5 = generateRoute([Bo, Di, Me, Na, Ka, Pe, La, Pi, Se, Ko, Ma, Bi, Ba, Mi, Wi])#([Me, Bo, Di, Wi, Ka, Na, Pe, La, Pi, Se, Ko, Ma, Bi, Ba, Mi])
routes = {"5":route1, "6":route2, "7":route3, "10":route4}

for key in routes:
    routes[key].totalDistance()

#--------------------------------------------------------GUI SETUP--------------------------------------------------------------------------
newGui = GUI("Strooi Wagens", "1000x600", routes)
newGui.home()
newGui.root.mainloop()




