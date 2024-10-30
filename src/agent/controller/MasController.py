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
            self.__initialized = True

    def get_agents(self):
        return self.__agents

    def create_agent(self) -> Agent:

        agent = Agent()
        self.__agents.append(agent)
        
        return agent

    def update(self, time):
        for agent in self.agents:
            agent.update_state(time)