import triangulator
import pygame
from classes.triangle import Triangle

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)


def draw_triangles(screen, triangle_list, circles=False, triangle_color=GREEN, circle_color=BLUE):
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
    superTriangle = Triangle((0, 0), (size_x*2, 0), (0, size_y*2))

    triangulation = [superTriangle]

    for point in point_list:
        pygame.draw.circle(screen, (255,255,255), point, 2)

    pygame.display.flip()
    pygame.time.wait(1000)

    for point in point_list:
        # Draw all triangles and show the new added point.
        draw_triangles(screen, triangulation)
        pygame.draw.circle(screen, (255,255,255), point, 2)
        
        pygame.display.flip()
        pygame.time.wait(1000)

        # Draw all bad triangles.
        badTriangles = triangulator.badTrianglesList(triangulation, point)
        draw_triangles(screen, badTriangles)
        pygame.draw.circle(screen, (255,255,255), point, 2)

        pygame.display.flip()
        pygame.time.wait(1000)
        
        # Draw the polygon
        polygon = triangulator.polygonEdges(badTriangles)
        draw_edges(screen, polygon)
        pygame.draw.circle(screen, (255,255,255), point, 2)

        pygame.display.flip()
        screen.fill((50, 50, 50))
        pygame.time.wait(1000)

        triangulator.removeBadTriangles(badTriangles, triangulation)
        triangulator.addNewTriangles(polygon, point, triangulation)
