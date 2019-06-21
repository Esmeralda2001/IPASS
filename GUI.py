from tkinter import *
from SimulatedA import sA

class GUI:
    def __init__(self, title, geo, routes):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(geo)
        self.frames = {}
        self.routes = routes
#------------------------------------------------------------SHAPES--------------------------------------------------------------------
    def calculateCoordinates(self, x, y):
        x = (x * 25) + 250
        y = (y * 25) + 20

        return x, y

    def makeCircle(self, x, y):
        r = 10 #standard circle radius

        x0 = x-r
        x1 = x+r

        y0 = y-r
        y1 = y+r

        return self.root.create_oval(x0, y0, x1, y1)

    def drawConnections(self, city, neighbors, color):
        x1, y1 = calculateCoordinates(city.x, city.y)
        for i in range(len(neighbors)):
            x2, y2 = calculateCoordinates(neighbors[i].x, neighbors[i].y)
            self.root.create_line(x1, y1, x2, y2, fill=color)

#------------------------------------------------------------ROUTE----------------------------------------------------------------------
    def drawRoute(self, route):
        for i in range(len(route)-1):
            city = route[i]
            neighbor = route[i+1]
            x1, y1 = calculateCoordinates(city.x, city.y)
            x2, y2 = calculateCoordinates(neighbor.x, neighbor.y)
            makeCircle(x1, y1)
            Label(text=city.name).place(x=x1 + 5, y=y1 - 5)
            self.root.create_line(x1, y1, x2, y2)

        lastCity = route[-1]
        x, y = calculateCoordinates(lastCity.x, lastCity.y)
        Label(text=lastCity.name).place(x=x + 5, y=y - 5)
        makeCircle(x, y)



#------------------------------------------------------------FRAMES--------------------------------------------------------------------
    def home(self):
        homeFrame = Frame(master=self.root)
        homeFrame.pack(fill="both", expand=True)
        self.addButtons(homeFrame, self.mapFrame, 4)
        if "home" not in self.frames:
            self.frames["home"] = homeFrame


    def mapFrame(self, route):
        self.frames["home"].pack_forget()
        newFrame = Frame(master=self.root)
        newFrame.pack(fill="both", expand=True)
        backButton = Button(master=newFrame, text="Return", command=self.home)
        newRoute = sA(route)

    def addButtons(self, frame, func, amt):
        for i in range(amt):
            button = Button(master=frame, text="5 points", command=lambda arg=self.routes[i]: func(arg))
            button.config(height=2, width=15)
            button.pack(pady=25)