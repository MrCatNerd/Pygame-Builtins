__author__ = "Alon B.R."
import pygame

pygame.init()


def in_screen(screen_with, screen_height, x, y, obj_width, obj_height) -> bool:
    """checks if a point is in range of WIDTH,HEIGHT"""
    if (
        x - obj_width > 0
        and x <= screen_with
        and y - obj_height > 0
        and y <= screen_height
    ):
        return True
    return False


class Vector2:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def add(self, vector2) -> None:
        self.x += vector2.x
        self.y += vector2.y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_tuple(self) -> tuple:
        return (self.get_x(), self.get_y())


class Vector3:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

    def add(self, vector3) -> None:
        if type(vector3) is tuple or type(vector3) is list:
            vector3 = Vector3(vector3[0], vector3[1], vector3[2])

        self.x += vector3.x
        self.y += vector3.y
        self.z += vector3.z

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z

    def get_tuple(self) -> tuple:
        return (self.get_x(), self.get_y(), self.get_z())


class BooleanSet:
    def __init__(self, **kwargs) -> None:
        for key, value in kwargs.items():
            exec(f"self.{key} = {value}")


class RectParticle:
    def __init__(
        self,
        x: int,
        y: int,
        color: tuple,
        vel_x: float | int,
        vel_y: float | int,
        accel_x: float | int,
        accel_y: float | int,
        timer: float | int,
        power: float | int,
    ) -> None:

        self.rect = pygame.Rect(x, y, timer, timer)

        self.color: tuple = color
        self.color = min(self.color, (255, 255, 255))
        self.color = max(self.color, (0, 0, 0))

        self.vel_x = vel_x
        self.vel_y = vel_y

        self.accel_x = accel_x
        self.accel_y = accel_y

        self.timer = timer
        self.power = power

        self.kill: bool = False

    def update(self, window, DeltaTime=None) -> None:
        if DeltaTime is None:
            DeltaTime = 1

        self.timer -= self.power * DeltaTime

        self.vel_x += self.accel_x * DeltaTime
        self.vel_y += self.accel_y * DeltaTime

        self.rect.x += self.vel_x * DeltaTime
        self.rect.y += self.vel_y * DeltaTime

        pygame.draw.rect(window, self.color, self.rect)

        if self.timer <= 0:
            self.kill = True
        elif self.timer > 0 and self.kill is True:
            self.kill = False


class CircleParticle:
    def __init__(
        self,
        x: int,
        y: int,
        color: tuple,
        vel_x: float | int,
        vel_y: float | int,
        accel_x: float | int,
        accel_y: float | int,
        timer: float | int,
        power: float | int,
    ) -> None:

        self.rect = pygame.Rect(x, y, timer, timer)

        self.color: tuple = color
        self.color = min(self.color, (255, 255, 255))
        self.color = max(self.color, (0, 0, 0))

        self.vel_x = vel_x
        self.vel_y = vel_y

        self.accel_x = accel_x
        self.accel_y = accel_y

        self.timer = timer
        self.power = power

        self.kill: bool = False

    def update(self, window, DeltaTime=None) -> None:
        if DeltaTime is None:
            DeltaTime = 1

        self.timer -= self.power * DeltaTime

        self.vel_x += self.accel_x * DeltaTime
        self.vel_y += self.accel_y * DeltaTime

        self.rect.x += self.vel_x * DeltaTime
        self.rect.y += self.vel_y * DeltaTime

        pygame.draw.circle(window, self.color, (self.rect.x, self.rect.y), self.timer)

        if self.timer <= 0:
            self.kill = True
        elif self.timer > 0 and self.kill is True:
            self.kill = False


class ImgParticle:
    def __init__(
        self,
        img,
        x: int,
        y: int,
        vel_x: float | int,
        vel_y: float | int,
        accel_x: float | int,
        accel_y: float | int,
        timer: float | int,
        power: float | int,
    ) -> None:

        self.img = img

        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.vel_x = vel_x
        self.vel_y = vel_y

        self.accel_x = accel_x
        self.accel_y = accel_y

        self.timer = timer
        self.power = power

        self.kill: bool = False

    def update(self, window, DeltaTime=None) -> None:
        if DeltaTime is None:
            DeltaTime = 1

        self.timer -= self.power * DeltaTime

        self.vel_x += self.accel_x * DeltaTime
        self.vel_y += self.accel_y * DeltaTime

        self.rect.x += self.vel_x * DeltaTime
        self.rect.y += self.vel_y * DeltaTime

        window.blit(self.img, self.rect)

        if self.timer <= 0:
            self.kill = True
        elif self.timer > 0 and self.kill is True:
            self.kill = False


