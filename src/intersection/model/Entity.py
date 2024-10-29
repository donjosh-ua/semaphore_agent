
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

import pygame

import os

# Construir la ruta correcta a la imagen

class Entity:
    
    __paths = { 
               "person": "src/intersection/person.png",
               "bus_gris":"src/intersection/bus_gris.png",
               "bus_celeste":"src/intersection/bus_celeste.png",
               "bus_morado":"src/intersection/bus_morado.png",
    }

    def __init__(self, type=None, speed=0, x=0, y=0, vel_x=0, vel_y=0, image_path="", image_size=(180, 81)):
        
        self.speed = speed
        self.x = x 
        self.y = y 
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.image_path = image_path
        self.image_size = image_size
        self.type = self.set_type(type)
        self.image = self.load_image()
        self.rect = self.image.get_rect(center=(self.x, self.y))  # centro de la i
        self.is_moving = True
        
    def set_type(self, new_type):
        #* Como cambia el tipo también cambia el asset
        if new_type != None:
            self.set_image_path()
        else:
            self.image_path = os.path.join(os.path.dirname(__file__), '../assets/default.png')
            
        return new_type

    def set_image_path(self):
        self.image_path = self.__paths[self.type]
    
    def move(self):
        self.x += self.vel_x
        self.y += self.vel_y
        self.rect.center = (self.x, self.y)
        #print(f"{self}: {self.x}, {self.y}")
        #print("Has llegado al tope rey")

        # Bounce the ball if it hits the screen boundaries
        if self.rect.right >= SCREEN_WIDTH or self.rect.left <= 0:
            self.vel_x = -self.vel_x
        if self.rect.bottom >= SCREEN_HEIGHT or self.rect.top <= 0:
            self.vel_y = -self.vel_y
            
    def load_image(self, rotacion=0):
        # print("Path a cargar:", self.image_path)
        return pygame.transform.rotate( #* rota la imagen
                    pygame.transform.scale( #* redimensiona la imagen
                        pygame.image.load(self.image_path), self.image_size),  #* carga la imagen
                rotacion)