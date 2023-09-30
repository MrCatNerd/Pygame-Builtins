import pygame

pygame.init()


class _Slidebar2D:
    def __init__(
        self, minimum: float, maximum: float, length_px: int, value_px: int = 0
    ) -> None:
        self.length_px: int = length_px
        self.value_x: int = value_px

        self.minimum: float = minimum
        self.maximum: float = maximum

    @property
    def value(self) -> float:
        return
