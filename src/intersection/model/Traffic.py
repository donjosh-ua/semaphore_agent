
class Traffic:

    def is_near(self, entity_xy, trafficLigth_xy, velocity_entity_dxy):
        return (entity_xy + velocity_entity_dxy) > trafficLigth_xy

    def is_before(self, entity_xy, trafficLigth_xy):
        return (entity_xy - trafficLigth_xy) <= 0

    def can_move(self, entity_xy, trafficLigth_xy, velocity_entity_dxy):
        return self.is_near(entity_xy, trafficLigth_xy, velocity_entity_dxy) and self.is_before(entity_xy, trafficLigth_xy)
    