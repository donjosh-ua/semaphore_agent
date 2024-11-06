import pygame
class ImageView:
    def __init__(self, model) -> None:
        self.model = model
        
    def draw(self, screen):
        screen.blit(self.model.image, self.model.rect)
        """It is to see the red point in the middle of the figure, the debug mode"""
        #pygame.draw.circle(screen, (255, 0, 0), (int(self.model.rect.centerx), int(self.model.rect.centery)), 5)