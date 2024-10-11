
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
    pos_sem_inferior = (440, 450)
    pos_sem_izquierda = (260, 440)

    pos_bus_amarillo_0 = [34, 350]
    pos_bus_morado_0 = [34, 100]
    pos_bus_gris_0 = [34, 200]

    pos_bus_amarillo_270 = [370, 600]
    pos_bus_morado_270 = [307, 600]
    pos_bus_gris_270 = [207, 600]

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
    semaforo_inferior = canvas.create_image(pos_sem_inferior[0], pos_sem_inferior[1], anchor="nw", image=semaforo_rojo_tk)
    semaforo_izquierdo = canvas.create_image(pos_sem_izquierda[0], pos_sem_izquierda[1], anchor="nw", image=semaforo_verde_tk)

    #* Mostrar buses
    bus_amarillo_0 = canvas.create_image(pos_bus_amarillo_0[0], pos_bus_amarillo_0[1], anchor="nw", image=bus_amarillo_tk)
    bus_morado_0 = canvas.create_image(pos_bus_morado_0[0], pos_bus_morado_0[1], anchor="nw", image=bus_morado_tk)
    bus_gris_0 = canvas.create_image(pos_bus_gris_0[0], pos_bus_gris_0[1], anchor="nw", image=bus_gris_tk)

    bus_amarillo_270 = canvas.create_image(pos_bus_amarillo_270[0], pos_bus_amarillo_270[1], anchor="nw", image=bus_amarillo_tk_270)
    bus_morado_270 = canvas.create_image(pos_bus_morado_270[0], pos_bus_morado_270[1], anchor="nw", image=bus_morado_tk_270)
    bus_gris_270 = canvas.create_image(pos_bus_gris_270[0], pos_bus_gris_270[1], anchor="nw", image=bus_gris_tk_270)

    #* diccionario entre imágenes y posiciones
    dict_image_pos_init = dict()
    dict_image_pos_init[bus_amarillo_0] = pos_bus_amarillo_0
    dict_image_pos_init[bus_gris_0] = pos_bus_gris_0
    dict_image_pos_init[bus_morado_0] = pos_bus_morado_0
    dict_image_pos_init[bus_amarillo_270] = pos_bus_amarillo_270
    dict_image_pos_init[bus_gris_270] = pos_bus_gris_270
    dict_image_pos_init[bus_morado_270] = pos_bus_morado_270
    dict_image_pos_init[semaforo_inferior] = pos_sem_inferior
    dict_image_pos_init[semaforo_izquierdo] = pos_sem_izquierda

    #* diccionario entre imágenes y posiciones
    dict_image_pos = dict()
    dict_image_pos[bus_amarillo_0] = pos_bus_amarillo_0
    dict_image_pos[bus_gris_0] = pos_bus_gris_0
    dict_image_pos[bus_morado_0] = pos_bus_morado_0
    dict_image_pos[bus_amarillo_270] = pos_bus_amarillo_270
    dict_image_pos[bus_gris_270] = pos_bus_gris_270
    dict_image_pos[bus_morado_270] = pos_bus_morado_270
    dict_image_pos[semaforo_inferior] = pos_sem_inferior
    dict_image_pos[semaforo_izquierdo] = pos_sem_izquierda

    #* diccionario entre imágenes y sus tamaños
    dict_image_size = dict()
    dict_image_size[bus_amarillo_0] = size_bus
    dict_image_size[bus_gris_0] = size_bus
    dict_image_size[bus_morado_0] = size_bus
    dict_image_size[semaforo_inferior] = size_sem
    dict_image_size[semaforo_izquierdo] = size_sem

    #TODO: Funciones de movimiento de las imágenes
    def mover_imagen(self, imagen, dx, dy):

        # Obtener las coordenadas actuales de la imagen
        x1, y1, x2, y2 = self.canvas.bbox(imagen)

        """Esta parte es lo que hace que funcione como salva pantallas, es decir que rebote"""
        # Verificar los límites de la ventana (rebote)
        if x2 >= self.size_ventana[0] or x1 <= 0:

            x = self.dict_image_pos[imagen][0] - self.dict_image_pos_init[imagen][0]
            y = self.dict_image_pos_init[imagen][1]

            self.canvas.move(imagen, -x, 0)
            self.dict_image_pos[imagen] = self.dict_image_pos_init[imagen]
            return


        if y2 >= self.size_ventana[1] or y1 <= 0:
            x = self.dict_image_pos_init[imagen][0]
            y = self.dict_image_pos_init[imagen][1] - self.dict_image_pos[imagen][1]

            self.canvas.move(imagen, 0, self.dict_image_pos_init[imagen][1])
            self.dict_image_pos[imagen] = self.dict_image_pos_init[imagen]
            return

        # Mover la imagen
        self.canvas.move(imagen, dx, dy)
        self.dict_image_pos[imagen] = [self.dict_image_pos[imagen][0] + dx, self.dict_image_pos[imagen][1] + dy]

    # Función para cambiar la imagen
    def cambiar_imagen(self, imagen, color, rotacion=0):
        #print("Se ha cambiado de imagen")
        nueva_imagen = None
        if color == "red" and rotacion ==0:
            nueva_imagen = self.semaforo_rojo_tk
        
        elif color == "yellow" and rotacion ==0:
            nueva_imagen = self.semaforo_amarillo_tk
        
        elif color == "green" and rotacion ==0:
            nueva_imagen = self.semaforo_verde_tk

        if color == "red" and rotacion != 0:
            nueva_imagen = self.semaforo_rojo_tk_90
        
        elif color == "yellow" and rotacion != 0:
            nueva_imagen = self.semaforo_amarillo_tk_90
        
        elif color == "green" and rotacion != 0:
            nueva_imagen = self.semaforo_verde_tk_90

        # imagen se refiere a las variables tipo semaforo_inferior = canvas.create_image(p0_sem_inferior[0], p0_sem_inferior[1], anchor="nw", image=semaforo_rojo_tk)
        self.canvas.itemconfig(imagen, image=nueva_imagen)

    def get_posicion_image(self, imagen:int):
        return self.dict_image_pos[imagen]