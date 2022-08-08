from src.sprite import Sprite
from src.data_structures.body_1d import Body1D
import pygame
from math import atan, pi


class Player(Sprite):
    def __init__(self, surface: pygame.Surface, icon_name: str = None, position: tuple | None = None,
                 size: tuple | None = None, anchor: str = ""):
        super().__init__(surface=surface, icon_name=icon_name, position=position, size=size, anchor=anchor)
        self.direction = 1
        self.bounds = self.surface.get_size()
        self.bounds = ((self.icon.get_size()[0]/2, self.bounds[0]-self.icon.get_size()[0]/2),
                       (self.icon.get_size()[1]/2, self.bounds[1]-self.icon.get_size()[1]/2))
        self.x_velocity = 400
        self.y_body = Body1D(self.position.y, gravity=1200)
        self.rotation_angle = 0

    def player_loop(self, dt: float):
        self.position.x += self.x_velocity * dt * self.direction
        if False in self.check_bounds_x():
            self.direction *= -1
            self.icon = pygame.transform.flip(self.icon, flip_x=True, flip_y=False)

        self.position.y = self.y_body.time_step(dt)
        y_bounds_check = self.check_bounds_y(True)
        if False in y_bounds_check:
            self.y_body.velocity = -self.y_body.velocity
            self.y_body.position = self.position.y

        self.rotation_angle = atan(self.y_body.velocity / self.x_velocity) / pi * 180 * self.direction * -1

    def check_bounds_x(self, fix_pos: bool = False):
        result = [True] * 2
        if self.position.x < self.bounds[0][0]:
            if fix_pos:
                self.position.x = self.bounds[0][0]
            result[0] = False
        elif self.position.x > self.bounds[0][1]:
            if fix_pos:
                self.position.x = self.bounds[0][1]
            result[1] = False
        return result

    def check_bounds_y(self, fix_pos: bool = False):
        result = [True] * 2
        if self.position.y < self.bounds[1][0]:
            if fix_pos:
                self.position.y = self.bounds[1][0]
            result[0] = False
        elif self.position.y > self.bounds[1][1]:
            if fix_pos:
                self.position.y = self.bounds[1][1]
            result[1] = False
        return result

    def check_bounds(self):
        return self.check_bounds_x(), self.check_bounds_y()

    def set_position(self, pos):
        super().set_position(pos)

    def render(self):
        self.surface.blit(pygame.transform.rotate(self.icon, self.rotation_angle),
                          (self.position.x + self._render_offset[0], self.position.y + self._render_offset[1]))
