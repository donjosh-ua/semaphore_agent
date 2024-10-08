
import tkinter as tk
from PIL import Image, ImageTk

# Crear la ventana principal
class Ventana:
    #* path de las imágenes
    path_fondo = "src/intersection/assets/fondo.png"
    path_sem_rojo = "src/intersection/assets/rojo.png"
    path_sem_verde = "src/intersection/assets/verde.png"
    path_sem_amarillo = "src/intersection/assets/amarillo.png"

    #* size de las imágenes
    size_fondo = (1348, 793)
    size_sem = (46, 90)

    #* posición inicial de las imágenes
    p0_sem_inferior = (720, 450)


    def cargar_imagen(path, size):
        imagen = Image.open(path)
        imagen = imagen.resize(size)
        return ImageTk.PhotoImage(imagen)
        pass
        
    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Cambiar imagen")
    ventana.geometry("1348x793")

    # Crear el lienzo (Canvas)
    canvas = tk.Canvas(ventana, width=1348, height=793)
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


    # Mostrar la imagen de fondo
    canvas.create_image(0, 0, anchor="nw", image=fondo_tk)

    # Mostrar la imagen inicial y guardar la referencia del objeto
    semaforo_inferior = canvas.create_image(p0_sem_inferior[0], p0_sem_inferior[1], anchor="nw", image=semaforo_rojo_tk)

    semaforo_izquierdo = canvas.create_image(620, 250, anchor="nw", image=semaforo_verde_tk)

    velocidad_horizontal = 5
    velocidad_vertical = 5

    #* Movimiento de las imágenes
    def mover_imagen(self):
        global velocidad_horizontal, velocidad_vertical

        # Obtener las coordenadas actuales de la imagen
        x1, y1, x2, y2 = self.canvas.bbox(self.semaforo_inferior)

        # Verificar los límites de la ventana (rebote)
        if x2 >= 1348 or x1 <= 0:
            velocidad_horizontal = -velocidad_horizontal  # Cambiar la dirección en el eje x
        if y2 >= 793 or y1 <= 0:
            velocidad_vertical = -velocidad_vertical  # Cambiar la dirección en el eje y

        # Mover la imagen
        self.canvas.move(self.semaforo_inferior, velocidad_horizontal, velocidad_vertical)

        # Llamar a la función nuevamente después de 100 ms
        self.ventana.after(100, self.mover_imagen)

    # Iniciar el movimiento de la imagen
    #mover_imagen()

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
    ventana.mainloop()