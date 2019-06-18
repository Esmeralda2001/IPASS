#swap function
#swaps two cities with eachother
def swap(r, i, j):
    temp = r[i]
    r[i] = r[j]
    r[j] = temp


def calculateCoordinates(x, y):
    x = (x * 10) + 50
    y = (y * 10) + 50

    return x, y