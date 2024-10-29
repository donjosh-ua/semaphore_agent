import tkinter as tk
import pygame

"""
Valores de referencia
#! Tamaño de los semáforos: 45, 90
#! Tamaño del fondo: 1348, 793 -> 800x800
#! Tamano de los buses: 500, 226 -> 180, 81
#! Posición del semáforo inferior: 720, 450
#! Posición del semáforo izquierdo: 0, 0
"""


class ImageView:
    def __init__(self, model) -> None:
        self.model = model
        
    def draw(self, screen):
        #print("Dibujos cada cosa")
        # print(f"Modelo:{str(self.model.image)}, Recta:{str(self.model.rect)}")
        screen.blit(self.model.image, self.model.rect)
        
    