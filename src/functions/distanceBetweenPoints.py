from math import sqrt

def distanceBetweenPoints(point1: tuple, point2: tuple):
    return sqrt(((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2))