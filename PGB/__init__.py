__author__ = "Alon B.R."
import pygame
from pygame import Rect

pygame.init()

# from PGB import buttons, hitboxes, particles, tilebased, utils


class HitBox2D:
    """
    Better than pygame.Rect because of floating point accuracy
    and this class has more functions and everybody knows that more functions > less functions.
    """

    def __init__(
        self, x: float | int, y: float | int, width: float | int, height: float | int
    ) -> None:
        self.x: float | int = x
        self.y: float | int = y
        self.width: float | int = width
        self.height: float | int = height

    def collideHitBox(self, other) -> bool:
        return (
            (self.left >= other.left and self.left <= other.right)
            or (self.right >= other.left and self.right <= other.right)
        ) and (
            (self.top >= other.top and self.top <= other.bottom)
            or (self.bottom >= other.top or self.bottom <= other.bottom)
        )

    def collideLikeHitBox(
        self,
        likeOther: tuple[float | int, float | int, float | int, float | int]
        | list[float | int, float | int, float | int, float | int],
    ) -> bool:

        oleft = likeOther[0]
        oright = likeOther[1]
        otop = likeOther[2]
        obottom = likeOther[3]

        return (
            (self.left >= oleft and self.left <= oright)
            or (self.right >= oleft and self.right <= oright)
        ) and (
            (self.top >= otop and self.top <= obottom)
            or (self.bottom >= otop or self.bottom <= obottom)
        )

    def collidePoint(self, point: tuple[float | int, float | int]) -> bool:
        return (point[0] > self.x and point[0] < (self.x + self.width)) and (
            point[1] > self.y and point[1] < (self.y + self.height)
        )

    def render(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(
            screen, (255, 0, 0), self.get_like_rect, 3
        )  # TODO add more options

    def addHitBox(self, other) -> None:
        self.x += other.x
        self.y += other.y

    def subHitBox(self, other) -> None:
        self.x -= other.x
        self.y -= other.y

    def mulHitBox(self, other) -> None:
        self.x *= other.x
        self.y *= other.y

    def divHitBox(self, other) -> None:
        self.x /= other.x
        self.y /= other.y

    def modHitBox(self, other) -> None:
        self.x %= other.x
        self.y %= other.y

    @property
    def get_rect(self) -> Rect:
        return Rect(self.x, self.y, self.width, self.height)

    @property
    def get_like_rect(
        self,
    ) -> tuple[float | int, float | int, float | int, float | int]:
        return (self.x, self.y, self.width, self.height)

    @property
    def get_pos(self) -> tuple[float | int, float | int]:
        return (self.x, self.y)

    @property
    def bottom(self) -> float | int:
        return self.y + self.height

    @property
    def top(self) -> float | int:  # idk why
        return self.y

    @property
    def right(self) -> float | int:
        return self.x + self.width

    @property
    def left(self) -> float | int:  # idk why
        return self.x


print("Welcome to the Pygame Builtins libarary")
