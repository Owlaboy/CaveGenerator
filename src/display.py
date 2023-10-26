import pygame
from functions.roomGenerator import roomRectGenerator, roomPoints
from triangulator import BowyerWatson
from minimalTreeGenerator import prim
from functions.tunnels import draw_tunnels
from functions.triangulation_animator import triangulation_animation


def display(sizeX, sizeY, roomCount, showAnimation, speed):
    """The main logic of the program. This function calls the needed functions to generate the rooms of the cave, 
    generate the triangulation and the minimum spanning tree of the triangulation. It also works as the main renderer
    of the pygame loop.

    Args:
        sizeX (int): wanted x size of the screen
        sizeY (int): wanted y size of the screen
        roomCount (int): the number of wanted rooms
        showAnimation (bool): This parameter defines if the animation is show to the user.
        speed (int): the speed at which to display the animation steps
    
    Returns:
        returnable (tuple): This tuple contains two boolean values. The firs tboolean value tells the calling function if the user wants to keep running the program. 
        the second boolean value tells the program if it needs to ask the user for the inputs again or to run the program with the same inputs.
    """    


    pygame.init()

    screen = pygame.display.set_mode([sizeX, sizeY])

    rooms = roomRectGenerator(sizeX, sizeY, roomCount)
    room_centers = roomPoints(rooms)

    triangulation = BowyerWatson(room_centers, sizeX, sizeY)
    minimumSpanningTree = prim(triangulation)
    restart = None

    running = True
    setUp = True
    while running:
        pygame.display.set_caption("CaveGenerator map")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                restart = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    restart = False
                elif event.key == pygame.K_SPACE:
                    running = False
                    restart = True
                    setUp = False
                else:
                    running = False
                    restart = True
                    setUp = True

        screen.fill((50, 50, 50))

        draw_tunnels(screen, minimumSpanningTree)

        for room in rooms:
            pygame.draw.rect(screen, (255, 255, 255), room)

        if showAnimation:
            pygame.display.set_caption("Triangulator animation")

            pygame.display.flip()
            screen.fill((50, 50, 50))
            triangulation_animation(screen, sizeX, sizeY, room_centers, speed)
        pygame.display.set_caption("CaveGenerator map")
        showAnimation = False

        pygame.display.flip()

    pygame.quit()
    returnable = (restart, setUp)
    return returnable

if __name__ == "__main__":
    display(1000, 500, 10)