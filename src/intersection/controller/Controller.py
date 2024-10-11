from src.intersection.model.TrafficLight import TrafficLight
from src.agent.model.Agent import Agent
from src.intersection.model.Traffic import Traffic
from ..view.MainWindow import MainWindow
import resources.constants as const
import time


class Controller:

    agent = Agent()
    view = MainWindow()

    def __init__(self):
        Controller.view.ventana.mainloop()

    def change_color(self, imagen_semaforo, semaforo:TrafficLight, rotacion=0):
        self.view.cambiar_imagen(imagen_semaforo, semaforo.active_color, rotacion)
    
    #def are_close(self, coordenadas_bus, coordenadas_semafora):


    def move_entity(self, imagen_entidad, dx, dy):
        self.view.mover_imagen(imagen_entidad, dx, dy)

    @staticmethod
    def run():

        vx_bus_amarillo = 10
        vx_bus_gris = 10
        vx_bus_morado = 10

        vy_bus_amarillo = 10
        vy_bus_gris = 10
        vy_bus_morado = 10

        traffic = Traffic()

        tl_ver = TrafficLight()
        tl_hor = TrafficLight()

        Controller.agent.set_traffic_lights(tl_ver, tl_hor)
        tl_hor.change_color()
        total_seconds = 0

        while True:

            if(total_seconds >= const.RED_TIME):
                total_seconds = 0

            pos_bus_amarillo_0 = Controller.view.get_posicion_image(Controller.view.bus_amarillo_0)
            pos_bus_gris_0 = Controller.view.get_posicion_image(Controller.view.bus_gris_0)
            pos_bus_morado_0 = Controller.view.get_posicion_image(Controller.view.bus_morado_0)
            
            pos_bus_amarillo_270 = Controller.view.get_posicion_image(Controller.view.bus_amarillo_270)
            pos_bus_gris_270 = Controller.view.get_posicion_image(Controller.view.bus_gris_270)
            pos_bus_morado_270 = Controller.view.get_posicion_image(Controller.view.bus_morado_270)

            posicion_semaforo_izquierdo = Controller.view.get_posicion_image(Controller.view.semaforo_izquierdo)
            posicion_semaforo_inferior = Controller.view.get_posicion_image(Controller.view.semaforo_inferior)


            #print("Posición morado:", pos_bus_amarillo_0)
            #print("Posición amarillo:", pos_bus_amarillo_0)
            #print("Posición gris:", posicion_bus_gris)

            #print("Posición semafor:", posicion_semaforo_izquierdo)

            #print("move morado:", traffic.can_move(posicion_bus_morado[0] + 180, posicion_semaforo_izquierdo[0], v_bus_amarillo))
            #print("move amarillo:", traffic.can_move(pos_bus_amarillo_0[0] + Controller.view.size_bus[0]/2, posicion_semaforo_izquierdo[0], vx_bus_amarillo))
            #print("move gris:", traffic.can_move(posicion_bus_gris[0] + 180, posicion_semaforo_izquierdo[0], v_bus_amarillo))

            #! Buses horazontales
            #* Movimiento del bus amarillo
            if traffic.can_move(pos_bus_amarillo_0[0] + Controller.view.size_bus[0]/2, posicion_semaforo_izquierdo[0], vx_bus_amarillo) and tl_hor.active_color != "green":
                pass
            else:
                Controller.move_entity(Controller, Controller.view.bus_amarillo_0, vx_bus_amarillo, 0)

            #* Movimiento del bus morado
            if traffic.can_move(pos_bus_morado_0[0] + Controller.view.size_bus[0]/2, posicion_semaforo_izquierdo[0], vx_bus_morado) and tl_hor.active_color != "green":
                pass
            else:
                #Controller.move_entity(Controller, Controller.view.bus_morado_0, vx_bus_morado, 0)
                pass

             #* Movimiento del bus gris
            if traffic.can_move(pos_bus_gris_0[0] + Controller.view.size_bus[0]/2, posicion_semaforo_izquierdo[0], vx_bus_gris) and tl_hor.active_color != "green":
                pass
            else:
                #Controller.move_entity(Controller, Controller.view.bus_gris_0, vx_bus_gris, 0)
                pass

            
            #! Buses verticales
            #* Movimiento del bus amarillo
            if traffic.can_move(-(pos_bus_amarillo_270[1] - Controller.view.size_bus[0]/2), -posicion_semaforo_inferior[1], vy_bus_amarillo) and tl_ver.active_color != "green":
                pass
            else:
                Controller.move_entity(Controller, Controller.view.bus_amarillo_270, 0, -vy_bus_amarillo)
                pass

            #* Movimiento del bus morado
            if traffic.can_move(-(pos_bus_morado_270[1] - Controller.view.size_bus[0]/2), -posicion_semaforo_inferior[1], vy_bus_morado) and tl_ver.active_color != "green":
                pass
            else:
                #Controller.move_entity(Controller, Controller.view.bus_morado_270, 0, -vy_bus_morado)
                pass

             #* Movimiento del bus gris
            if traffic.can_move(-(pos_bus_gris_270[1] - Controller.view.size_bus[0]/2), -posicion_semaforo_inferior[1], vy_bus_gris) and tl_ver.active_color != "green":
                pass
            else:
                #Controller.move_entity(Controller, Controller.view.bus_gris_270, 0, -vy_bus_gris)
                pass

            if Controller.agent.update_state(total_seconds):
                Controller.change_color(Controller, Controller.view.semaforo_inferior, tl_ver, 0)
                Controller.change_color(Controller, Controller.view.semaforo_izquierdo, tl_hor, 90)

            time.sleep(const.FRAME_TIME)
            total_seconds += const.FRAME_TIME
