class TrafficLight:

    __colors = ['green', 'yellow', 'red']
    #color = __colors[0]
 
    def __init__(self):
        self.active_color = self.__colors[0]

    def set_active_color(self, color):
        self.active_color = color

    def change_color(self):
        try:
            self.active_color = self.__colors[self.__colors.index(self.active_color) + 1]
        except Exception as e:
            #print(e)
            self.active_color = self.__colors[0]

    def get_path_image(self):
        return f"src/intersection/assets/{self.active_color}.png"