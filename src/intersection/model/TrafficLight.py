class TrafficLight:

    __colors = ['red', 'yellow', 'green']

    def __init__(self):
        self.active_color = None

    def set_active_color(self, color):
        self.active_color = color