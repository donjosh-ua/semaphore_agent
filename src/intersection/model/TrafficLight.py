class TrafficLight:

    __colors = ['green', 'yellow', 'red']
 
    def __init__(self):
        self.active_color = "red"
        self.image_path = "src/intersection/assets/{self.active_color}.png"

    def set_active_color(self, color):
        self.active_color = color

    def change_color(self):
        try:
            self.active_color = self.__colors[self.__colors.index(self.active_color) + 1]
        except Exception as e:
            self.active_color = self.__colors[0]
        self.set_active_color(self.active_color)

    def __set_image_path(self, color):
        self.image_path = "src/intersection/assets/{self.active_color}.png"

    def get_path_image(self):
        return self.image_path;