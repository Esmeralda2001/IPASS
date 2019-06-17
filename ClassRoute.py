class Route:
    #constructor function for class 'Route'
    #route has a property 'distance'
    #which is the total distance you would travel if you were to take this route
    def __init__(self, route):
        self.route = route
        self.distance = 0


    #function to calculate the total distance of this route
    #distance between each city is calculated and added to the total
    def totalDistance(self):
        total = 0
        for i in range(len(self.route)-1):
            c1 = self.route[i]
            c2 = self.route[i+1]
            total += c1.distance(c2)
        total += self.route[0].distance(self.route[-1])
        self.distance = total

    def setNeighbors(self):
        route = self.route
        for i in range(len(route)):
            route[i].getNeighbors(route)

    def sortRoute(self):
        route = self.route
        sortedRoute = []
        for i in range(len(route)):
            if i == 0:
                sortedRoute.append(route[i])
            else:
                print("------------------")
                print(sortedRoute[i-1].name, ":")
                neighbors = sortedRoute[i-1].neighbors
                closestNeighbor = neighbors[0]
                closestNeighborDist = 1000
                for j in range(len(neighbors)):
                    print(neighbors[j].name)
                    newDist = sortedRoute[i-1].distance(neighbors[j])
                    if newDist < closestNeighborDist and not neighbors[j] in sortedRoute:
                        closestNeighbor = neighbors[j]
                        closestNeighborDist = newDist
                sortedRoute.append(closestNeighbor)
        self.route = sortedRoute

    def toString(self):
        names = []
        for i in range(len(self.route)):
            names.append(self.route[i].name)
        print(names)


