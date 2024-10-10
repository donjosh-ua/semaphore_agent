
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
    path_sem_rojo = "src/intersection/assets/red.png"
    path_sem_verde = "src/intersection/assets/green.png"
    path_sem_amarillo = "src/intersection/assets/yellow.png"
    path_bus_amarillo = "src/intersection/assets/bus_amarillo.png"
    path_bus_morado = "src/intersection/assets/bus_morado.png"
    path_bus_gris = "src/intersection/assets/bus_gris.png"

    #* size de las imágenes
    size_fondo = (800, 800)
    size_sem = (45, 90)
    size_ventana = (800, 800)
    size_bus = (180, 81)

    #* posición inicial de las imágenes
    p0_sem_inferior = (416, 438)
    p0_sem_izquierda = (260, 330)
    pos_bus_amarillo = (34, 341)
    pos_bus_morado = (100, 100)
    pos_bus_gris = (100, 200)

    @staticmethod
    def cargar_imagen(path, size, rotacion=0):
        imagen = Image.open(path)
        imagen = imagen.resize(size)
        if rotacion != 0:
            imagen = imagen.rotate(rotacion, expand=True)
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
    fondo_tk = cargar_imagen(path=path_fondo, size=size_fondo)

    #* Imagenes de los semaforos sin rotar
    semaforo_rojo_tk = cargar_imagen(path_sem_rojo, size_sem)
    semaforo_amarillo_tk = cargar_imagen(path_sem_amarillo, size_sem)
    semaforo_verde_tk = cargar_imagen(path_sem_verde, size_sem)

    #* Imagenes de los semaforos rotados 90°
    semaforo_rojo_tk_90 = cargar_imagen(path_sem_rojo, size_sem, rotacion=270)
    semaforo_amarillo_tk_90 = cargar_imagen(path_sem_amarillo, size_sem, rotacion=270)
    semaforo_verde_tk_90 = cargar_imagen(path_sem_verde, size_sem, rotacion=270)

    #* Imagenes de los buses sin rotar
    bus_amarillo_tk = cargar_imagen(path_bus_amarillo, size_bus)
    bus_morado_tk = cargar_imagen(path_bus_morado, size_bus)
    bus_gris_tk = cargar_imagen(path_bus_gris, size_bus)

    #* Imagenes de los buses rotados 270°
    bus_amarillo_tk_270 = cargar_imagen(path_bus_amarillo, size_bus, rotacion=90)
    bus_morado_tk_270 = cargar_imagen(path_bus_morado, size_bus, rotacion=90)
    bus_gris_tk_270 = cargar_imagen(path_bus_gris, size_bus, rotacion=90)

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
            self.canvas.delete(imagen)


        if y2 >= self.size_ventana[1] or y1 <= 0:
            dy = -dy # Cambiar la dirección en el eje y
            self.canvas.delete(imagen)

        # Mover la imagen
        self.canvas.move(imagen, dx, dy)

        # Llamar a la función nuevamente después de 100 ms
        #self.ventana.after(100, self.mover_imagen, imagen, dx, dy)

    """Eventos de teclado"""
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
    def cambiar_imagen(self, imagen, color, rotacion=0):
        #print("Se ha cambiado de imagen")
        nueva_imagen = None
        if color == "red" and rotacion ==0:
            print("Se ha cambiado a rojo")
            nueva_imagen = self.semaforo_rojo_tk
        
        elif color == "yellow" and rotacion ==0:
            print("Se ha cambiado a amarillo")
            nueva_imagen = self.semaforo_amarillo_tk
        
        elif color == "green" and rotacion ==0:
            print("Se ha cambiado a verde")
            nueva_imagen = self.semaforo_verde_tk

        if color == "red" and rotacion != 0:
            print("Se ha cambiado a rojo")
            nueva_imagen = self.semaforo_rojo_tk_90
        
        elif color == "yellow" and rotacion != 0:
            print("Se ha cambiado a amarillo")
            nueva_imagen = self.semaforo_amarillo_tk_90
        
        elif color == "green" and rotacion != 0:
            print("Se ha cambiado a verde")
            nueva_imagen = self.semaforo_verde_tk_90

        # imagen se refiere a las variables tipo semaforo_inferior = canvas.create_image(p0_sem_inferior[0], p0_sem_inferior[1], anchor="nw", image=semaforo_rojo_tk)
        self.canvas.itemconfig(imagen, image=nueva_imagen)
        
    # Vincular las teclas de flechas con las funciones de movimiento
    ventana.bind("<Up>", mover_arriba)
    ventana.bind("<Down>", mover_abajo)
    ventana.bind("<Left>", mover_izquierda)
    ventana.bind("<Right>", mover_derecha)

    # Iniciar el bucle principal
    #ventana.mainloop()