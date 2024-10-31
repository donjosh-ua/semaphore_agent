
class Traffic:
    @staticmethod
    def is_same_street(entityCorner, trafficLigthCorner):
        return entityCorner==trafficLigthCorner
        
    @staticmethod
    def __is_near(entityCorner, trafficLigthCorner, velocityEntity):
        if entityCorner < trafficLigthCorner:
            return (entityCorner + velocityEntity) > trafficLigthCorner
        else: 
            return False
        
    @staticmethod
    def __is_before(entityCorner, trafficLigthCorner):
        return (entityCorner - trafficLigthCorner) <= 0
    
    @staticmethod
    def is_influenciable(entityCorner, trafficLigthCorner, velocityEntity):
        return Traffic.__is_near(entityCorner, trafficLigthCorner, velocityEntity) and Traffic.__is_before(entityCorner, trafficLigthCorner)    
