from src.intersection.model.TrafficLight import TrafficLight
from src.agent.model.Agent import Agent
from ..view.MainWindow import MainWindow
import datetime, time

class Controller:

    agent = Agent()
    view = MainWindow()

    def __init__(self):
        Controller.view.ventana.mainloop()

    @staticmethod
    def run():

        tl1 = TrafficLight()
        tl2 = TrafficLight()

        Controller.agent.add_traffic_light(tl1)
        Controller.agent.add_traffic_light(tl2)

        total_seconds = 5

        while True:

            if(total_seconds == 0):
                total_seconds = 5

            timer = datetime.timedelta(seconds = total_seconds)

            print(timer, end="\r")
    
            time.sleep(1)

            total_seconds -= 1

            """Se debe pasar que imagen se desea que se mueva, una velocidad horizontal y una velocidad vertical """
            Controller.view.mover_imagen(Controller.view.semaforo_inferior, 5, 5)
