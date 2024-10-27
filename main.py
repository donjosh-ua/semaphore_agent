#from src.intersection.controller.Controller import ImageController
#import threading    
#from semaphore_agent.src.intersection.view.ImageView import ImageView
from src.intersection.model import TrafficLight, Traffic, Entity
from src.intersection.controller.Controller import StreetController
from src.intersection.view.MainWindow import ImageView

import pygame


import pygame
from src.intersection.model.Entity import Entity
from src.intersection.model.TrafficLight import TrafficLight
#from semaphore_agent.src.intersection.view.ImageView import ImageView
from src.intersection.controller.Controller import StreetController

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (255, 255, 255)

# Initialization of Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('MVC Pygame Example')

def main():
    clock = pygame.time.Clock()
    cars = [Entity(image_size=(100, 100), x=200, y=200, vel_x=10, vel_y=10) for _ in range(2)]  # Create multiple images
    #people = [Entity(type="person") for _ in range(BALL_COUNT)]  # Create multiple images
    
    trafficLights = [TrafficLight(image_size=(45, 90), x=200, y=200,), TrafficLight(image_size=(45, 90), x=100, y=300)]  # Create multiple images
    
    images = cars #+ people
    
    views = [ImageView(image) for image in images]  # Create a view for each image
    
    print("Views:",views)
    controller = StreetController()
    
    for entity in images:
        controller.add_entity(entity, trafficLights[0])
    
    # Instantiate the color-changing square
    #color_changing_square = ColorChangingSquare()

    running = True
    #screen.fill(BACKGROUND_COLOR)
    while running:
        screen.fill(BACKGROUND_COLOR)
        controller.handle_events()
        controller.update()
        controller.check_and_stop_near_to_trafficLigth  # Check if any images should be stopped
        controller.change_color_trafficLight()

        # Draw each image
        #print("Hola xd")
        for view in views:
            view.draw(screen)
            
        pygame.display.flip()
        clock.tick(60)  # Maintain 60 FPS

if __name__ == '__main__':
    main()

    

    

    