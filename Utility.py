#swap function
#swaps two cities with eachother
def swap(r, i, j):
    temp = r[i]
    r[i] = r[j]
    r[j] = temp