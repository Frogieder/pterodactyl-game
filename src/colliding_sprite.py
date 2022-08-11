from src.sprite import Sprite
import pygame


class CollidingSprite(Sprite):
    def __init__(self, surface: pygame.Surface, icon_name: str = None, position: tuple | None = None,
                 size: tuple | None = None, anchor: str = "ul"):
        super().__init__(surface=surface, icon_name=icon_name, position=position, size=size, anchor=anchor)
        self.rect = self.icon.get_rect(topleft=(self.position.x, self.position.y))

    def check_collision(self, sprite) -> bool:
        return self.rect.colliderect(sprite.rect)

    def check_collisions(self, sprites, find_all=False):
        if find_all:
            self.rect.collidelistall([sprite.rect for sprite in sprites])
        else:
            self.rect.collidelist([sprite.rect for sprite in sprites])

    def on_loop(self):
        self.rect.topleft = (self.position.x + self._render_offset[0], self.position.y + self._render_offset[1])
