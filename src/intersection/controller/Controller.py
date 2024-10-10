from src.intersection.model.TrafficLight import TrafficLight
from src.agent.model.Agent import Agent
from ..view.MainWindow import MainWindow
import datetime, time

class Controller:

    agent = Agent()
    view = MainWindow()

    def __init__(self):
        Controller.view.ventana.mainloop()

    def change_color(self, imagen_semaforo, semaforo:TrafficLight, rotacion=0):

        #* Cambia el valor de la variable active_color
        semaforo.change_color()

        #* Cambia la imagen según el valor que se encuentra en el atributo active_color
        self.view.cambiar_imagen(imagen_semaforo, semaforo.active_color, rotacion)

    @staticmethod
    def run():

        tl1 = TrafficLight()
        tl2 = TrafficLight()

        Controller.agent.add_traffic_light(tl1)
        Controller.agent.add_traffic_light(tl2)
        
        tl2.change_color()
        total_seconds = 0
        while True:

            if(total_seconds == 21):
                total_seconds = 0

            timer = datetime.timedelta(seconds = total_seconds)

            if tl2.active_color == "green": # movimiento de los buses según los semáforos
                Controller.view.mover_imagen(Controller.view.bus_amarillo, 100, 0)

            if total_seconds % 3 == 0: # el cambio se hace cada 7 segundos
                Controller.change_color(self=Controller, imagen_semaforo=Controller.view.semaforo_inferior, semaforo=tl1)
                Controller.change_color(self=Controller, imagen_semaforo=Controller.view.semaforo_izquierdo, semaforo=tl2, rotacion=90)
            
        

            print(timer, end="\r")
            time.sleep(1)
            total_seconds += 1
