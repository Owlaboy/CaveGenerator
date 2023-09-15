# Simple pygame program

# Import and initialize the pygame library
import pygame
from pygame import Rect
from random import randint
from triangulator import Triangle, BowyerWatson
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([1000, 500])

def RoomRectGenerator(RoomCount):
    generatedRooms = []
    collidingRooms = []

    i = 0
    while i < RoomCount:
        new = Rect(((randint(10,890),randint(10,490)), (randint(20,80),randint(20,80))))
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

    

rooms = RoomRectGenerator(10)

testingArray = [(812, 422), (686, 311), (782, 512), (288, 67), (793, 234), (756, 354), (65, 406), (853, 493), (395, 442), (630, 478)]
a = BowyerWatson(testingArray[:4])
for triangle in a:
    print(str(triangle))

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((50, 50, 50))

    # Draw a solid blue circle in the center
    for triangle in a:
        pygame.draw.line(screen,(0,255,255), triangle.pointA, triangle.pointB)
        pygame.draw.line(screen,(0,255,255), triangle.pointB, triangle.pointC)
        pygame.draw.line(screen,(0,255,255), triangle.pointA, triangle.pointC)
        
        pygame.draw.circle(screen, (255,255,255), triangle.pointA, 2)
        pygame.draw.circle(screen, (255,255,255), triangle.pointB, 2)
        pygame.draw.circle(screen, (255,255,255), triangle.pointC, 2)

    for room in rooms:
        pygame.draw.rect(screen, (255,255,255), room)


    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()