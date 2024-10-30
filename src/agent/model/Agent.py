from src.intersection.model.TrafficLight import TrafficLight


class Agent:

    def __init__(self, type: str, control):
        self.__lights = []
        self.has_control = control
        self.type = type
        self.current_state = 5
        self.set_states_number(type)
        self.set_state_table(type)

    def set_states_number(self, type: str):
        self.states_number = 5 if type == "street" else 3

    def set_state_table(self, type: str):
        if type == "street":
            self.states_table = {1: ("green", "green"),
                                 2: ("green", "yellow"),
                                 3: ("green", "red"),
                                 4: ("yellow", "red"),
                                 5: ("red", "red")}
        else:
            self.states_table = {1: ("red", "red"),
                                 2: ("red", "green"),
                                 3: ("green", "green")}

    def add_light(self, light: TrafficLight):
        self.__lights.append(light)

    def get_lights(self):
        return self.__lights

    def update_state(self):

        self.current_state = self.current_state + 1 if self.current_state < self.states_number else 1
        
        if self.type == "street":
            self.__lights[1].set_active_color(self.states_table.get(self.current_state)[0])
            self.__lights[0].set_active_color(self.states_table.get(self.current_state)[1])
        else:
            self.__lights[0].set_active_color(self.states_table[self.current_state][0])
            self.__lights[1].set_active_color(self.states_table[self.current_state][1])
            self.__lights[2].set_active_color(self.states_table[self.current_state][0])
            self.__lights[3].set_active_color(self.states_table[self.current_state][1])

    