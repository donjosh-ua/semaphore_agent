import sys
import time
import pygame
from resources import constants as cons
from src.intersection.model.TrafficLight import TrafficLight
from src.agent.controller.MasController import MasController
from src.intersection.model.Traffic import Traffic
from src.intersection.model.Entity import Entity

class StreetController:

    mas = MasController()

    def __init__(self):
        self.entities = []
        self.agent_entitites = dict()
        self.create_agents()

    def create_agents(self):

        self.horizontal_street_agent = self.mas.create_agent("street", control=True)
        self.horizontal_street_agent.add_light(TrafficLight("vertical", "street", x=345, y=459))
        self.horizontal_street_agent.add_light(TrafficLight("vertical", "street", x=345, y=539))

        self.vertical_street_agent = self.mas.create_agent("street")
        self.vertical_street_agent.add_light(TrafficLight("horizontal", "street", x=539, y=655))
        self.vertical_street_agent.add_light(TrafficLight("horizontal", "street", x=459, y=655))

        self.horizontal_pedestrian_agent = self.mas.create_agent("pedestrian", control=True)
        self.horizontal_pedestrian_agent.add_light(TrafficLight("vertical", "pedestrian", x=420, y=380)) 
        self.horizontal_pedestrian_agent.add_light(TrafficLight("vertical", "pedestrian", x=420, y=619))
        self.horizontal_pedestrian_agent.add_light(TrafficLight("vertical", "pedestrian", x=582, y=380))
        self.horizontal_pedestrian_agent.add_light(TrafficLight("vertical", "pedestrian", x=582, y=619))

        self.vertical_pedestrian_agent = self.mas.create_agent("pedestrian")
        self.vertical_pedestrian_agent.add_light(TrafficLight("horizontal", "pedestrian", x=619, y=580))
        self.vertical_pedestrian_agent.add_light(TrafficLight("horizontal", "pedestrian", x=380, y=420))
        self.vertical_pedestrian_agent.add_light(TrafficLight("horizontal", "pedestrian", x=619, y=420))
        self.vertical_pedestrian_agent.add_light(TrafficLight("horizontal", "pedestrian", x=380, y=580))

    def add_entity(self, entity, name=None):
        
        self.entities.append(entity)
    
    def can_move(self, entity:Entity):
        """
        Each conditional match only the entity and trafficlight when they are for the same type, and there are in the same street,
        It's important the coordenates from trafficLight and entity to coordinate
        This funtion return a list: [boolean can move, boolean if the entity is crossing] # in this version only return [boolean can move, False]
        """
        if entity.vel_y == 0  and entity.type == "bus":
            for trafficLight in self.horizontal_street_agent.get_lights():
                if Traffic.is_same_street(entity.y, trafficLight.y):
                    return [not (Traffic.is_influenciable(entityCorner=entity.x + cons.BUS_LENGTH/2, trafficLigthCorner=trafficLight.x, velocityEntity=entity.vel_x*cons.TRESHOLD_BUS) and trafficLight.active_color != "green"), False]
                    
        if entity.vel_x == 0  and entity.type == "bus":
            for trafficLight in self.vertical_street_agent.get_lights(): 
                if Traffic.is_same_street(entity.x, trafficLight.x):
                    return [not (Traffic.is_influenciable(entityCorner= -(entity.y - cons.BUS_LENGTH/2), trafficLigthCorner= -trafficLight.y, velocityEntity= -entity.vel_y*cons.TRESHOLD_BUS) and trafficLight.active_color != "green"), False]
                
        if entity.vel_y == 0  and entity.type == "person":
            for trafficLight in self.horizontal_pedestrian_agent.get_lights(): 
                if Traffic.is_same_street(entity.y, trafficLight.y):
                    return [not (Traffic.is_influenciable(entityCorner=entity.x + cons.PERSON_LENGTH/2, trafficLigthCorner=trafficLight.x, velocityEntity=entity.vel_x*cons.TRESHOLD_PERSON) and trafficLight.active_color != "green"), False]
        
        if entity.vel_x == 0  and entity.type == "person":
            for trafficLight in self.vertical_pedestrian_agent.get_lights():
                if Traffic.is_same_street(entity.x, trafficLight.x):
                    return [not (Traffic.is_influenciable(entityCorner= -(entity.y + cons.PERSON_LENGTH/2), trafficLigthCorner= -trafficLight.y, velocityEntity= -entity.vel_y*cons.TRESHOLD_BUS) and trafficLight.active_color != "green"), False]

    def draw_entities(self, screen):
        for entity in self.entities:
            screen.blit(entity.image, entity.rect)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()