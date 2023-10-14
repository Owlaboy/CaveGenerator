from random import randint
from pygame import Rect


def roomRectGenerator(sizeX, sizeY, RoomCount):
    """This function generates the wanted number of rooms onto the map. The rooms are pygame's Rect objects.
    The objects are randomly generated such that the result is always different. The function generates the
    position of each room randomly and uses Rect object's methods to make sure the rooms do not overlap.

    Args:
        sizeX (int): maximum x direction of the map
        sizeY (int): maximum y direction of the map
        RoomCount (int): the wanted number of rooms

    Returns:
        list: list of Rect objects that are not overlapping.
    """
    generatedRooms = []
    collidingRooms = []

    i = 0
    while i < RoomCount:
        width = randint(20, 80)
        height = randint(20, 80)
        new = Rect(((randint(10, sizeX-(10 + width)),
                   randint(10, sizeY-(10 + height))), (width, height)))
        if new.collidelistall(generatedRooms) == []:
            generatedRooms.append(new)
            i += 1
        else:
            collidingRooms.append(new)
    return generatedRooms


def roomPoints(generatedRooms: list):
    """This function converts a list of Rect objects into a list of their coordinates

    Args:
        generatedRooms (list): list of Rect objects

    Returns:
        list: list of (x,y) tuples.
    """
    centerPointList = []

    for room in generatedRooms:
        centerPointList.append(room.center)

    return centerPointList
