from src.intersection.model.TrafficLight import TrafficLight
from src.agent.model.Agent import Agent
from ..view.MainWindow import MainWindow
import datetime, time

class Controller:

    agent = Agent()
    view = MainWindow()

    def __init__(self):
        Controller.view.ventana.mainloop()

    def change_color(self, imagen_semaforo, semaforo:TrafficLight):

        #* Cambia el valor de la variable active_color
        semaforo.change_color()

        #* Cambia la imagen según el valor que se encuentra en el atributo active_color
        self.view.cambiar_imagen(imagen_semaforo, semaforo.active_color)

    @staticmethod
    def run():

        tl1 = TrafficLight()
        tl2 = TrafficLight()

        Controller.agent.add_traffic_light(tl1)
        Controller.agent.add_traffic_light(tl2)

        Controller.view.mover_imagen(Controller.view.semaforo_inferior, 5, 5)

        for i in range(0, 10):
            Controller.change_color(self=Controller, imagen_semaforo=Controller.view.semaforo_inferior, semaforo=tl1)
            time.sleep(1)
