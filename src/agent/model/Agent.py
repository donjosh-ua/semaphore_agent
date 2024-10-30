import resources.constants as cons


class Agent:

    def __init__(self):
        self.__lights = []
        self.has_control = False
        self.states_table = {1: ("green", "green"),
                             2: ("green", "yellow"),
                             3: ("green", "red"),
                             4: ("yellow", "red"),
                             5: ("red", "red")}

    def add_light(self, light):
        self.__lights.append(light)

    def get_lights(self):
        return self.__lights

    def update_state(self):

        changed = False

        return changed
    