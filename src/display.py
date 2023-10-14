import pygame
from functions.roomGenerator import roomRectGenerator, roomPoints
from triangulator import BowyerWatson
from minimalTreeGenerator import prim
from functions.tunnels import draw_tunnels
from functions.triangulation_animator import triangulation_animation


def display(sizeX, sizeY, roomCount, showAnimation):
    """The main logic of the program. This function calls the needed functions to generate the rooms of the cave, 
    generate the triangulation and the minimum spanning tree of the triangulation. It also works as the main renderer
    of the pygame loop.

    Args:
        sizeX (int): wanted x size of the screen
        sizeY (int): wanted y size of the screen
        roomCount (int): the number of wanted rooms
        showAnimation (bool): This parameter defines if the animation is show to the user.
    """    
    pygame.init()

    screen = pygame.display.set_mode([sizeX, sizeY])

    rooms = roomRectGenerator(sizeX, sizeY, roomCount)
    room_centers = roomPoints(rooms)

    triangulation = BowyerWatson(room_centers, sizeX, sizeY)
    minimumSpanningTree = prim(triangulation)
    first_loop = True

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((50, 50, 50))

        draw_tunnels(screen, minimumSpanningTree)

        for room in rooms:
            pygame.draw.rect(screen, (255, 255, 255), room)

        if showAnimation:
            pygame.display.flip()
            screen.fill((50, 50, 50))
            triangulation_animation(screen, sizeX, sizeY, room_centers)
        showAnimation = False

        """
        for triangle in triangulation:
            pygame.draw.line(screen, (0, 255, 0),
                             triangle.pointA, triangle.pointB)
            pygame.draw.line(screen, (0, 255, 0),
                             triangle.pointB, triangle.pointC)
            pygame.draw.line(screen, (0, 255, 0),
                             triangle.pointA, triangle.pointC)

            pygame.draw.circle(screen, (255, 255, 255), triangle.pointA, 2)
            pygame.draw.circle(screen, (255, 255, 255), triangle.pointB, 2)
            pygame.draw.circle(screen, (255, 255, 255), triangle.pointC, 2)

        for edge in minimumSpanningTree:
            pygame.draw.line(screen, (255, 0, 0), edge.point1, edge.point2)
        """

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    display(1000, 500, 10)