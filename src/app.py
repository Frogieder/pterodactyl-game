import pygame
# from pygame.locals import *
from src.player import Player


class App:
    def __init__(self):
        self.sprites = {}
        self._running = True
        self.size = self.width, self.height = 1280, 800

    # noinspection PyAttributeOutsideInit
    def on_init(self) -> bool:
        pygame.init()
        # create window
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption("Pterodaktyln't")
        # set icon
        icon = pygame.image.load("assets/pterodactyl_icon_large.png")
        pygame.display.set_icon(icon)

        self.clock = pygame.time.Clock()

        # create sprites
        self.sprites["player"] = Player(
            surface=self._display_surf,
            position=(self.width / 2, self.height / 2),
            icon_name="pterodactyl.png", size=(50, 50), anchor="c"
        )

        # init done
        self._running = True
        return True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        dt = self.clock.tick(60) / 1000
        print(dt)
        self.sprites["player"].player_loop(dt)

    def on_render(self):
        self._display_surf.fill((0, 255, 0))

        self.render_sprites()

        pygame.display.update()

    def render_sprites(self):
        for sprite in self.sprites.values():
            sprite.render()

    # noinspection PyMethodMayBeStatic
    def on_cleanup(self):
        pygame.quit()

    def on_test(self):
        """
        Some random code to test the app
        """
        self.sprites["player"].set_position((100, 200))

    def on_execute(self):
        if not self.on_init():
            self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            # self.on_test()
            self.on_render()
        self.on_cleanup()
