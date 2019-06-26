import math

class City:

    def __init__(self, name, posx, posy):
        '''
        :param name: string, name of the city
        :param posx: integer, x-coordinate of the city
        :param posy: integer, y-coordinate of the city
        '''
        self.name = name
        self.x = posx
        self.y = posy
        self.neighbors = []

    def distance(self, city):
        '''
        :param city: city is a part of the City Class
        :return: the distance between 'self' and another instance of the City Class
        '''
        xAxis = (self.x-city.x)**2
        yAxis = (self.y-city.y)**2
        dist = math.sqrt(xAxis+yAxis)
        return dist

    def addNeighbor(self, city):
        '''
        :param city: city is part of the City Class
        :return: returns void, function simply adds an instance of the City Class to self.neighbors
        '''
        self.neighbors.append(city)

