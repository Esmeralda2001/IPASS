import math

class City:
    #constructor function of class 'City'
    #city has the following properties: name, x, y
    #name is a string
    #x and y are the coordinates of the city
    def __init__(self, name, posx, posy):
        self.name = name
        self.x = posx
        self.y = posy
        self.neighbors = []

    #function distance calculates the distance between
    #a city and another city
    def distance(self, city):
        xAxis = (self.x-city.x)**2
        yAxis = (self.y-city.y)**2
        dist = math.sqrt(xAxis+yAxis)
        return dist

    def addNeighbor(self, city):
        self.neighbors.append(city)

    def getNeighbors(self, arr):
        for i in range(2):
            closestDist = 1000
            closestCity = None

            for city in arr:
                newDist = self.distance(city)
                if city != self and newDist < closestDist and not (city in self.neighbors):
                      closestCity = city
                      closestDist = newDist
            if closestCity is not None:
                self.neighbors.append(closestCity)
                closestCity.neighbors.append(self)
