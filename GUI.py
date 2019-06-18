from tkinter import *
from Utility import *

def makeCircle(canvas, x, y):
    r = 10 #standard circle radius

    x0 = x-r
    x1 = x+r

    y0 = y-r
    y1 = y+r

    return canvas.create_oval(x0, y0, x1, y1)



def drawRoute(route):
    root = Tk()
    myMap = Canvas(root)
    myMap.pack()

    for i in range(len(route)-1):
        city = route[i]
        neighbor = route[i+1]
        x1, y1 = calculateCoordinates(city.x, city.y)
        x2, y2 = calculateCoordinates(neighbor.x, neighbor.y)
        makeCircle(myMap, x1, y1)
        Label(text=city.name).place(x=x1 + 5, y=y1 - 5)
        myMap.create_line(x1, y1, x2, y2)

    lastCity = route[-1]
    x, y = calculateCoordinates(lastCity.x, lastCity.y)
    Label(text=lastCity.name).place(x=x + 5, y=y - 5)
    makeCircle(myMap, x, y)


    root.mainloop()