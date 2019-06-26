class Route:
    """
    This module contains the 'Route Class'
    An instance of Route has a list that contains instances of class City
    """

    def __init__(self, route):
        """
        :param route: a list containing instances of class 'City'
        """
        self.route = route
        self.distance = 0

    def totalDistance(self):
        """
        :return: returns void, sets the total distance.
        Total distance = distance from the first City to the second City, added to the distance between the second and third City, etc.
        """
        total = 0
        for i in range(len(self.route)-1):
            c1 = self.route[i]
            c2 = self.route[i+1]
            total += c1.distance(c2)
        self.distance = total

    def toString(self):
        """
        :return: returns void. Function puts the name of each City into a list and prints it
        """
        names = []
        for i in range(len(self.route)):
            names.append(self.route[i].name)
        print(names)

    def connectionAmt(self):
        """
        :return: returns the total amount of connections of all Cities combined. Connections = amount of neighbors per City
        :rtype: integer
        """
        connections = 0
        route = self.route
        for city in route:
            connections += len(city.neighbors)
        return connections

    def validRoute(self):
        """
        :return: returns if the Route is a valid route or not.
        A route is valid if the first City in the route is the neighbor of the second City and if the second City is the neighbor of the third City etc.
        :rtype: bool
        """
        route = self.route
        for i in range(len(route) - 1):
            if route[i] not in route[i + 1].neighbors:
                return False
        return True


