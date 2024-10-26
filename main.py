from src.intersection.controller.Controller import Controller
import threading    
from src.intersection.view.MainWindow import MainWindow


def threadmain():
    Controller.run()

if __name__ == '__main__':
    
    thread = threading.Thread(target=threadmain,)
    thread.start()
    
    Controller()
    