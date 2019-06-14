import math

class City:
    def __init__(self, name, posx, posy):
        self.name = name
        self.x = posx
        self.y = posy

    def distance(self, city):
        xAxis = (self.x-city.x)**2
        yAxis = (self.y-city.y)**2
        dist = math.sqrt(xAxis+yAxis)
        return dist