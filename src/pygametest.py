# Simple pygame program

# Import and initialize the pygame library
import pygame
from pygame import Rect
from random import randint
pygame.init()



# Set up the drawing window
screen = pygame.display.set_mode([1000, 500])

def RoomRectGenerator(RoomCount):
    generatedRooms = []
    collidingRooms = []

    i = 0
    while i < RoomCount:
        new = Rect(((randint(10,890),randint(10,490)), (randint(20,80),randint(20,80))))
        print(new.collidelistall(generatedRooms))
        if new.collidelistall(generatedRooms) == []:
            generatedRooms.append(new)
            i += 1
        else:
            collidingRooms.append(new)
    print(generatedRooms)
    return generatedRooms

def RoomPoints(generatedRooms: list):
    centerPointList = []

    for room in generatedRooms:
        centerPointList.append(room.center)

    return centerPointList

    

rooms = RoomRectGenerator(10)
print(RoomPoints(rooms))


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
    for room in rooms:
        pygame.draw.rect(screen, (255,255,255), room)


    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()