import pygame
import sys

class StreetController:

    def __init__(self):
        #ImageController.view.iniciar_ventana()
        self.entitys = list()
        self.trafficLights_entitys = dict()
    
    def add_entity(self, entity, trafficLigth):
        #agrega las entidades según el semáforo con el cual va a interactuar.
        if trafficLigth not in self.trafficLights_entitys.keys():
            self.trafficLights_entitys[trafficLigth] = [entity]
        else:
            self.trafficLights_entitys[trafficLigth].append(entity)
        
        self.entitys.append(entity)
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
    def update(self):
        #print("movimiento ")
        #print(self.entitys)
        for model in self.entitys:
            #print(f"mover {str(model)}")
            model.move()
            
    def check_and_stop_near_to_trafficLigth(self):
        for trafficLight in self.trafficLights_entitys.keys():
            for entity in self.trafficLights_entitys[trafficLight]:
                #if Traffic().can_move(entity, trafficLight)
                if self.distance(trafficLight, entity) <= 10 and trafficLight.active_color == "red":
                    print("La distancia es menor y debe frenar")
                    entity.is_moving = False
                    #pass
                else:
                    entity.is_moving = True
        
    def distance(self, trafficLight, entity):
        return 0
    
    def change_color_trafficLight(self):
        pass
        #print("Cambia el color de los semáforos")