import pygame
import os

from src.intersection.model.Entity import Entity
from src.intersection.view.MainWindow import ImageView
from src.intersection.model.TrafficLight import TrafficLight
from src.intersection.controller.StreetController import StreetController
from resources import constants as cons


def main():

    clock = pygame.time.Clock()

    vertical_spawn_points = [(20, 459), (20, 539)]
    horizontal_spawn_points = [(459, 980), (539, 980)]

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

    bus_list = []
    bus_list.append(Entity("bus", x=60, y=539))
    bus_list.append(Entity("bus", x=60, y=459))
    bus_list.append(Entity("bus", x=459, y=940, rotation=90))
    bus_list.append(Entity("bus", x=539, y=940, rotation=90))

    views = [ImageView(light) for light in vertical_lights]
    views += [ImageView(light) for light in horizontal_lights]
    views += [ImageView(bus) for bus in bus_list]

    controller = StreetController()

    while True:

        controller.handle_events()
        controller.update()
        controller.check_and_stop_near_to_trafficLigth
        controller.change_color_trafficLight()
        screen.blit(background_image, [0, 0])

        for view in views:  
            view.draw(screen)
            
        pygame.display.flip()
        clock.tick(cons.FRAME_RATE)

if __name__ == '__main__':

    pygame.init()
    screen = pygame.display.set_mode(cons.SCREEN_SIZE)
    pygame.display.set_caption("Control de semáforos")
    path_fondo = os.path.join(os.path.dirname(__file__), "src/intersection/assets/background.png")

    background_image = pygame.transform.scale(pygame.image.load(path_fondo).convert(), cons.SCREEN_SIZE)

    main()
