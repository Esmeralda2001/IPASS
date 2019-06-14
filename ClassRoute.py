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
        self.distance = total


