import pygame

RED = (255, 0, 0)

def draw_tunnels(screen, edge_list):
    """This function converts diagonal lines into its horizontal and vertical compnents and renders those components

    Args:
        screen (pygame obj): The screen to which to render to
        edge_list (list): list of edges to be rendered
    """
    for edge in edge_list:
        pygame.draw.line(screen, RED, edge.point1, (edge.point1[0],edge.point2[1]), 5)
        pygame.draw.line(screen, RED, (edge.point1[0],edge.point2[1]), edge.point2, 5)
        