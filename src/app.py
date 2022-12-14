import pygame
# from pygame.locals import *
from src.player import Player
from src.data_structures.colors import Color


class App:
    def __init__(self):
        self.sprites = {}
        self.size = self.width, self.height = 1280, 800

        pygame.init()
        # create window
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption("Pterodaktyln't")
        # set icon
        icon = pygame.image.load("assets/pterodactyl_icon_large.png")
        pygame.display.set_icon(icon)

        # create sprites
        self.sprites["player"] = Player(
            surface=self._display_surf,
            position=(self.width / 2, self.height / 2),
            icon_name="pterodactyl.png", size=(50, 50), anchor="c"
        )
        # other definitions
        self.clock = pygame.time.Clock()
        self.fps_counter = pygame.font.Font("assets/RobotoCondensed-Italic.ttf", 48)

        # init done
        self._running = True

    def on_event(self, event):
        # print(event)
        if event.type == pygame.KEYDOWN:
            self.sprites["player"].y_body.velocity = -1000
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        dt = self.clock.tick(60) / 1000
        self.sprites["player"].on_loop(dt)

    def on_render(self):
        self._display_surf.fill(Color.green)
        self._display_surf.blit(
            self.fps_counter.render(f"{self.clock.get_fps():.0f} FPS", True, (255, 255, 255)),
            (0, 0)
        )
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
        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            # self.on_test()
            self.on_render()
        self.on_cleanup()
