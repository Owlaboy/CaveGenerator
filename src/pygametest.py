# Simple pygame program

# Import and initialize the pygame library
import pygame
from pygame import Rect
from random import randint
from triangulator import Triangle, BowyerWatson
from display import RoomPoints, RoomRectGenerator
from minimalTreeGenerator import prim
from pygameTestRenderer import drawEdges


rooms = RoomRectGenerator(1000, 500, 10)

testingArray = [(812, 422), (686, 311), (782, 512), (288, 67), (793, 234), (756, 354), (65, 406), (853, 493), (395, 442), (630, 478)]
a = BowyerWatson(testingArray[:], 1000, 500 )
# for triangle in a:
#     print(str(triangle))
edges = prim(a)
drawEdges(edges)
# Run until the user asks to quit
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([1000, 500])
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


    # for room in rooms:
    #     pygame.draw.rect(screen, (255,255,255), room)


    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()