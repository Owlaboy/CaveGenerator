import pygame


def drawTriangles(triangleList, points=[], sizeX=1200, sizeY=700):
    pygame.init()

    screen = pygame.display.set_mode([sizeX, sizeY])

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((50, 50, 50))

        for triangle in triangleList:
            pygame.draw.line(screen, (255, 0, 0),
                             triangle.pointA, triangle.pointB)
            pygame.draw.line(screen, (255, 0, 0),
                             triangle.pointB, triangle.pointC)
            pygame.draw.line(screen, (255, 0, 0),
                             triangle.pointA, triangle.pointC)
            pygame.draw.circle(screen, (0, 0, 255),
                               triangle.circleCenter, triangle.radius, 1)

            pygame.draw.circle(screen, (255, 255, 255), triangle.pointA, 2)
            pygame.draw.circle(screen, (255, 255, 255), triangle.pointB, 2)
            pygame.draw.circle(screen, (255, 255, 255), triangle.pointC, 2)

        for point in points:
            pygame.draw.circle(screen, (0, 255, 255), point, 2)

        pygame.display.flip()

    pygame.quit()


def drawEdges(edgeList, points=[], sizeX=1200, sizeY=700):
    pygame.init()

    screen = pygame.display.set_mode([sizeX, sizeY])

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((50, 50, 50))

        for edge in edgeList:
            pygame.draw.line(screen, (255, 0, 0), edge.point1, edge.point2)

        for point in points:
            pygame.draw.circle(screen, (200, 255, 255), point, 2)

        pygame.display.flip()

    pygame.quit()


def drawPoints(pointList, sizeX=1200, sizeY=700):
    pygame.init()

    screen = pygame.display.set_mode([sizeX, sizeY])

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((50, 50, 50))

        for point in pointList:
            pygame.draw.circle(screen, (255, 255, 255), point, 2)

        pygame.display.flip()

    pygame.quit()
