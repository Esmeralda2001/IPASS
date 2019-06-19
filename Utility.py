#swap function
#swaps two cities with eachother
def swap(r, i, j):
    temp = r[i]
    r[i] = r[j]
    r[j] = temp


def calculateCoordinates(x, y):
    x = (x * 25) + 250
    y = (y * 25) + 20

    return x, y