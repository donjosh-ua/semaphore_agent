import pygame
import os

from src.intersection.model.Entity import Entity
from src.intersection.view.MainWindow import ImageView
from src.intersection.model.TrafficLight import TrafficLight
from src.intersection.controller.Controller import StreetController


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

def main():

    clock = pygame.time.Clock()

    # vertical_spawn_points = [(20, 459), (20, 539)]
    # horizontal_spawn_points = [(459, 20), (539, 20)]

    vertical_lights = []
    vertical_lights.append(TrafficLight("vertical", "street", x=345, y=459))
    vertical_lights.append(TrafficLight("vertical", "street", x=345, y=539))
   
    vertical_lights.append(TrafficLight("vertical", "pedestrian", x=420, y=619))
    vertical_lights.append(TrafficLight("vertical", "pedestrian", x=582, y=619))
    vertical_lights.append(TrafficLight("vertical", "pedestrian", x=420, y=380))
    vertical_lights.append(TrafficLight("vertical", "pedestrian", x=582, y=380))

    horizontal_lights = []
    horizontal_lights.append(TrafficLight("horizontal", "street", x=459, y=655))
    horizontal_lights.append(TrafficLight("horizontal", "street", x=539, y=655))

    vertical_lights.append(TrafficLight("horizontal", "pedestrian", x=380, y=580))
    vertical_lights.append(TrafficLight("horizontal", "pedestrian", x=619, y=580))
    vertical_lights.append(TrafficLight("horizontal", "pedestrian", x=380, y=420))
    vertical_lights.append(TrafficLight("horizontal", "pedestrian", x=619, y=420))

    views = [ImageView(traffic_light) for traffic_light in vertical_lights]
    views += [ImageView(traffic_light) for traffic_light in horizontal_lights]

    controller = StreetController()
    running = True

    while running:

        controller.handle_events()
        controller.update()
        controller.check_and_stop_near_to_trafficLigth
        controller.change_color_trafficLight()
        screen.blit(background_image, [0, 0])

        for view in views:  
            view.draw(screen)
            
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Sistemas Multiagentes')
    path_fondo = os.path.join(os.path.dirname(__file__), 'src/intersection/assets/background.png')

    background_image = pygame.transform.scale(pygame.image.load(path_fondo).convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))

    main()
