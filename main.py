from src.intersection.controller.Controller import Controller
import threading
from src.intersection.view.MainWindow import MainWindow


"""
El proyecto está basado en mvc (que es lo más fácil), pero separado en módulos
con vertical slicing. Cada slice es un módulo que contiene los tres componentes de mvc.
"""

def threadmain():
    Controller.run()


if __name__ == '__main__':
    thread = threading.Thread(target=threadmain,)
    thread.start()
    Controller()
    