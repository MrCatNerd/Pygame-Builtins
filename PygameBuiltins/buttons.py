__author__ = "Alon B.R."

import pygame

pygame.init()


class _Button2D:
    def __init__(self, position: pygame.FRect) -> None:
        self.position: pygame.FRect = position

    def update(self, mx: float | int, my: float | int) -> None:
        pass  # TODO collosion stuff and boilerplate
