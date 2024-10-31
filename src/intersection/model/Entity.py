import pygame
import random
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
        self.x += self.vel_x
        self.y += self.vel_y
        self.rect.center = (self.x, self.y)

        #print(self.rect.center, self.rect.right, self.rect.left, sep= "|")
        # Bounce the entity if it hits the screen boundaries
        if self.rect.right >= cons.SCREEN_SIZE[0] or self.rect.left <= 0: 
            self.vel_x = -self.vel_x
            self.__respaw("HORIZONTAL")
        if self.rect.bottom >= cons.SCREEN_SIZE[1] or self.rect.top <= 0:
            self.vel_y = -self.vel_y
            self.__respaw("VERTICAL")
    
    def __respaw(self, posicion):
        #if posicion == "HORIZONTAL":
        spawnValues = cons.SPAWN_POSICION[posicion][self.type]
        print(spawnValues)
        #center = cons.HORIZONTAL_SPAWN_BUS[random.randint(0, 1)]
        #print(center)
        #self.image.get_rect(center=cons.HORIZONTAL_SPAWN_BUS[random.randint(0, 1)])
        pass
    
    def __load_image(self, rotation: int = 0) -> pygame.Surface:
        """
        Loads and transforms the entity's image.
        """
        return pygame.transform.rotate(pygame.transform.scale(pygame.image.load(self.image_path), self.image_size), self.rotation)