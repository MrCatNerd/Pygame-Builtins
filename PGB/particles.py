__author__ = "Alon B.R."

import pygame

from pygame import Vector2, Surface

pygame.init()


class _Particle2D:
    def __init__(
        self,
        x: int,
        y: int,
        vel_x: float | int,
        vel_y: float | int,
        accel_x: float | int,
        accel_y: float | int,
        time: float | int,
    ) -> None:

        self.pos: Vector2 = Vector2(x, y)
        self.vel: Vector2 = Vector2(vel_x, vel_y)
        self.accel: Vector2 = Vector2(accel_x, accel_y)

        self.time = time

    def update(
        self,
        deltaTime: float | int = 1,
        deltaTimeMultiply: float | int = 1,
    ) -> None:
        self.vel += self.accel
        self.vel.x *= deltaTime * deltaTimeMultiply
        self.vel.y *= deltaTime * deltaTimeMultiply

        self.pos.x += self.vel.x * deltaTime * deltaTimeMultiply
        self.pos.y += self.vel.y * deltaTime * deltaTimeMultiply

    def decay(
        self,
        decayAmount: float | int,
        deltaTime: float | int = 1,
        deltaTimeMultiply: float | int = 1,
    ) -> None:

        self.time -= decayAmount * deltaTime * deltaTimeMultiply

    @property
    def timeout(self) -> bool:
        return self.time <= 0


class ImageParticle2D(_Particle2D):
    def __init__(
        self,
        x: int,
        y: int,
        img: Surface,
        vel_x: float | int,
        vel_y: float | int,
        accel_x: float | int,
        accel_y: float | int,
        time: float | int,
    ) -> None:
        super().__init__(x, y, vel_x, vel_y, accel_x, accel_y, time)
        self.img: Surface = img

    def render(self, screen: Surface) -> None:
        screen.blit(self.img, self.pos)


class RectParticle2D(_Particle2D):
    def __init__(
        self,
        x: int,
        y: int,
        color: tuple,
        vel_x: float | int,
        vel_y: float | int,
        accel_x: float | int,
        accel_y: float | int,
        time: float | int,
    ) -> None:
        super().__init__(x, y, vel_x, vel_y, accel_x, accel_y, time)
        self.color: tuple = color

    def render(self, screen: pygame.Surface, width: int = 0) -> None:
        pygame.draw.rect(
            screen, self.color, (self.pos.x, self.pos.y, self.time, self.time), width
        )


class CircleParticle2D(_Particle2D):
    def __init__(
        self,
        x: int,
        y: int,
        color: tuple,
        vel_x: float | int,
        vel_y: float | int,
        accel_x: float | int,
        accel_y: float | int,
        time: float | int,
    ) -> None:
        super().__init__(x, y, vel_x, vel_y, accel_x, accel_y, time)
        self.color: tuple = color

    def render(self, screen: pygame.Surface, width: int = 0) -> None:
        pygame.draw.circle(
            screen, self.color, self.pos, self.time, width, draw_top_left=True
        )
