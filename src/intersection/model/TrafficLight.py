import pygame
import os

class TrafficLight:

    __colors = ['green', 'yellow', 'red']
 
    def __init__(self, orientation, type, x=0, y=0):
        self.orientation = orientation
        self.type = type
        self.x = x
        self.y = y
        self.active_color = "red"
        self.set_image_path(type)
        self.set_size(orientation, type)
        self.image = self.load_image()
        self.rect = self.image.get_rect(center=(self.x, self.y))
    
    def set_size(self, orientation, type):
        if type == "street":
            self.image_size = (25, 93) if orientation == "vertical" else (93, 25)
        else:
            self.image_size = (20, 60) if orientation == "vertical" else (60, 20)

    def set_image_path(self, type):
        if type == "street":
            self.image_path = os.path.join(os.path.dirname(__file__), f'../assets/{self.orientation}/{self.active_color}_light.png')
        else:
            self.image_path = os.path.join(os.path.dirname(__file__), f'../assets/{self.orientation}/{self.active_color}_pedestrian.png')

    def load_image(self, rotacion=0):
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

    def get_path_image(self):
        return self.image_path