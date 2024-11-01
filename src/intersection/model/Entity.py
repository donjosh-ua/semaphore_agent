import pygame
import random
import numpy as np
import math
import time

from resources import constants as cons


class Entity:
    """
    Represents a moving entity in the simulation.
    """
    
    __bus_paths = ["src/intersection/assets/bus_yellow.png",
                   "src/intersection/assets/bus_cyan.png",
                   "src/intersection/assets/bus_purple.png",
                   ]
    
    __person_paths = ["src/intersection/assets/person.png"]

    def __init__(self, type: str, x: int = 0, y: int = 0, x_speed: int = 0, y_speed: int = 0, rotation: int = 0):
        """
        Initializes the entity with the given parameters.
        """
        self.x = x
        self.y = y
        self.type = type
        self.vel_x = x_speed
        self.vel_y = y_speed
        self.rotation = rotation
        self.is_moving = True
        self.is_crossing = False
        self.changed = False
        self.change_direction = None
        self.is_changin = False
        self.__set_image_path(type)
        self.__set_image_size(type)
        self.image = self.__load_image()
        self.rect = self.image.get_rect(center=(x, y))
        
    def __set_image_size(self, type: str) -> None:
        """
        Sets the image size based on the entity type.
        """
        if type == "bus":
            self.image_size = (cons.BUS_LENGTH, cons.BUS_WIDTH)
        else:
            self.image_size = (cons.PERSON_LENGTH, cons.PERSON_WIDTH)

    def __set_image_path(self, type):
        """
        Updates the image path based on the entity type.
        """
        if type == "bus":
            self.image_path = self.__bus_paths[random.randint(0, len(self.__bus_paths) - 1)]
        else:
            self.image_path = self.__person_paths[0]

    def get_image_path(self) -> str:
        """
        Returns the image path of the entity.
        """
        return self.image_path
    
    def move(self):
        """
        Moves the entity and handles boundary collisions.
        """
        
        #if self.change_right:
            #print(f"vx:{self.__move_curve()}, vy:{self.vel_y}")
        #    self.__move_curve()
        
        if self.change_direction != None and not self.is_changin:
            self.__move_curve(self.change_direction)
        
        if self.is_moving or self.is_crossing:
            self.x += self.vel_x
            self.y += self.vel_y
            self.rect.center = (self.x, self.y)
            
            #print(self.rect.center)
            
            
            if self.change_direction == "right" and self.is_changin:
                #print("Entra")
                if abs(self.y - 539) <= 7:
                    print("Finaliza movimiento")
                    self.y = 539
                    self.vel_y = 0
                    self.vel_x = 7
                    self.is_changin = False
                    self.change_direction = None
                    self.changed = True
                    #self.rect.center=(self.x, self.y)
                    self.rotation = 0
                    self.__reset_flags()
                    self.image_size = (cons.BUS_LENGTH, cons.BUS_WIDTH)
                    self.image = self.__load_image()
                    self.rect = self.image.get_rect(center=(self.x, self.y))
            
            if self.change_direction == "left" and self.is_changin:
                #print("Entra")
                if abs(459 -self.x) <= 7:
                    print("Finaliza movimiento")
                    self.x = 459
                    self.vel_y = -7
                    self.vel_x = 0
                    self.is_changin = False
                    self.change_direction = None
                    self.changed = True
                    #self.rect.center=(self.x, self.y)
                    self.rotation = 90
                    self.__reset_flags()
                    self.image_size = (cons.BUS_LENGTH, cons.BUS_WIDTH)
                    self.image = self.__load_image()
                    self.rect = self.image.get_rect(center=(self.x, self.y))
                    
                
                #self.__move_curve(self.change_direction)
                #dt = -9
                
                #a = 4
                #self.vel_x = (261 - a*(dt**2))/dt

                #theta = math.degrees(math.atan((self.y + self.vel_y)/(self.x + self.vel_x)))
                #print(f"El ángulo es: {theta} grados")
                
                
            # Bounce the entity if it hits the screen boundaries
            if self.rect.right >= cons.SCREEN_SIZE[0] or self.rect.left <= 0: 
                #self.vel_x = -self.vel_x
                self.__respaw("HORIZONTAL")
            if self.rect.bottom >= cons.SCREEN_SIZE[1] or self.rect.top <= 0:
                #self.vel_y = -self.vel_y
                self.__respaw("VERTICAL")
                
    
    def __move_curve(self, direction="right"):
        
        if direction == "right":
                
            dt = -9
            a = 4
            self.vel_x = ((261 - a*(dt**2))/dt)*((2)**2)/6
            self.vel_y = (self.vel_y)*((2)**2)/6
            self.is_changin = True
            
            #self.vel_y = 
        if direction == "left":
            dt = -9
            a = 4
            self.vel_y = -((261 - a*(dt**2))/dt)*((2)**2)/14
            self.vel_x = (self.vel_x)*((2)**2)/6
            self.is_changin = True
        
            
            
            
        #theta = math.degrees(math.atan((self.y + self.vel_y)/(self.x + self.vel_x)))
            
        #print(f"El ángulo es: {theta} grados")
            
            
        #return (261 - a*(dt**2))/dt
        
    
    def __respaw(self, posicion):
        self.__reset_flags()
        
        # randomize posicion
        spawnValues = cons.SPAWN_POSICION[posicion][self.type]
        self.rect.center = spawnValues[random.randint(0, 1)]
        self.x, self.y = self.rect.center
        
        
        
        # randomize image
        self.__set_image_path(self.type)
        self.__set_image_size(self.type)
        
        self.image = self.__load_image()
        
        self.ver_atributos()
    
    def __reset_flags(self):
        self.is_moving = True
        self.is_crossing = False
        self.changed = False
        self.change_direction = None
        self.is_changin = False
        
    def ver_atributos(self):
        print("========================================")
        print("x:", self.x)
        print("y:", self.y)
        print("type:", self.type)
        print("vel_x:", self.vel_x)
        print("vel_y:", self.vel_y)
        print("rotation:", self.rotation)
        print("is_moving:", self.is_moving)
        print("is_crossing:", self.is_crossing)
        print("changed:", self.changed)
        print("change_direction:", self.change_direction)
        print("is_changin:", self.is_changin)
        print("image_path:", self.__set_image_path(type))
        print("image_size:", self.__set_image_size(type))
        print("image:", self.image)
        print("rect:", self.rect)
        
    
    def __load_image(self) -> pygame.Surface:
        """
        Loads and transforms the entity's image.
        """
        return pygame.transform.rotate(pygame.transform.scale(pygame.image.load(self.image_path), self.image_size), self.rotation)