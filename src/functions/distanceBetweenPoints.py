from math import sqrt

def distanceBetweenPoints(point1: tuple, point2: tuple):
    """This function calulates the distance between two points.

    Args:
        point1 (tuple): (x,y) coordinates of the first point
        point2 (tuple): (x,y) coordinates of the second point

    Returns:
        float: float value of the distance between the two points
    """
    return sqrt(((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2))
