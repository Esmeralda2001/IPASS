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
        y = (y * 20) + 10

        return x, y

    def makeCircle(self, canvas, x, y):
        r = 10 #standard circle radius

        x0 = x-r
        x1 = x+r

        y0 = y-r
        y1 = y+r

        return canvas.create_oval(x0, y0, x1, y1)

    def connections(self, canvas, route):
        for i in range(len(route.route)):
            self.drawConnections(canvas, route.route[i], route.route[i].neighbors, "green")

    def drawConnections(self, canvas, city, neighbors, color):
        x1, y1 = self.calculateCoordinates(city.x, city.y)
        for i in range(len(neighbors)):
            x2, y2 = self.calculateCoordinates(neighbors[i].x, neighbors[i].y)
            canvas.create_line(x1, y1, x2, y2, fill=color)

#------------------------------------------------------------ROUTE----------------------------------------------------------------------
    def drawRoute(self, canvas, route):
        for i in range(len(route)-1):
            city = route[i]
            neighbor = route[i+1]
            x1, y1 = self.calculateCoordinates(city.x, city.y)
            x2, y2 = self.calculateCoordinates(neighbor.x, neighbor.y)
            self.makeCircle(canvas, x1, y1)
            Label(master=canvas, text=city.name).place(x=x1 + 5, y=y1 - 5)
            canvas.create_line(x1, y1, x2, y2)

        lastCity = route[-1]
        x, y = self.calculateCoordinates(lastCity.x, lastCity.y)
        Label(master=canvas, text=lastCity.name).place(x=x + 5, y=y - 5)
        self.makeCircle(canvas, x, y)



#------------------------------------------------------------FRAMES--------------------------------------------------------------------
    def home(self):
        homeFrame = Frame(master=self.root)
        homeFrame.pack(fill="both", expand=True)
        self.addButtons(homeFrame, self.mapFrame, 4)
        self.frames["home"] = homeFrame

    def moveBack(self, currFrame):
        self.frames["home"].pack()
        currFrame.pack_forget()

    def mapFrame(self, route, frame=None, result=False):
        newFrame = Frame(master=self.root)
        if result:
            frame.pack_forget()
            oldLength = route.distance
            route, elapsedTime = sA(route)
            infoFrame = Frame(master=newFrame)
            infoFrame.pack(side=TOP)
            time = Label(master=infoFrame, text="Time taken to calculate: "+str(elapsedTime))
            length = Label(master=infoFrame, text="Route length: "+str(route.distance))
            oldL = Label(master=infoFrame, text="Old route length: "+str(oldLength))
            time.pack(expand=True, fill=BOTH)
            length.pack(expand=True, fill=BOTH)
            oldL.pack(expand=True, fill=BOTH)
        else:
            resultButton = Button(master=newFrame, text="Calculate Result",
            command=lambda arg1=route, arg2=newFrame, arg3=True: self.mapFrame(arg1, arg2, arg3))
            resultButton.config(height=2, width=15)
            resultButton.pack(padx=10, pady=10)

        self.frames["home"].pack_forget()
        newFrame.pack(fill="both", expand=True)
        backButton = Button(master=newFrame, text="Return", command=lambda arg=newFrame: self.moveBack(arg))
        backButton.config(height=2, width=15)
        backButton.pack(padx=10, pady=10)

        canvas = Canvas(master=newFrame)
        self.connections(canvas, route)
        self.drawRoute(canvas, route.route)
        canvas.pack(fill=BOTH, expand=True)


    def addButtons(self, frame, func, amt):
        for i in range(amt):
            button = Button(master=frame, text="5 points", command=lambda arg=self.routes[i]: func(arg))
            button.config(height=2, width=15)
            button.pack(pady=25)