import math

class City:
    """
    This module contains the 'City' class
    It is primarily used by the 'Route' class
    """

    def __init__(self, name, posx, posy):
        """
        :param name: name of the city
        :param posx: x-coordinate of the city
        :param posy: y-coordinate of the city
        :type name: basestring
        :type posx: integer
        :type posy: integer
        """
        self.name = name
        self.x = posx
        self.y = posy
        self.neighbors = []

    def distance(self, city):
        """
        :param city: a city
        :type city: City
        :return: the distance between 'self' and another instance of the City Class
        :rtype: float
        """
        xAxis = (self.x-city.x)**2
        yAxis = (self.y-city.y)**2
        dist = math.sqrt(xAxis+yAxis)
        return dist

    def addNeighbor(self, city):
        """
        :param city: a city
        :type city: City
        :return: returns void, function simply adds an instance of the City Class to self.neighbors
        """
        self.neighbors.append(city)

