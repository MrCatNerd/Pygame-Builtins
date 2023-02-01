__author__ = "Alon B.R."

import pygame

from pygame import Vector2, Surface

from PGB import HitBox2D

pygame.init()


class Tile:
    def __init__(
        self,
        x: int,
        y: int,
        img: Surface,
        tag: str = "tile",
        name: str = "Tile",
    ) -> None:
        self.img: Surface = img

        self.hitbox: HitBox2D = HitBox2D(
            x, y, self.img.get_width(), self.img.get_height()
        )

        self.tag: str = tag
        self.name: str = name

    def render(self, window: Surface) -> None:
        window.blit(self.img, self.hitbox.get_pos)


class Entity:
    def __init__(
        self,
        x: int,
        y: int,
        img,
        mass,
        GRAVITY,
        SCALE,
        tag: str = "entity",
        name: str = "Entity",
    ) -> None:
        self.img = img

        self.hitbox: HitBox2D = HitBox2D(
            x, y, self.img.get_width(), self.img.get_height()
        )

        self.tag: str = tag
        self.name: str = name

        # physics
        self.mass = mass
        self.velocity = Vector2(0, 0)
        self.direction_for_axis = Vector2(1, 1)
        self.acceleration = Vector2(
            (self.mass * GRAVITY) / SCALE, (self.mass * GRAVITY) / SCALE
        )

        # AI
        self.active_AI: bool = True

    def update(
        self,
        window,
        tile_list: list,
        deltaTime: float | int = 1,
        deltaTimeMultiply: float | int = 1,
    ) -> None:

        dx = 0
        dy = 0

        # gravity
        self.velocity.x += self.acceleration.x * deltaTime * deltaTimeMultiply
        self.velocity.y += self.acceleration.y * deltaTime * deltaTimeMultiply

        dx += self.velocity.x
        dy += self.veloicty.y

        # collision detection

        for tile in tile_list:

            if tile.hitbox.collideLikeHitBox(  # y collision detection
                (
                    self.hitbox.x + dy,
                    self.hitbox.y,
                    self.hitbox.width,
                    self.hitbox.height,
                )
            ):
                if dx > 0:
                    dx = (self.hitbox.x + self.hitbox.width) - tile.hitbox.x
                elif dx < 0:
                    dx = self.hitbox.x - (tile.hitbox.x + tile.hitbox.width)

                self.velocity.x = 0

            ##############################################################

            if tile.hitbox.collideLikeHitBox(  # y collision detection
                (
                    self.hitbox.x,
                    self.hitbox.y + dy,
                    self.hitbox.width,
                    self.hitbox.height,
                )
            ):
                if dy > 0:
                    dy = self.hitbox.bottom - tile.hitbox.top
                elif dy < 0:
                    dy = self.hitbox.top - tile.hitbox.bottom

                self.velocity.y = 0

        self.hitbox.x += dx
        self.hitbox.y += dy

        window.blit(self.img, (self.hitbox.x, self.rect.y))

    def init_AI(self):
        self.progress = 0

    def AI(
        self,
        walk_range: int | float,
        speed: int | float,
        deltaTime: float | int = 1,
        deltaTimeMultiply: float | int = 1,
        start_direction=None,
    ):
        if start_direction is None:
            start_direction = 1  # right

        direction = start_direction
        del start_direction

        if self.active_AI:
            self.hitbox.x += speed * direction * deltaTime * deltaTimeMultiply
            self.progress += speed * direction * deltaTime * deltaTimeMultiply
            if self.progress >= walk_range:
                self.progress *= -1
                direction *= -1


