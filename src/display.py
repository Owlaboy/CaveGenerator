# Simple pygame program

# Import and initialize the pygame library
import pygame
from pygame import Rect
from random import randint
from triangulator import Triangle, BowyerWatson


def RoomRectGenerator(sizeX, sizeY, RoomCount):
    generatedRooms = []
    collidingRooms = []

    i = 0
    while i < RoomCount:
        width = randint(20,80)
        height = randint(20,80)
        new = Rect(((randint(10,sizeX-(10 + width)),randint(10,sizeY-(10 + height))), (width, height)))
        if new.collidelistall(generatedRooms) == []:
            generatedRooms.append(new)
            i += 1
        else:
            collidingRooms.append(new)
    return generatedRooms

def RoomPoints(generatedRooms: list):
    centerPointList = []

    for room in generatedRooms:
        centerPointList.append(room.center)

    return centerPointList

    
def display(sizeX, sizeY, roomCount):
    pygame.init()

    screen = pygame.display.set_mode([sizeX, sizeY])
    
    rooms = RoomRectGenerator(sizeX, sizeY, roomCount)
    roomPoints = RoomPoints(rooms)

    triangulation = BowyerWatson(roomPoints, sizeX, sizeY)

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((50, 50, 50))

        for room in rooms:
            pygame.draw.rect(screen, (255,255,255), room)

        for triangle in triangulation:
            pygame.draw.line(screen,(255, 0, 0), triangle.pointA, triangle.pointB)
            pygame.draw.line(screen,(255, 0, 0), triangle.pointB, triangle.pointC)
            pygame.draw.line(screen,(255, 0, 0), triangle.pointA, triangle.pointC)
            
            pygame.draw.circle(screen, (255,255,255), triangle.pointA, 2)
            pygame.draw.circle(screen, (255,255,255), triangle.pointB, 2)
            pygame.draw.circle(screen, (255,255,255), triangle.pointC, 2)

        


        pygame.display.flip()

    pygame.quit()