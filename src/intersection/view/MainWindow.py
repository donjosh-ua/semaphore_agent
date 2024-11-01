import time
import pygame
from resources import constants as cons
from src.intersection.model.Entity import Entity
from src.intersection.view.ImageView import ImageView
from src.agent.controller.MasController import MasController
from src.intersection.controller.StreetController import StreetController
from src.intersection.model.Entity import Entity


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

        # instance of entity bus type
        self.street_controller.add_entity(Entity("bus", x=cons.BUS_LENGTH/2, y=459, x_speed=7))
        #self.street_controller.add_entity(Entity("bus", x=300, y=539, x_speed=2))
        
        self.street_controller.add_entity(Entity("bus", x=539, y=cons.SCREEN_SIZE[1]-cons.BUS_LENGTH/2, y_speed=-7, rotation=90))
        #self.street_controller.add_entity(Entity("bus", x=800, y=cons.SCREEN_SIZE[1]-cons.BUS_LENGTH/2, y_speed=-0, rotation=0))
        
        
        # instance of entity person type
        self.street_controller.add_entity(Entity("person", x=cons.PERSON_LENGTH/2, y=380, x_speed=3))
        self.street_controller.add_entity(Entity("person", x=619, y=cons.SCREEN_SIZE[1]-cons.PEDESTRIAN_LIGHT_LENGTH/2 ,y_speed=-3))
        
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
        
        while True:

            # Calculate elapsed time
            elapsed_time: float = time.time() - self.start_time
            
            self.street_controller.handle_events()
            
            # check if control should be switched
            if self.mas_controller.change_control:
                self.mas_controller.update(elapsed_time)
                continue
            
            if elapsed_time > cons.FOURTH_STATE:
                self.start_time = time.time()
            self.mas_controller.update(elapsed_time)

            self.screen.blit(self.background, [0, 0])
            
            #draw the views of the entities
            for entity in self.street_controller.entities:
                #entity.is_moving = self.street_controller.can_move(entity)
                self.street_controller.can_move(entity)
                print(entity.is_moving, entity.is_crossing, sep="|")
                
                
                entity.move()
            
            for view in self.entity_views:
                view.draw(self.screen)
            
            for view in self.entity_views:
                view.draw(self.screen)
                
            #draw the views of the traffic lights 
            for view in self.traffic_light_views:  
                view.draw(self.screen)
                
            pygame.display.flip()
            clock.tick(cons.FRAME_RATE)
            