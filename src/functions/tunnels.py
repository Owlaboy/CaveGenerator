import pygame

RED = (255, 0, 0)

def draw_tunnels(screen, edge_list):
    for edge in edge_list:
        pygame.draw.line(screen, RED, edge.point1, (edge.point1[0],edge.point2[1]), 5)
        pygame.draw.line(screen, RED, (edge.point1[0],edge.point2[1]), edge.point2, 5)
        