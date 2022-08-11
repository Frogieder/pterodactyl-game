from src.data_structures.position import Position
import pygame


class Sprite:
    def __init__(self, surface: pygame.Surface, icon_name: str = None, position: tuple | None = None,
                 size: tuple | None = None, anchor: str = "ul"):
        self.icon_name = "error.png"
        self.icon: pygame.Surface | None = None
        self.set_icon(icon_name)
        self.surface = surface

        if position is not None:
            self.position = Position.from_touple(position)
        else:
            self.position = Position(0, 0)

        if size is not None:
            self.set_size(size)

        self._render_offset = (0, 0)
        self.anchor = anchor.lower()
        self.set_anchor(self.anchor)

    def set_anchor(self, anchor: str):
        if "u" in anchor:
            x_offset = 0
        elif "d" in anchor:
            x_offset = -self.icon.get_size()[0]
        else:
            x_offset = -self.icon.get_size()[0] / 2

        if "r" in anchor:
            y_offset = 0
        elif "l" in anchor:
            y_offset = -self.icon.get_size()[1]
        else:
            y_offset = -self.icon.get_size()[1] / 2

        self._render_offset = (x_offset, y_offset)

    def set_icon(self, icon_name):
        self.icon_name = icon_name if icon_name is not None else "error.png"
        self.icon = pygame.image.load(f"assets/{icon_name}")

    def render(self):
        self.surface.blit(self.icon,
                          (self.position.x + self._render_offset[0], self.position.y + self._render_offset[1]))

    def set_size(self, size: tuple | None):
        self.set_icon(self.icon_name)
        self.icon = pygame.transform.scale(self.icon, size)

    def set_position(self, pos):
        self.position.x = pos[0]
        self.position.y = pos[1]
