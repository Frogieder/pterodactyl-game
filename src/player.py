from src.sprite import Sprite
import pygame


class Player(Sprite):
    def __init__(self, surface: pygame.Surface, icon_name: str = None, position: tuple | None = None,
                 size: tuple | None = None, anchor: str = ""):
        super().__init__(surface=surface, icon_name=icon_name, position=position, size=size, anchor=anchor)
        self.direction = 1
        self.bounds = self.surface.get_size()
        self.bounds = ((self.icon.get_size()[0]/2, self.bounds[0]-self.icon.get_size()[0]/2),
                       (self.icon.get_size()[1]/2, self.bounds[1]-self.icon.get_size()[1]/2))
        self.speed = 400

    def player_loop(self, dt: float):
        self.position.x += self.speed * dt * self.direction
        self.direction *= -1 if False in self.check_bounds() else 1

    def check_bounds(self):
        result = [True] * 4
        if self.position.x < self.bounds[0][0]:
            self.position.x = self.bounds[0][0]
            result[0] = False
        elif self.position.x > self.bounds[0][1]:
            self.position.x = self.bounds[0][1]
            result[1] = False
        if self.position.y < self.bounds[1][0]:
            self.position.y = self.bounds[1][0]
            result[2] = False
        elif self.position.y > self.bounds[1][1]:
            self.position.y = self.bounds[1][1]
            result[3] = False
        return result
