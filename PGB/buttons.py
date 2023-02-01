__author__ = "Alon B.R."

import pygame

from pygame import Surface

from PGB import HitBox2D

pygame.init()


class ImageButton2D:
    def __init__(
        self,
        x: float | int,
        y: float | int,
        img: Surface,
        working: bool = True,
    ) -> None:
        self.img: Surface = img
        self.hitbox: HitBox2D = HitBox2D(
            x, y, self.img.get_width(), self.img.get_height()
        )

        self.state: bool = False
        self.working: bool = working

    def update(self, mouseX: float | int, mouseY: float | int, click: bool) -> None:
        if self.hitbox.collidePoint((mouseX, mouseY)) and click and self.working:
            self.activate()
        elif self.state:
            self.reset()

    def reset(self) -> None:
        if not self.working:
            return
        self.state = False

    def activate(self) -> None:
        if not self.working:
            return
        self.state = True

    def switch(self) -> None:
        if not self.working:
            return
        self.state = not self.state

    def disable_button(self) -> None:
        self.working = False

    def enable_button(self) -> None:
        self.working = True

    def render(self, screen: Surface) -> None:
        screen.blit(self.img, self.hitbox.get_pos)


class ImageSwitch2D(ImageButton2D):
    def __init__(
        self,
        x: float | int,
        y: float | int,
        imgOff: Surface,
        imgOn: Surface,
        state: bool = True,
        working: bool = True,
    ) -> None:
        self.imgOff: Surface = imgOff
        self.imgOn: Surface = imgOn
        self.hitbox: HitBox2D = HitBox2D(
            x, y, self.img.get_width(), self.img.get_height()
        )

        self.state: bool = False
        self.working: bool = working

        self.state = state

    def update(self, mouseX: float | int, mouseY: float | int, click: bool) -> None:
        if self.hitbox.collidePoint((mouseX, mouseY)) and click and self.working:
            self.switch()

    def render(self, screen: Surface) -> None:
        screen.blit(
            {False: self.imgOff, True: self.imgOn}[self.state], self.hitbox.get_pos
        )
