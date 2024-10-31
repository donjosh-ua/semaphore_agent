import time
from src.agent.model.Agent import Agent
from resources import constants as cons


class MasController:
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MasController, cls).__new__(cls)
            cls.instance.__initialized = False
        return cls.instance

    def __init__(self):
        if not self.__initialized:
            self.change_control = False
            self.__agents = []
            self.__street_agents = []
            self.__pedestrian_agents = []
            self.__initialized = True
            self.__processed_state = set()

    def get_agents(self):
        return self.__agents

    def create_agent(self, type: str, control: bool=False) -> Agent:

        agent = Agent(type, control)
        self.__agents.append(agent)

        if agent.type == "street":
            self.__street_agents.append(agent)
        else:
            self.__pedestrian_agents.append(agent)
        
        return agent
    
    def switch_street_agents_control(self):

        sa1 = self.__street_agents[0]
        sa2 = self.__street_agents[1]

        if sa1.current_state == 5 and sa1.has_control:
            sa1.has_control = False
            sa2.has_control = True
            self.change_control = True

            return 
        
        if sa2.current_state == 5 and sa2.has_control:
            sa2.has_control = False
            sa1.has_control = True
            self.change_control = True

    def switch_pedestrian_agents_control(self):

        pa1 = self.__pedestrian_agents[0]
        pa2 = self.__pedestrian_agents[1]

        if pa1.current_state == 5 and pa1.has_control:
            pa1.has_control = False
            pa2.has_control = True
            self.change_control = True

            return 
        
        if pa2.current_state == 5 and pa2.has_control:
            pa2.has_control = False
            pa1.has_control = True
            self.change_control = True

    def update(self, elapsed_time) -> None:        
        
        states = (2, 4, 6, 8, 10)
        elapsed_time = int(elapsed_time)
    
        if elapsed_time not in states:
            return
        
        if elapsed_time in self.__processed_state:
            return
        
        if elapsed_time == cons.STRAIGHT_RED_TIME:
            self.__processed_state.clear()

        self.__processed_state.add(elapsed_time)
        
        for agent in self.__agents:
            if agent.has_control:
                agent.update_state()

        self.switch_pedestrian_agents_control()
        self.switch_street_agents_control()
