import resources.constants as const


class Agent:

    green_duration = const.GREEN_TIME  # seconds
    orange_duration = const.YELLOW_TIME  # seconds
 
    def __init__(self):
        self.vertical_light = None
        self.horizontal_light = None

    def set_traffic_lights(self, vertical, horizontal):
        self.vertical_light = vertical
        self.horizontal_light = horizontal

    def update_state(self, time):

        time = round(time, 1)
        changed = False

        if time == 0 and self.vertical_light.active_color == 'red':
            self.vertical_light.active_color = 'green'
            self.horizontal_light.active_color = 'red'
            return True
        
        if time == 0 and self.horizontal_light.active_color == 'yellow':
            self.horizontal_light.active_color = 'red'
            changed = True
        
        if time == 0 and self.vertical_light.active_color == 'yellow':
            self.vertical_light.active_color = 'red'
            changed = True
        
        if time == self.green_duration and self.vertical_light.active_color == 'green':
            self.vertical_light.active_color = 'yellow'
            changed = True
        
        if time == self.green_duration and self.horizontal_light.active_color == 'green':
            self.horizontal_light.active_color = 'yellow'
            changed = True
        
        if time == 0 and self.horizontal_light.active_color == 'red':
            self.vertical_light.active_color = 'red'
            self.horizontal_light.active_color = 'green'
            return True
        
        return changed

