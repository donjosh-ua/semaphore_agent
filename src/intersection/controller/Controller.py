from ..view.MainWindow import MainWindow
from ..model.TrafficLight import TrafficLight
import time
class Controller:
    view = MainWindow()
    
    """Se debe pasar que imagen se desea que se mueva, una velocidad horizontal y una velocidad vertical """
    view.mover_imagen(view.semaforo_inferior, 5, 5)

    
    """
    view.cambiar_imagen(view.semaforo_inferior, view.semaforo_verde_tk)
    #time.sleep(4)

    view.cambiar_imagen(view.semaforo_inferior, view.semaforo_rojo_tk)
    #time.sleep(4)

    view.cambiar_imagen(view.semaforo_inferior, view.semaforo_amarillo_tk)
    """

    view.ventana.mainloop()

    """
    view.cambiar_imagen(view.semaforo_inferior, view.semaforo_verde_tk)
    #time.sleep(4)

    view.cambiar_imagen(view.semaforo_inferior, view.semaforo_rojo_tk)
    #time.sleep(4)

    view.cambiar_imagen(view.semaforo_inferior, view.semaforo_amarillo_tk)
    
    view.ventana.mainloop()
    """



    semaforo = TrafficLight()
    
    print(semaforo.active_color)
    semaforo.change_color()
    print(semaforo.active_color)
    semaforo.change_color()
    print(semaforo.active_color)
    semaforo.change_color()
    print(semaforo.active_color)

    
    