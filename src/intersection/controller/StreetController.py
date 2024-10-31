import sys
import pygame
from src.intersection.model.TrafficLight import TrafficLight
from src.agent.controller.MasController import MasController

class StreetController:

    mas = MasController()

    def __init__(self):
        self.entities = []
        self.create_agents()

    def create_agents(self):

        horizontal_street_agent = self.mas.create_agent("street", control=True)
        horizontal_street_agent.add_light(TrafficLight("vertical", "street", x=345, y=459))
        horizontal_street_agent.add_light(TrafficLight("vertical", "street", x=345, y=539))
        # horizontal_street_agent.update_state()

        vertical_street_agent = self.mas.create_agent("street")
        vertical_street_agent.add_light(TrafficLight("horizontal", "street", x=539, y=655))
        vertical_street_agent.add_light(TrafficLight("horizontal", "street", x=459, y=655))

        horizontal_pedestrian_agent = self.mas.create_agent("pedestrian", control=True)
        horizontal_pedestrian_agent.add_light(TrafficLight("vertical", "pedestrian", x=420, y=380)) 
        horizontal_pedestrian_agent.add_light(TrafficLight("vertical", "pedestrian", x=420, y=619))
        horizontal_pedestrian_agent.add_light(TrafficLight("vertical", "pedestrian", x=582, y=380))
        horizontal_pedestrian_agent.add_light(TrafficLight("vertical", "pedestrian", x=582, y=619))

        vertical_pedestrian_agent = self.mas.create_agent("pedestrian")
        vertical_pedestrian_agent.add_light(TrafficLight("horizontal", "pedestrian", x=619, y=580))
        vertical_pedestrian_agent.add_light(TrafficLight("horizontal", "pedestrian", x=380, y=420))
        vertical_pedestrian_agent.add_light(TrafficLight("horizontal", "pedestrian", x=619, y=420))
        vertical_pedestrian_agent.add_light(TrafficLight("horizontal", "pedestrian", x=380, y=580))

    def add_entity(self, entity):
        self.entities.append(entity)

    def draw_entities(self, screen):
        for entity in self.entities:
            screen.blit(entity.image, entity.rect)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()