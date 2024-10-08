class Agent:
    
    def __init__(self):
        self.traffic_lights = []

    def add_traffic_light(self, traffic_light):
        self.traffic_lights.append(traffic_light)

    def update(self):
        for tl in self.traffic_lights:
            if tl.active_color == "green":
                tl.set_active_color("red")
            else:
                tl.set_active_color("green")