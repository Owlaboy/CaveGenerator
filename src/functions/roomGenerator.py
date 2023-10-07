from random import randint
from pygame import Rect


def roomRectGenerator(sizeX, sizeY, RoomCount):
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
    centerPointList = []

    for room in generatedRooms:
        centerPointList.append(room.center)

    return centerPointList
