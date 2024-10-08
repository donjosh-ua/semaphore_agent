from ..view.MainWindow import MainWindow

class Controller:
    view = MainWindow()

    """Se debe pasar que imagen se desea que se mueva, una velocidad horizontal y una velocidad vertical """
    view.mover_imagen(view.semaforo_inferior, 5, 5)

    view.ventana.mainloop()
