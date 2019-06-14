class Route:
    def __init__(self, route):
        self.route = route
        self.size = 0


    def totalDistance(self):
        total = 0
        for i in range(len(self.route)-1):
            c1 = self.route[i]
            c2 = self.route[i+1]

            total += c1.distance(c2)