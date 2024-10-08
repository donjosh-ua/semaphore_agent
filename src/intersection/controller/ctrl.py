from ..view.ventana import Ventana

class Controlador:
    view = Ventana()

    """Se debe pasar que imagen se desea que se mueva, una velocidad horizontal y una velocidad vertical """
    view.mover_imagen(view.semaforo_inferior, 5, 5)

    view.ventana.mainloop()
