import numpy as np


def inv_distance(x, y):
    n1 = len(x)
    n2 = len(y)
    dist = np.empty((n1, n2))
    for i in range(n1):
        for j in range(n2):
            dist[i, j] = 1.0 / np.sqrt((x[i] - y[j]) ** 2)
    return dist


def inv_distance_vect(x, y):
    n1 = len(x)
    n2 = len(y)
    return 1.0 / np.sqrt((x.reshape((n1, 1)) - y.reshape((1, n2))) ** 2)