class ImagePhysicParticle2D:
    def __init__(
        self,
        x: int | float,
        y: int | float,
        img: Surface,
        timer: int | float,
        power: int | float,
        vel_x: int | float,
        vel_y: int | float,
        accel_x: int | float,
        accel_y: int | float,
        max_vel_x: int | float,
        max_vel_y: int | float,
        const_hitbox_size: bool = True,
    ) -> None:

        self.hitbox: HitBox2D = HitBox2D(x, y, img.get_width(), img.get_height())
        self.img: Surface = img
        self.velocity = Vector2(vel_x, vel_y)
        self.acceleration = Vector2(accel_x, accel_y)

        self.timer = timer
        self.power = power

        self.max_vel_x: int | float = max_vel_x
        self.max_vel_y: int | float = max_vel_y

        self.const_hitbox_size: bool = const_hitbox_size

    def update(
        self,
        tile_list: list[Tile],
        deltaTime: float | int = 1,
        deltaTimeMultiply: float | int = 1,
    ) -> None:
        self.timer -= self.power * deltaTime * deltaTimeMultiply

        dx = 0
        dy = 0

        self.velocity.x += self.acceleration.x * deltaTime * deltaTimeMultiply
        self.velocity.y += self.acceleration.y * deltaTime * deltaTimeMultiply

        self.velocity.y = min(self.velocity.y, self.max_vel_y)
        self.velocity.x = min(self.velocity.x, self.max_vel_x)
        self.velocity.y = max(self.velocity.y, -self.max_vel_y)
        self.velocity.x = max(self.velocity.x, -self.max_vel_x)

        dx += self.velocity.x
        dy += self.velocity.y

        # collision detection:

        # x collision detection
        for tile in tile_list:
            if tile.hitbox.collideLikeHitBox(
                (
                    self.hitbox.x + dx,
                    self.hitbox.y,
                    self.hitbox.right,
                    self.hitbox.height,
                )
            ):
                if dx > 0:
                    dx = (self.hitbox.right) - tile.hitbox.x
                elif dx < 0:
                    dx = self.hitbox.x - (tile.hitbox.x + tile.hitbox.width)

                self.velocity.x = 0

            # y collision detection
            if tile.hitbox.collideLikeHitBox(
                (
                    self.hitbox.x,
                    self.hitbox.y + dy,
                    self.hitbox.right,
                    self.hitbox.height,
                )
            ):
                print(tile)
                if dy >= 0:
                    dy = tile.hitbox.top - self.hitbox.bottom
                elif dy < 0:
                    dy = tile.hitbox.bottom - self.hitbox.top

                self.velocity.y = 0
        # adding values to position
        self.hitbox.x += dx
        self.hitbox.y += dy

        # updating hitbox size
        if not self.const_hitbox_size:
            self.hitbox.width = self.timer
            self.hitbox.height = self.timer

    @property
    def timeout(self) -> bool:
        return self.timer <= 0

    def render(self, screen: Surface) -> None:
        screen.blit(self.img, (self.hitbox.x, self.hitbox.y))


class _PhysicParticle2D:
    def __init__(
        self,
        x: float | int,
        y: float | int,
        color: tuple,
        timer: float | int,
        power: float | int,
        vel_x: float | int,
        vel_y: float | int,
        accel_x: float | int,
        accel_y: float | int,
    ) -> None:

        self.timer: float | int = timer
        self.power: float | int = power

        self.color: tuple = color

        self.hitbox = HitBox2D(x, y, self.timer, self.timer)
        self.velocity = Vector2(vel_x, vel_y)
        self.acceleration = Vector2(accel_x, accel_y)

    def update(
        self,
        tile_list: list[Tile],
        deltaTime: float | int = 1,
        deltaTimeMultiply: float | int = 1,
    ) -> None:

        self.timer -= self.power * deltaTime * deltaTimeMultiply

        dx = 0
        dy = 0

        self.velocity.x += self.acceleration.x * deltaTime * deltaTimeMultiply
        self.velocity.y += self.acceleration.y * deltaTime * deltaTimeMultiply

        dx += self.velocity.x
        dy += self.velocity.y
        # collision detection:

        # x collision detection
        for tile in tile_list:
            print(tile)
            if tile.hitbox.collideLikeHitBox(
                (
                    self.hitbox.x + dx,
                    self.hitbox.y,
                    self.hitbox.right,
                    self.hitbox.height,
                )
            ):
                if dx > 0:
                    dx = (self.hitbox.right) - tile.hitbox.x
                elif dx < 0:
                    dx = self.hitbox.x - (tile.hitbox.x + tile.hitbox.width)

                self.velocity.x = 0

            # y collision detection
            if tile.hitbox.collideLikeHitBox(
                (
                    self.hitbox.x,
                    self.hitbox.y + dy,
                    self.hitbox.right,
                    self.hitbox.height,
                )
            ):
                if dy >= 0:
                    dy = tile.hitbox.top - self.hitbox.bottom
                elif dy < 0:
                    dy = tile.hitbox.bottom - self.hitbox.top

                self.velocity.y = 0
        # adding values to position
        self.hitbox.x += dx
        self.hitbox.y += dy

        # updating hitbox size
        self.hitbox.width = self.timer
        self.hitbox.height = self.timer

    @property
    def timeout(self) -> bool:
        return self.timer <= 0


class RectPhisycParticle2D(_PhysicParticle2D):
    def __init__(
        self,
        x: float | int,
        y: float | int,
        color: tuple,
        timer: float | int,
        power: float | int,
        vel_x: float | int,
        vel_y: float | int,
        accel_x: float | int,
        accel_y: float | int,
    ) -> None:
        super().__init__(x, y, color, timer, power, vel_x, vel_y, accel_x, accel_y)

    def render(self, screen: Surface, width: int = 0) -> None:
        pygame.draw.rect(
            screen, self.color, (*self.hitbox.get_pos, self.timer, self.timer), width
        )


class CirclePhisycParticle2D(_PhysicParticle2D):
    def __init__(
        self,
        x: float | int,
        y: float | int,
        color: tuple,
        timer: float | int,
        power: float | int,
        vel_x: float | int,
        vel_y: float | int,
        accel_x: float | int,
        accel_y: float | int,
    ) -> None:
        super().__init__(x, y, color, timer, power, vel_x, vel_y, accel_x, accel_y)

    def render(self, screen: Surface, width: int = 0) -> None:
        pygame.draw.circle(
            screen,
            self.color,
            self.hitbox.get_pos,
            self.timer,
            width,
            draw_top_left=True,
        )
