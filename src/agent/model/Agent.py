class Agent:
    
    traffic_lights = []

    def add_traffic_light(self, traffic_light):
        self.traffic_lights.append(traffic_light)

    @classmethod
    def update(cls):
        for tl in cls.traffic_lights:
            print(tl.active_color)
 
    