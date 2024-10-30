from src.agent.model.Agent import Agent


class MasController:
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MasController, cls).__new__(cls)
            cls.instance.__initialized = False
        return cls.instance

    def __init__(self):
        if not self.__initialized:
            self.__agents = []
            self.__street_agents = []
            self.__initialized = True

    def get_agents(self):
        return self.__agents

    def create_agent(self, type: str, control: bool=False) -> Agent:

        agent = Agent(type, control)
        self.__agents.append(agent)

        if agent.type == "street":
            self.__street_agents.append(agent)
        
        return agent

    def update(self) -> None:        
          
        for agent in self.__agents:
            if agent.has_control and agent.type == "street":
                agent.update_state()

        sa1 = self.__street_agents[0]
        sa2 = self.__street_agents[1]

        if sa1.current_state == 5 and sa1.has_control:
            sa1.has_control = False
            sa2.has_control = True
            return
        
        if sa2.current_state == 5 and sa2.has_control:
            sa2.has_control = False
            sa1.has_control = True
