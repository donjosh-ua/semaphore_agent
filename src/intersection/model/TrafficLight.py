import pygame
import os

from resources import constants as cons


class TrafficLight:

    __colors = ["green", "yellow", "red"]
 
    def __init__(self, orientation, type, x=0, y=0):
        self.x = x
        self.y = y
        self.type = type
        self.active_color = "red"
        self.orientation = orientation
        self.__set_image_path(type)
        self.__set_size(orientation, type)
        self.image = self.__load_image()
        self.rect = self.image.get_rect(center=(x, y))
    
    def __set_size(self, orientation, type):
        if type == "street":
            self.image_size = (cons.TRAFFIC_LIGHT_WIDTH, cons.TRAFFIC_LIGHT_LENGTH) if orientation == "vertical" else (cons.TRAFFIC_LIGHT_LENGTH, cons.TRAFFIC_LIGHT_WIDTH)
        else:
            self.image_size = (cons.PEDESTRIAN_LIGHT_WIDTH, cons.PEDESTRIAN_LIGHT_LENGTH) if orientation == "vertical" else (cons.PEDESTRIAN_LIGHT_LENGTH, cons.PEDESTRIAN_LIGHT_WIDTH)

    def __set_image_path(self, type):
        if type == "street":
            self.image_path = os.path.join(os.path.dirname(__file__), f'../assets/{self.orientation}/{self.active_color}_light.png')
        else:
            self.image_path = os.path.join(os.path.dirname(__file__), f'../assets/{self.orientation}/{self.active_color}_pedestrian.png')

    def get_image_path(self):
        return self.image_path

    def __load_image(self, rotacion=0):
        return pygame.transform.rotate( #* rota la imagen
                pygame.transform.scale( #* redimensiona la imagen
                pygame.image.load(self.image_path), self.image_size),  #* carga la imagen
                rotacion)

    def set_active_color(self, color):
        self.active_color = color

    def change_color(self):
        try:
            self.active_color = self.__colors[self.__colors.index(self.active_color) + 1]
        except Exception as e:
            self.active_color = self.__colors[0]
        self.set_active_color(self.active_color)
