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

    #function distance calculates the distance between
    #a city and another city
    def distance(self, city):
        xAxis = (self.x-city.x)**2
        yAxis = (self.y-city.y)**2
        dist = math.sqrt(xAxis+yAxis)
        return dist