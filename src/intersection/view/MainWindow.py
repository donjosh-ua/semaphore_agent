import pygame
from resources import constants as cons
from src.intersection.view.ImageView import ImageView
from src.intersection.controller.StreetController import StreetController


class MainWindow:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(MainWindow, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, '_initialized'):
            pygame.init()
            self.screen = pygame.display.set_mode(cons.SCREEN_SIZE)
            pygame.display.set_caption("Traffic simulation")
            self.background_path = "src/intersection/assets/background.png"
            self.background = pygame.transform.scale(pygame.image.load(self.background_path).convert(), cons.SCREEN_SIZE)

            self._initialized = True
            self.run()

    def run(self):

        clock = pygame.time.Clock()
        views = []

        vertical_spawn_points = [(20, 459), (20, 539)]
        horizontal_spawn_points = [(459, 980), (539, 980)]

        controller = StreetController()

        for agent in controller.mas.get_agents():
            for light in agent.get_lights():
                views += [ImageView(light)]

        while True:

            controller.handle_events()
            self.screen.blit(self.background, [0, 0])

            for view in views:  
                view.draw(self.screen)
                
            pygame.display.flip()
            clock.tick(cons.FRAME_RATE)