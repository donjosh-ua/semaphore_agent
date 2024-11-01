
class Traffic:
    @staticmethod
    def is_same_street(entityCorner, trafficLigthCorner):
        return entityCorner==trafficLigthCorner
        
    @staticmethod
    def __is_near(entityCorner, trafficLigthCorner, velocityEntity):
        print("Is near?,", entityCorner + velocityEntity, trafficLigthCorner)
        if entityCorner < trafficLigthCorner:
            return (entityCorner + velocityEntity) > trafficLigthCorner
        else: 
            return False
        
    @staticmethod
    def __is_before(entityCorner, trafficLigthCorner):
        print("Is before?,", entityCorner - trafficLigthCorner)
        return (entityCorner - trafficLigthCorner) <= 0
    
    @staticmethod
    def is_influenciable(entityCorner, trafficLigthCorner, velocityEntity):
        #entity.is_moving = not (Traffic.__is_near(entityCorner, trafficLigthCorner, velocityEntity) and Traffic.__is_before(entityCorner, trafficLigthCorner))
        #print("Antes del return:", entity.is_moving)
        return Traffic.__is_near(entityCorner, trafficLigthCorner, velocityEntity) and Traffic.__is_before(entityCorner, trafficLigthCorner)    
    
    @staticmethod
    def is_crossing(entity, entityCorner, trafficLigthCorner, trafficLigthReference = None, coordenate="x"):
        
        if trafficLigthCorner < entityCorner:
            entity.is_crossing = True
            print(trafficLigthCorner, entityCorner, sep='semaforo,entidad')
            if (not entity.changed) and trafficLigthReference != None:
                if abs(trafficLigthReference) == 539:
                    entity.change_direction = "right"
                    
                if abs(trafficLigthReference) == 459:
                    entity.change_direction = "left"
                
        
        print("Change right?:", entity.change_direction)
    
    @staticmethod
    def near_entity_trafficLight(trafficLights:list, entity, coordenate="x"):
        distances = dict()
        if coordenate == "x":
            for trafficLight in trafficLights:
                #print("Coordenadas semáforo:", trafficLight.rect.center)
                #print("Coordenadas entidad:", entity.rect.center)
                if Traffic.is_same_street(trafficLight.y, entity.y):
                    distances[abs(trafficLight.x - entity.x)] = trafficLight
                
        if coordenate == "y":
            for trafficLight in trafficLights:
                #print("Coordenadas semáforo:", trafficLight.rect.center)
                #print("Coordenadas entidad:", entity.rect.center)
                if Traffic.is_same_street(trafficLight.x, entity.x):
                    distances[abs(trafficLight.y - entity.y)] = trafficLight
        if not distances:
            return None
        
        return distances[min(distances.keys())]