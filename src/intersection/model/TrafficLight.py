import pygame
import os
from resources import constants as cons


class TrafficLight:
    """
    Represents a traffic light in the simulation.
    """
    
    __colors = ["green", "yellow", "red"]

    def __init__(self, orientation: str, type: str, x: int = 0, y: int = 0):
        """
        Initializes the traffic light with the given parameters.
        """
        self.x = x
        self.y = y
        self.type = type
        self.active_color = "red"
        self.orientation = orientation
        self.__set_image_path(type)
        self.__set_image_size(orientation, type)
        self.image = self.__load_image()
        self.rect = self.image.get_rect(center=(x, y))
    
    def __set_image_size(self, orientation: str, type: str):
        """
        Sets the size of the traffic light based on its orientation and type.
        """
        if type == "street":
            self.image_size = (cons.TRAFFIC_LIGHT_WIDTH, cons.TRAFFIC_LIGHT_LENGTH) if orientation == "vertical" else (cons.TRAFFIC_LIGHT_LENGTH, cons.TRAFFIC_LIGHT_WIDTH)
        else:
            self.image_size = (cons.PEDESTRIAN_LIGHT_WIDTH, cons.PEDESTRIAN_LIGHT_LENGTH) if orientation == "vertical" else (cons.PEDESTRIAN_LIGHT_LENGTH, cons.PEDESTRIAN_LIGHT_WIDTH)

    def __set_image_path(self, type: str):
        """
        Sets the image path for the traffic light based on its type and orientation.
        """
        if type == "street":
            self.image_path = os.path.join(os.path.dirname(__file__), f'../assets/{self.orientation}/{self.active_color}_light.png')
        else:
            self.image_path = os.path.join(os.path.dirname(__file__), f'../assets/{self.orientation}/{self.active_color}_pedestrian.png')

    def get_image_path(self) -> str:
        """
        Returns the image path of the traffic light.
        """
        return self.image_path

    def __load_image(self, rotation: int = 0) -> pygame.Surface:
        """
        Loads and transforms the traffic light's image.
        """
        return pygame.transform.rotate(pygame.transform.scale(pygame.image.load(self.image_path), self.image_size), rotation)

    def set_active_color(self, color: str):
        """
        Sets the active color of the traffic light.
        """
        self.active_color = color

    def change_color(self):
        """
        Changes the traffic light's color to the next one in the sequence.
        """
        try:
            self.active_color = self.__colors[self.__colors.index(self.active_color) + 1]
        except IndexError:
            self.active_color = self.__colors[0]
        self.set_active_color(self.active_color)