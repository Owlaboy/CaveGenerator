# Simple pygame program

# Import and initialize the pygame library
import pygame
from pygame import Rect
from random import randint
from triangulator import Triangle, BowyerWatson, badTriangles
from display import RoomPoints, RoomRectGenerator
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([1000, 500])

rooms = RoomRectGenerator(10)

testingArray = [(812, 422), (686, 311), (782, 512), (288, 67), (793, 234), (756, 354), (65, 406), (853, 493), (395, 442), (630, 478)]
a = BowyerWatson(testingArray[:3], 1000, 500)
b = badTriangles(a, testingArray[4])
print(b)
# for triangle in a:
#     print(str(triangle))

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

    for triangle in b:
        pygame.draw.circle(screen, (0,0,255), triangle.circleCenter, triangle.radius)

        pygame.draw.circle(screen, (255,255,255), triangle.pointA, 2)
        pygame.draw.circle(screen, (255,255,255), triangle.pointB, 2)
        pygame.draw.circle(screen, (255,255,255), triangle.pointC, 2)
        
        pygame.draw.circle(screen, (255,255,255), testingArray[4], 3)
        
    for triangle in b:
        
        pygame.draw.line(screen,(255,0,0), triangle.pointA, triangle.pointB)
        pygame.draw.line(screen,(255,0,0), triangle.pointB, triangle.pointC)
        pygame.draw.line(screen,(255,0,0), triangle.pointA, triangle.pointC)

    # for room in rooms:
    #     pygame.draw.rect(screen, (255,255,255), room)


    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()