import pygame
import math

def draw_tunnels(screen, edge_list):
    for edge in edge_list:
        top_left = (min((edge.point1[0], edge.point2[0])), min((edge.point1[1], edge.point2[1])))
        bottom_right = (max((edge.point1[0], edge.point2[0])), max((edge.point1[1], edge.point2[1])))
        edge_rectangle = pygame.Rect(top_left, bottom_right)

        pygame.draw.arc(screen, (255,255,255), edge_rectangle, 0, math.pi)