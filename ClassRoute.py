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
        #total += self.route[0].distance(self.route[-1])
        self.distance = total

    def toString(self):
        names = []
        for i in range(len(self.route)):
            names.append(self.route[i].name)
        print(names)

    def connectionAmt(self):
        connections = 0
        route = self.route
        for city in route:
            connections += len(city.neighbors)
        return connections

    def validRoute(self):
        route = self.route
        for i in range(len(route) - 1):
            if route[i] not in route[i + 1].neighbors:
                return False
        return True


