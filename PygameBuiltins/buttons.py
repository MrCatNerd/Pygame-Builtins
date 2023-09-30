__author__ = "Alon B.R."

import pygame

pygame.init()


class _Button2D:
    def __init__(self, rect: pygame.FRect, state: bool | None = None) -> None:
        if state is None:
            state = False
        else:
            state = state

        self.rect: pygame.FRect = rect
        self.state: bool = state
        self._clicked = False

    def update(
        self, mouseX: float | int, mouseY: float | int, mouse_pressed: bool
    ) -> None:
        if (
            self.rect.collidepoint(mouseX, mouseY)
            and mouse_pressed
            and not self._clicked
        ):
            self.state = True
            self._clicked = True
        elif self._clicked and not mouse_pressed:
            self._clicked = False
        elif self.state and self._clicked == False:
            self.state = False


class Button2D(_Button2D):# TODO: make multiple types of img shapes etc
    def __init__(self, rect: pygame.FRect, state: bool | None = None) -> None:
        super().__init__(rect, state)


class _Switch2D:
    def __init__(self, rect: pygame.FRect, state: bool | None = None) -> None:
        if state is None:
            state = False
        else:
            state = state

        self.rect: pygame.FRect = rect
        self.state: bool = state
        self._clicked = False

    def update(
        self, mouseX: float | int, mouseY: float | int, mouse_pressed: bool
    ) -> None:
        if (
            self.rect.collidepoint(mouseX, mouseY)
            and mouse_pressed
            and not self._clicked
        ):
            self.state = not self.state
            self._clicked = True
        elif self._clicked and not mouse_pressed:
            self._clicked = False

class Switch2D(_Switch2D): # TODO: make multiple types of img shapes etc
    def __init__(self, rect: pygame.FRect, state: bool | None = None) -> None:
        super().__init__(rect, state)

