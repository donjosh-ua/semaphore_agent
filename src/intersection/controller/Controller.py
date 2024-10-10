from src.intersection.model.TrafficLight import TrafficLight
from src.agent.model.Agent import Agent
from ..view.MainWindow import MainWindow
import resources.constants as const
import time


class Controller:

    agent = Agent()
    view = MainWindow()

    def __init__(self):
        Controller.view.ventana.mainloop()

    def change_color(self, imagen_semaforo, semaforo:TrafficLight, rotacion=0):

        #* Cambia el valor de la variable active_color
        # semaforo.change_color()

        #* Cambia la imagen según el valor que se encuentra en el atributo active_color
        self.view.cambiar_imagen(imagen_semaforo, semaforo.active_color, rotacion)

    @staticmethod
    def run():

        tl_ver = TrafficLight()
        tl_hor = TrafficLight()

        Controller.agent.set_traffic_lights(tl_ver, tl_hor)
        tl_hor.change_color()
        total_seconds = 0

        while True:

            if(total_seconds >= const.RED_TIME):
                total_seconds = 0

            # Falta programar los movimientos del bus nada mas

            if Controller.agent.update_state(total_seconds):
                Controller.change_color(Controller, Controller.view.semaforo_inferior, tl_ver, 0)
                Controller.change_color(Controller, Controller.view.semaforo_izquierdo, tl_hor, 90)

            time.sleep(const.FRAME_TIME)
            total_seconds += const.FRAME_TIME
