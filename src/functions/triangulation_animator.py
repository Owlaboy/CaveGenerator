import triangulator
import pygame
from classes.triangle import Triangle

DELAY = 1000

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)


def draw_triangles(screen, triangle_list, circles=False, triangle_color=GREEN, circle_color=BLUE):
    """This function renders a list of given triangles

    Args:
        screen (pygame obj): what screen to render to
        triangle_list (list): list of the triangles to be drawn
        circles (bool, optional): Whether to draw the circumcirlces of the triangles. Defaults to False.
        triangle_color (tuple, optional): what color to give the triangles. Defaults to GREEN.
        circle_color (tuple, optional): what color to give the circles. Defaults to BLUE.
    """
    for triangle in triangle_list:
            pygame.draw.line(screen, triangle_color,
                             triangle.pointA, triangle.pointB)
            pygame.draw.line(screen, triangle_color,
                             triangle.pointB, triangle.pointC)
            pygame.draw.line(screen, triangle_color,
                             triangle.pointA, triangle.pointC)
            if circles:
                pygame.draw.circle(screen, circle_color,
                                triangle.circleCenter, triangle.radius, 1)

            pygame.draw.circle(screen, WHITE, triangle.pointA, 2)
            pygame.draw.circle(screen, WHITE, triangle.pointB, 2)
            pygame.draw.circle(screen, WHITE, triangle.pointC, 2)

def draw_edges(screen, edge_list, edge_color=RED):
     for edge in edge_list:
            pygame.draw.line(screen, edge_color, edge.point1, edge.point2)

def triangulation_animation(screen, size_x, size_y, point_list):
    """This function renders the whole triangulation step by step. It uses the functions defined in the triangulator.py file

    Args:
        screen (pygame screen): the screen where to render the animation
        size_x (int): maximum value of x 
        size_y (int): maximum value of y
        point_list (list): list of points that are to be triangulated
    """
    superTriangle = Triangle((0, 0), (size_x*2, 0), (0, size_y*2))

    triangulation = [superTriangle]

    for point in point_list:
        pygame.draw.circle(screen, (255,255,255), point, 2)

    pygame.display.flip()
    pygame.time.wait(DELAY)
    screen.fill((50, 50, 50))


    for point in point_list:
        pygame.display.flip()

        # Draw all triangles and show the new added point.
        draw_triangles(screen, triangulation)
        pygame.draw.circle(screen, (255,255,255), point, 2)
        
        pygame.display.flip()
        pygame.time.wait(DELAY)

        # Draw all bad triangles.
        badTriangles = triangulator.badTrianglesList(triangulation, point)
        draw_triangles(screen, badTriangles, True, RED)
        pygame.draw.circle(screen, (255,255,255), point, 2)

        pygame.display.flip()
        pygame.time.wait(DELAY)
        
        # Draw the polygon
        polygon = triangulator.polygonEdges(badTriangles)
        draw_edges(screen, polygon, BLUE)
        pygame.draw.circle(screen, (255,255,255), point, 2)

        pygame.display.flip()
        screen.fill((50, 50, 50))
        pygame.time.wait(DELAY)

        triangulator.removeBadTriangles(badTriangles, triangulation)
        triangulator.addNewTriangles(polygon, point, triangulation)

    draw_triangles(screen, triangulation)

    pygame.display.flip()
    pygame.time.wait(DELAY*2)
