import pygame
import os

class TrafficLight:

    __colors = ['green', 'yellow', 'red']
 
    def __init__(self, image_size, x=0, y=0):
        self.x = x
        self.y = y
        self.image_size = image_size
        self.active_color = "red"
        self.image_path = os.path.join(os.path.dirname(__file__), f'../assets/{self.active_color}.png')
        #self.image_path = "src/intersection/assets/{self.active_color}.png"
        self.image=self.load_image()
        
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

    def set_image_path(self):
        self.image_path = "src/intersection/assets/{self.active_color}.png"

    def get_path_image(self):
        return self.image_path