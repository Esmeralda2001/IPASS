from tkinter import *
from SimulatedA import sA

'''
Module for a GUI that displays the calculated routes for several test-cases 
'''


class GUI:
    def __init__(self, title, geo, routes):
        """
        :param title: title for the GUI
        :param geo: size of the GUI
        :param routes: all the routes that will be displayed
        :type title: basestring
        :type geo: basestring
        :type routes: dict containing instances of Route
        """
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(geo)
        self.frames = {}
        self.routes = routes
#------------------------------------------------------------SHAPES--------------------------------------------------------------------
    def calculateCoordinates(self, x, y):
        """
        :param x: x-coordinate
        :param y: y-coordinate
        :type x: float/integer
        :type y: float/integer
        :return: newly calculated x and y coordinates
        :rtype: float/integer
        """
        x = (x * 25) + 250
        y = (y * 20) + 10

        return x, y

    def makeCircle(self, canvas, x, y):
        """
        :param canvas: canvas that's being drawn on
        :param x: x-coordinate for the circle
        :param y: y-coordinate for the circle
        :type x: integer/float
        :type y: integer/float
        :type canvas: tkinter.Canvas
        :return: circle
        :rtype: canvas.create_oval
        """
        r = 10 #standard circle radius

        x0 = x-r
        x1 = x+r

        y0 = y-r
        y1 = y+r

        return canvas.create_oval(x0, y0, x1, y1)

    def connections(self, canvas, route):
        """
        :param canvas: canvas that's being drawn on
        :param route: Route that contains all the Cities and therefore also contains the connections
        :type canvas: tkinter.Canvas
        :type route: Route
        :return: void. Function will call 'drawConnections' to actually draw the connections
        """
        for i in range(len(route.route)):
            self.drawConnections(canvas, route.route[i], route.route[i].neighbors, "green")

    def drawConnections(self, canvas, city, neighbors, color):
        """
        :param canvas: canvas that's being drawn on
        :param city: current city for which the connections are being drawn for
        :param neighbors: the neighbors of the current city
        :param color: color of the lines
        :type canvas: tkinter.Canvas
        :type city: City
        :type neighbors: list containing instances of City
        :type color: basestring
        :return: void. Function will draw lines on the canvas that represent the connections between each city and it's neighbors
        """
        x1, y1 = self.calculateCoordinates(city.x, city.y)
        for i in range(len(neighbors)):
            x2, y2 = self.calculateCoordinates(neighbors[i].x, neighbors[i].y)
            canvas.create_line(x1, y1, x2, y2, fill=color)

#------------------------------------------------------------ROUTE----------------------------------------------------------------------
    def drawRoute(self, canvas, route):
        """
        :param canvas: canvas that will be drawn on
        :param route: Route that will be drawn onto the canvas
        :type canvas: tkinter.Canvas
        :type route: Route
        :return: void. Functio draws the Route onto the canvas
        """
        for i in range(len(route)-1):
            city = route[i]
            neighbor = route[i+1]
            x1, y1 = self.calculateCoordinates(city.x, city.y)
            x2, y2 = self.calculateCoordinates(neighbor.x, neighbor.y)
            self.makeCircle(canvas, x1, y1)
            Label(master=canvas, text=city.name).place(x=x1 + 5, y=y1 - 5)
            canvas.create_line(x1, y1, x2, y2, width=5)

        lastCity = route[-1]
        x, y = self.calculateCoordinates(lastCity.x, lastCity.y)
        Label(master=canvas, text=lastCity.name).place(x=x + 5, y=y - 5)
        self.makeCircle(canvas, x, y)



#------------------------------------------------------------FRAMES--------------------------------------------------------------------
    def home(self):
        """
        This function draws the home-screen on the GUI
        :return: void
        """
        homeFrame = Frame(master=self.root)
        homeFrame.pack(fill="both", expand=True)
        self.addButtons(homeFrame, self.mapFrame)
        self.frames["home"] = homeFrame

    def moveBack(self, currFrame):
        """
        :param currFrame: current Frame from which is beig moved back from
        :type currFrame: tkinter.Frame
        :return: void. Function makes the currFrame dissappear and lets the homeFrame appear
        """
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
            if oldLength == route.distance:
                length = Label(master=infoFrame, text="No improvements were found")
            else:
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


    def addButtons(self, frame, func):
        """
        :param frame: frame for which the buttons are being added
        :param func: function that will be assigned to the buttons
        :type frame: tkinter.Frame
        :type func: function
        :return: void. Function simply adds buttons to the Frame
        """
        for key in self.routes:
            button = Button(master=frame, text=key+" points", command=lambda arg=self.routes[key]: func(arg))
            button.config(height=2, width=15)
            button.pack(pady=20)