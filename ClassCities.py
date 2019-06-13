class City:
    def _init_(self, name, posx, posy):
        self.name = name
        self.x = posx
        self.y = posy

    def distance(self):
        return self.x