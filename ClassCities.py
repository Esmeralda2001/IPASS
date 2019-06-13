class City:
    def __init__(self, name, posx, posy):
        self.name = name
        self.x = posx
        self.y = posy

    def distance(self):
        return self.x