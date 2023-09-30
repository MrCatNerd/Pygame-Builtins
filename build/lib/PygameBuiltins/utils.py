__author__ = "Alon B.R."

import pygame
import math

from os.path import join as join_path

pygame.init()


def get_directions_from_degree(degree: float | int) -> tuple[float, float]:

    x_move = math.sin(degree)
    y_move = math.cos(degree)

    return (x_move, y_move)


def load_image(
    *paths: str, size: tuple | list | None = None, convert_alpha: bool = False
) -> pygame.Surface:

    srf: pygame.Surface = pygame.image.load(join_path(*paths))

    if size is not None:
        srf = pygame.transform.scale(srf, size)

    if convert_alpha:
        srf = srf.convert_alpha()
    else:
        srf = srf.convert()

    return srf
