__author__ = "Alon B.R."

import pygame

pygame.init()


# basic particle with pygame rendering and stuff
class _Particle2D:
    def __init__(self, position: pygame.FRect, velocity: tuple, acceleration: tuple) -> None:
        self.position: pygame.FRect = position
        self.velocity: tuple = velocity
        self.acceleration: tuple = acceleration

    def update(self, deltaTime: float = None, m=None) -> None:
        if deltaTime is None:
            deltaTime = 1

        # multiplier for lazy people like me
        if m is None:
            m = 1

        self.velocity[0] += self.acceleration[0] * deltaTime * m
        self.velocity[1] += self.acceleration[1] * deltaTime * m

        self.position[0] += self.velocity[0] * deltaTime * m
        self.position[1] += self.velocity[1] * deltaTime * m


class ImageParticle2D(_Particle2D):
    # Rect is still usefull for basic collisions
    def __init__(self, img: pygame.Surface, position: pygame.FRect, velocity: tuple, acceleration: tuple) -> None:
        self.img: pygame.Surface = img

        super().__init__(position, velocity, acceleration)

    def render(self, screen: pygame.Surface) -> None:
        screen.blit(self.img, self.position)


class RectParticle2D(_Particle2D):
    # Rect is still usefull for basic collisions
    def __init__(self, color: tuple, position: pygame.FRect, velocity: tuple, acceleration: tuple) -> None:
        self.color: tuple = color

        super().__init__(position, velocity, acceleration)

    def render(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, self.color, self.position)


class CircleParticle2D(_Particle2D):
    # Rect is still usefull for basic collisions
    def __init__(self, radius: float, color: tuple, position: pygame.FRect, velocity: tuple, acceleration: tuple) -> None:
        self.color: tuple = color
        self.radius: float = radius

        super().__init__(position, velocity, acceleration)

    def render(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, self.color,
                           (self.position.x, self.position), self.radius)
