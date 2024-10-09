from src.agent.model.Agent import Agent


class AgentController:
    
    agent = Agent()

    def __init__(self):
        pass

    def update_lights(self):
        
        self.agent.update()
