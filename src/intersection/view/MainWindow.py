import time
import pygame
from resources import constants as cons
from src.intersection.model.Entity import Entity
from src.intersection.view.ImageView import ImageView
from src.agent.controller.MasController import MasController
from src.intersection.controller.StreetController import StreetController


class MainWindow:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(MainWindow, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):

        # singleton pattern
        if hasattr(self, '_initialized'):
            return

        # initialize pygame
        pygame.init()
        self.screen = pygame.display.set_mode(cons.SCREEN_SIZE)
        pygame.display.set_caption("Traffic simulation")
        self.background_path = "src/intersection/assets/background.png"
        self.background = pygame.transform.scale(
            pygame.image.load(self.background_path).convert(), 
            cons.SCREEN_SIZE)
        
        # instantiate controllers
        self.mas_controller = MasController()
        self.street_controller = StreetController()

        # create views for traffic lights
        self.traffic_light_views = []
        for agent in self.mas_controller.get_agents():
            for light in agent.get_lights():
                self.traffic_light_views.append(ImageView(light))

        # create views for entities
        self.entity_views = [ImageView(entity) for entity in self.street_controller.entities]

        # start time
        self.start_time = time.time()

        self._initialized = True
        self.run()

    def run(self):

        clock = pygame.time.Clock()

        # fixed spawn points for buses
        vertical_spawn_points = [(20, 459), (20, 539)]
        horizontal_spawn_points = [(459, 980), (539, 980)]

        while True:

            # Calculate elapsed time
            elapsed_time: float = time.time() - self.start_time
            
            self.street_controller.handle_events()

            # check if control should be switched
            if self.mas_controller.change_control:
                self.mas_controller.update(elapsed_time)
                continue

            # reset start time if limit is reached
            if elapsed_time > cons.STRAIGHT_RED_TIME:
                self.start_time = time.time()
            
            # update agents
            self.mas_controller.update(elapsed_time)

            self.screen.blit(self.background, [0, 0])

            # draw entities
            for view in self.traffic_light_views:  
                view.draw(self.screen)
                
            pygame.display.flip()
            clock.tick(cons.FRAME_RATE)
            