class Button:
    def __init__(self, x, y, img) -> None:
        self.img = img
        self.width = self.img.get_width()
        self.height = self.img.get_height()

        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.clicked = False
        self.clicked_one = False

        self.click_type_table = {
            "left": 0,
            "middle": 1,
            "right": 2,
            "side1": 3,
            "side2": 4,
            "side3": 4,
        }

    def update(self, window, mx, my, click_type: str) -> None:

        if (
            in_screen(self.width, self.height, mx, my, 0, 0)
            and pygame.mouse.get_pressed()[self.click_type_table[click_type]]
        ):
            self.clicked_one = True
            self.clicked = True
        elif self.clicked is True:
            self.clicked = False

        window.blit(self.img, self.rect)

    def update_clicks(self) -> None:
        """if you want to use if self.clicked is True
        and you want it to work then active this function"""
        if self.clicked is True:
            self.clicked = False

    def help_click_type(self) -> None:
        print(
            """click_type arg means::
              left = left click input
              right = right click input
              middle = middle click input
              side 1 = side button 1 click input
              side 2 = side button 2 click input
              side 3 = side button 3 click input
              """
        )


class TileBased:
    class Settings:
        """Dont have to do this but theese are the basic requirements for this TileBased thing
        you can just look at the args"""

        def print_args() -> str:
            print(
                """
                  WIDTH,
                  HEIGHT,
                  GRAVITY,
                  SCALE,
                  TILE SIZE,
                  ICON(dont have to do this one),
                  FPS_LIMIT(in settings if its None then u got unlimited fps and it will create you the self.clock only if its not none)
                  """
            )

        def __init__(
            self,
            WIDTH,
            HEIGHT,
            GRAVITY,
            SCALE,
            TILE_SIZE,
            ICON=None,
            FPS_LIMIT: int = None,
        ):
            """self.clock will not be created if self.FPS_LIMIT is None"""
            self.WIDTH = WIDTH
            self.HEIGHT = HEIGHT
            self.ICON = ICON
            self.FPS_LIMIT = FPS_LIMIT
            if self.FPS_LIMIT is not None:
                self.clock = pygame.time.Clock()
            self.TILE_SIZE = TILE_SIZE

            # physics
            self.GRAVITY = GRAVITY
            self.SCALE = SCALE

    class Tile:
        def __init__(
            self,
            x: int,
            y: int,
            img,
            bouncy_multiplier: float | int,
            tag: str = "tile",
            name: str = "Tile",
        ) -> None:
            self.img = img
            self.width = self.img.get_width()
            self.height = self.img.get_height()

            self.rect = self.img.get_rect()
            self.rect.x = x
            self.rect.y = y

            self.bouncy_multiplier: float | int = bouncy_multiplier

            self.tag: str = tag
            self.name: str = name

        def update(self, window, add_x=None, add_y=None) -> None:
            if add_x is None:
                add_x = 0
            if add_y is None:
                add_y = 0
            window.blit(self.img, (self.rect.x + add_x, self.rect.y + add_y))

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
            self.width = self.img.get_width()
            self.height = self.img.get_height()

            self.rect = self.img.get_rect()
            self.rect.x = x
            self.rect.y = y

            self.tag: str = tag
            self.name: str = name

            # physics
            self.mass = mass
            self.velocity = Vector2(0, 0)
            self.active_directions = BooleanSet(x=True, y=True)
            self.direction_for_axis = Vector2(1, 1)
            self.acceleration = Vector2(
                (self.mass * GRAVITY) / SCALE, (self.mass * GRAVITY) / SCALE
            )

            # AI
            self.active_AI: bool = True

        def update(
            self, window, tile_list: list, DeltaTime=None, add_x=None, add_y=None
        ) -> None:
            if DeltaTime is None:
                DeltaTime = 1

            if add_x is None:
                add_x = 0

            if add_y is None:
                add_y = 0

            dx = 0
            dy = 0

            # gravity
            self.velocity.x += self.acceleration.x * DeltaTime
            self.velocity.y += self.acceleration.y * DeltaTime

            dx += self.velocity.x
            dy += self.veloicty.y

            # collision detection

            for tile in tile_list:

                if tile.rect.colliderect(  # y collision detection
                    self.rect.x + dy, self.rect.y, self.width, self.height
                ):
                    if dx > 0:
                        dx = (self.rect.x + self.width) - tile.rect.x
                    elif dx < 0:
                        dx = self.rect.x - (tile.rect.x + tile.width)

                    self.velocity.x = 0

                ##############################################################

                if tile.rect.colliderect(  # y collision detection
                    self.rect.x, self.rect.y + dy, self.width, self.height
                ):
                    if dy > 0:
                        dy = self.rect.bottom - tile.rect.top
                    elif dy < 0:
                        dy = self.rect.top - tile.rect.bottom

                    self.velocity.y = 0

            self.rect.x += dx
            self.rect.y += dy

            window.blit(self.img, (self.rect.x + add_y, self.rect.y + add_y))

        def init_AI(self):
            self.progress = 0

        def AI(self, walk_range: int | float, speed: int | float, start_direction=None):
            if start_direction is None:
                start_direction = 1  # right

            direction = start_direction
            del start_direction

            if self.active_AI:
                self.rect.x += speed * direction
                self.progress += speed * direction
                if self.progress >= walk_range:
                    self.progress *= -1
                    direction *= -1

    class ImgPhysicParticle:
        def __init__(
            self,
            x: int | float,
            y: int | float,
            img,
            bouncy_multiplier: float | int,
            timer: int | float,
            power: int | float,
            vel_x: int | float,
            vel_y: int | float,
            GRAVITY: int | float,
            SCALE: int | float,
            mass: int | float,
            active_accel_x: bool = False,
            active_accel_y: bool = True,
            use_img_size: bool = None,
            const_size: int | float = None,
        ) -> None:

            self.use_img_size = False
            self.const_size = False

            if use_img_size is None:
                self.use_img_size = False
            elif use_img_size is True:
                self.use_img_size = True

            if timer < 0:
                self.infinite_time = True
            else:
                self.infinite_time = False

            if const_size is None:
                self.const_size = False
                self.size = timer
            elif self.use_img_size is None or self.use_img_size is False:
                self.const_size = True
                self.size = const_size

            if self.use_img_size is True:
                self.img = img
                self.rect = self.img.get_rect()
                self.size_x = self.img.get_width()
                self.size_y = self.img.get_height()
            else:
                self.img = pygame.transform.scale(img, (self.size, self.size))
                self.rect = pygame.Rect(x, y, self.size, self.size)

            self.rect.x = x
            self.rect.y = y

            self.bouncy_multiplier: float | int = bouncy_multiplier
            self.mass = mass
            self.velocity = Vector2(vel_x, vel_y)
            self.acceleration = Vector2(
                ((self.mass * GRAVITY) / SCALE) * int(active_accel_x),
                ((self.mass * GRAVITY) / SCALE) * int(active_accel_y),
            )

            self.timer = timer
            self.power = power

            self.kill: bool = False

        def update(
            self, window, tile_list, DeltaTime=None, add_x=None, add_y=None
        ) -> None:
            if DeltaTime is None:
                DeltaTime = 1

            if add_x is None:
                add_x = 0
            if add_y is None:
                add_y = 0

            if self.infinite_time is False:
                self.timer -= self.power * DeltaTime
            if self.const_size is False:
                self.size = self.timer

            dx = 0
            dy = 0

            self.velocity.x += self.acceleration.x * DeltaTime
            self.velocity.y += self.acceleration.y * DeltaTime

            dx += self.velocity.x
            dy += self.velocity.y

            # collision detection

            if len(tile_list) > 0:
                # x collision detection
                for tile in tile_list:

                    if self.use_img_size:
                        if tile.rect.colliderect(
                            self.rect.x + dx, self.rect.y, self.size_x, self.size_y
                        ):
                            if dx > 0:
                                dx = (self.rect.x + self.timer) - tile.rect.x
                            elif dx < 0:
                                dx = self.rect.x - (tile.rect.x + tile.width)

                            self.velocity.x *= -1 * (
                                self.bouncy_multiplier * tile.bouncy_multiplier
                            )
                    else:
                        if tile.rect.colliderect(
                            self.rect.x + dx, self.rect.y, self.size, self.size
                        ):
                            if dx > 0:
                                dx = (self.rect.x + self.timer) - tile.rect.x
                            elif dx < 0:
                                dx = self.rect.x - (tile.rect.x + tile.width)

                            self.velocity.x *= -1 * (
                                self.bouncy_multiplier * tile.bouncy_multiplier
                            )

                    # y collision detection
                    for tile in tile_list:
                        if self.use_img_size:
                            if tile.rect.colliderect(
                                self.rect.x, self.rect.y + dy, self.size_x, self.size_y
                            ):
                                if dy > 0:
                                    dy = self.rect.bottom - tile.rect.top
                                elif dy < 0:
                                    dy = self.rect.top - tile.rect.bottom

                                self.velocity.y *= -1 * (
                                    self.bouncy_multiplier * tile.bouncy_multiplier
                                )
                        else:
                            if tile.rect.colliderect(
                                self.rect.x, self.rect.y + dy, self.size, self.size
                            ):
                                if dy > 0:
                                    dy = self.rect.bottom - tile.rect.top
                                elif dy < 0:
                                    dy = self.rect.top - tile.rect.bottom

                                self.velocity.y *= -1 * (
                                    self.bouncy_multiplier * tile.bouncy_multiplier
                                )
            # adding values to position
            self.rect.x += dx
            self.rect.y += dy

            # updating rect size
            if self.const_size is False:
                self.rect = pygame.Rect(
                    self.rect.x, self.rect.y, self.timer, self.timer
                )

            # bliting the img to screen at the position
            window.blit(self.img, (self.rect.x + add_x, self.rect.y + add_y))

            if self.timer <= 0 and self.infinite_time is False:
                self.kill = True
            elif self.timer > 0 and self.kill is True:
                self.kill = False

    class RectPhysicParticle:
        def __init__(
            self,
            x,
            y,
            color: tuple,
            bouncy_multiplier: float | int,
            timer,
            power,
            vel_x,
            vel_y,
            GRAVITY,
            SCALE,
            mass,
            active_accel_x: bool = False,
            active_accel_y: bool = True,
            const_size: int | float = None,
        ) -> None:

            if const_size is None:
                self.const_size = False
                self.size = timer
            else:
                self.const_size = True
                self.size = const_size

            if timer < 0:
                self.infinite_time = True
            else:
                self.infinite_time = False

            self.color: tuple = color

            self.rect = pygame.Rect(x, y, self.size, self.size)

            self.bouncy_multiplier: float | int = bouncy_multiplier
            self.mass = mass
            self.velocity = Vector2(vel_x, vel_y)
            self.acceleration = Vector2(
                ((self.mass * GRAVITY) / SCALE) * int(active_accel_x),
                ((self.mass * GRAVITY) / SCALE) * int(active_accel_y),
            )

            self.timer = timer
            self.power = power

            self.kill: bool = False

        def update(
            self, window, tile_list, DeltaTime=None, add_x=None, add_y=None
        ) -> None:
            if DeltaTime is None:
                DeltaTime = 1

            if add_x is None:
                add_x = 0

            if add_y is None:
                add_y = 0

            if self.infinite_time is False:
                self.timer -= self.power
            if self.const_size is False:
                self.size = self.timer

            dx = 0
            dy = 0

            self.velocity.x += self.acceleration.x * DeltaTime
            self.velocity.y += self.acceleration.y * DeltaTime

            dx += self.velocity.x
            dy += self.velocity.y

            # collision detection

            if len(tile_list) > 0:
                for tile in tile_list:
                    # x collision detection
                    if tile.rect.colliderect(
                        self.rect.x + dx, self.rect.y, self.size, self.size
                    ):
                        if dx > 0:
                            dx = (self.rect.x + self.size) - tile.rect.x
                        elif dx < 0:
                            dx = self.rect.x - (tile.rect.x + tile.width)

                        self.velocity.x *= -1 * (
                            self.bouncy_multiplier * tile.bouncy_multiplier
                        )

                    # y collision detection
                    for tile in tile_list:
                        if tile.rect.colliderect(
                            self.rect.x, self.rect.y + dy, self.size, self.size
                        ):
                            if dy > 0:
                                dy = self.rect.bottom - tile.rect.top
                            elif dy < 0:
                                dy = self.rect.top - tile.rect.bottom

                            self.velocity.y *= -1 * (
                                self.bouncy_multiplier * tile.bouncy_multiplier
                            )
            # adding values to position
            self.rect.x += dx
            self.rect.y += dy

            # updating rect size
            if self.const_size is False:
                self.rect = pygame.Rect(
                    self.rect.x, self.rect.y, self.timer, self.timer
                )

            # drawing a shape to the screen at the position
            pygame.draw.rect(
                window,
                self.color,
                (self.rect.x + add_x, self.rect.y + add_y, self.size, self.size),
            )

            if self.timer <= 0 and self.infinite_time is False:
                self.kill = True
            elif self.timer > 0 and self.kill is True:
                self.kill = False

    class CirclePhysicParticle:
        def __init__(
            self,
            x,
            y,
            color: tuple,
            bouncy_multiplier: float | int,
            timer,
            power,
            vel_x,
            vel_y,
            GRAVITY,
            SCALE,
            mass,
            active_accel_x: bool = False,
            active_accel_y: bool = True,
            const_size: int | float = None,
        ) -> None:

            if const_size is None:
                self.const_size = False
                self.size = timer
            else:
                self.const_size = True
                self.size = const_size

            if timer < 0:
                self.infinite_time = True
            else:
                self.infinite_time = False

            self.color: tuple = color

            self.rect = pygame.Rect(x, y, self.size, self.size)

            self.bouncy_multiplier: float | int = bouncy_multiplier
            self.mass = mass
            self.velocity = Vector2(vel_x, vel_y)
            self.acceleration = Vector2(
                ((self.mass * GRAVITY) / SCALE) * int(active_accel_x),
                ((self.mass * GRAVITY) / SCALE) * int(active_accel_y),
            )

            self.timer = timer
            self.power = power

            self.width = self.size
            self.height = self.size

            self.kill: bool = False

        def update(
            self, window, tile_list, DeltaTime=None, add_x=None, add_y=None
        ) -> None:
            if DeltaTime is None:
                DeltaTime = 1

            if add_x is None:
                add_x = 0

            if add_y is None:
                add_y = 0

            if self.infinite_time is False:
                self.timer -= self.power * DeltaTime

            if self.const_size is False:
                self.size = self.timer

            dx = 0
            dy = 0

            self.velocity.x += self.acceleration.x * DeltaTime
            self.velocity.y += self.acceleration.y * DeltaTime

            dx += self.velocity.x
            dy += self.velocity.y

            # collision detection

            if len(tile_list) > 0:
                for tile in tile_list:
                    # x collision detection
                    if tile.rect.colliderect(
                        self.rect.x + dx, self.rect.y, self.size, self.size
                    ):
                        if dx > 0:
                            dx = (self.rect.x + self.size) - tile.rect.x
                        elif dx < 0:
                            dx = self.rect.x - (tile.rect.x + tile.width)

                        self.velocity.x *= -1 * (
                            self.bouncy_multiplier * tile.bouncy_multiplier
                        )

                    # y collision detection
                    for tile in tile_list:
                        if tile.rect.colliderect(
                            self.rect.x, self.rect.y + dy, self.size, self.size
                        ):
                            if dy > 0:
                                dy = self.rect.bottom - tile.rect.top
                            elif dy < 0:
                                dy = self.rect.top - tile.rect.bottom

                            self.velocity.y *= -1 * (
                                self.bouncy_multiplier * tile.bouncy_multiplier
                            )
            # adding values to position
            self.rect.x += dx
            self.rect.y += dy

            # updating rect size
            if self.const_size is False:
                self.rect = pygame.Rect(
                    self.rect.x - (self.size // 2),
                    self.rect.y - (self.size // 2),
                    self.size,
                    self.size,
                )

            # drawing a shape to the screen at the position
            pygame.draw.circle(
                window,
                self.color,
                (self.rect.x + add_x, self.rect.y + add_y),
                self.size,
            )

            if self.timer <= 0 and self.infinite_time is False:
                self.kill = True
            elif self.timer > 0 and self.kill is True:
                self.kill = False
