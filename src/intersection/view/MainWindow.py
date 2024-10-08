
import tkinter as tk
from PIL import Image, ImageTk

"""
Valores de referencia
#! Tamaño de los semáforos: 45, 90
#! Tamaño del fondo: 1348, 793 -> 800x800
#! Tamano de los buses: 500, 226 -> 180, 81
#! Posición del semáforo inferior: 720, 450
#! Posición del semáforo izquierdo: 0, 0
"""

class MainWindow:
    #* path de las imágenes
    path_fondo = "src/intersection/assets/fondo.png"
    path_sem_rojo = "src/intersection/assets/rojo.png"
    path_sem_verde = "src/intersection/assets/verde.png"
    path_sem_amarillo = "src/intersection/assets/amarillo.png"
    path_bus_amarillo = "src/intersection/assets/bus_amarillo.png"
    path_bus_morado = "src/intersection/assets/bus_morado.png"
    path_bus_gris = "src/intersection/assets/bus_gris.png"

    #* size de las imágenes
    size_fondo = (800, 800)
    size_sem = (45, 90)
    size_ventana = (800, 800)
    size_bus = (180, 81)

    #* posición inicial de las imágenes
    p0_sem_inferior = (720, 450)
    p0_sem_izquierda = (0, 0)
    pos_bus_amarillo = (0, 100)
    pos_bus_morado = (100, 100)
    pos_bus_gris = (100, 200)

    def cargar_imagen(path, size):
        imagen = Image.open(path)
        imagen = imagen.resize(size)
        return ImageTk.PhotoImage(imagen)
        
    #TODO: Crear ventanas y lienzos
    #* Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Sistemas Multiagentes")
    ventana.geometry(f"{size_ventana[0]}x{size_ventana[1]}")

    #* Crear el lienzo (Canvas)
    canvas = tk.Canvas(ventana, width=size_ventana[0], height=size_ventana[1])
    canvas.pack()

    #TODO: Cargar las imágenes
    #* Imagen del fondo
    fondo_tk = cargar_imagen(path_fondo, size_fondo)

    #* Imagen del semaforo_rojo
    semaforo_rojo_tk = cargar_imagen(path_sem_rojo, size_sem)

    #* Imagen del semaforo_amarillo
    semaforo_amarillo_tk = cargar_imagen(path_sem_amarillo, size_sem)

    #* Imagen del semaforo_verde
    semaforo_verde_tk = cargar_imagen(path_sem_verde, size_sem)

    #* Imagen del bus_amarillo
    bus_amarillo_tk = cargar_imagen(path_bus_amarillo, size_bus)

    #* Imagen del bus_verde
    bus_morado_tk = cargar_imagen(path_bus_morado, size_bus)

    #* Imagen del bus_rojo
    bus_gris_tk = cargar_imagen(path_bus_gris, size_bus)

    #TODO: Mostrar imágenes
    #* Mostrar la imagen de fondo, usa como referencia el origen
    canvas.create_image(0, 0, anchor="nw", image=fondo_tk)

    #* Mostrar semáforos
    semaforo_inferior = canvas.create_image(p0_sem_inferior[0], p0_sem_inferior[1], anchor="nw", image=semaforo_rojo_tk)
    semaforo_izquierdo = canvas.create_image(p0_sem_izquierda[0], p0_sem_izquierda[1], anchor="nw", image=semaforo_verde_tk)

    #* Mostrar buses
    bus_amarillo = canvas.create_image(pos_bus_amarillo[0], pos_bus_amarillo[1], anchor="nw", image=bus_amarillo_tk)
    bus_morado = canvas.create_image(pos_bus_morado[0], pos_bus_morado[1], anchor="nw", image=bus_morado_tk)
    bus_gris = canvas.create_image(pos_bus_gris[0], pos_bus_gris[1], anchor="nw", image=bus_gris_tk)

    #TODO: Funciones de movimiento de las imágenes
    def mover_imagen(self, imagen, dx, dy):

        # Obtener las coordenadas actuales de la imagen
        x1, y1, x2, y2 = self.canvas.bbox(imagen)

        """Esta parte es lo que hace que funcione como salva pantallas, es decir que rebote"""
        # Verificar los límites de la ventana (rebote)
        if x2 >= self.size_ventana[0] or x1 <= 0:
            dx = -dx # Cambiar la dirección en el eje x
        if y2 >= self.size_ventana[1] or y1 <= 0:
            dy = -dy # Cambiar la dirección en el eje y

        # Mover la imagen
        self.canvas.move(imagen, dx, dy)

        # Llamar a la función nuevamente después de 100 ms
        self.ventana.after(100, self.mover_imagen, imagen, dx, dy)

    # Funciones para mover la imagen y luego cambiarla
    def mover_arriba(self, event):
        self.canvas.move(self.semaforo_inferior, 0, -10)
        self.cambiar_imagen()

    def mover_abajo(self, event):
        self.canvas.move(self.semaforo_inferior, 0, 10)
        self.cambiar_imagen()

    def mover_izquierda(self, event):
        self.canvas.move(self.semaforo_inferior, -10, 0)
        self.cambiar_imagen()

    def mover_derecha(self, event):
        self.canvas.move(self.semaforo_inferior, 10, 0)
        self.cambiar_imagen()

    # Función para cambiar la imagen
    def cambiar_imagen(self):
        self.canvas.itemconfig(self.semaforo_inferior, image=self.semaforo_verde_tk)
        pass
    # Vincular las teclas de flechas con las funciones de movimiento
    ventana.bind("<Up>", mover_arriba)
    ventana.bind("<Down>", mover_abajo)
    ventana.bind("<Left>", mover_izquierda)
    ventana.bind("<Right>", mover_derecha)

    # Iniciar el bucle principal
    #ventana.mainloop()