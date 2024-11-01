import pygame
class ImageView:
    def __init__(self, model) -> None:
        self.model = model
        
    def draw(self, screen):
        screen.blit(self.model.image, self.model.rect)
        pygame.draw.circle(screen, (255, 0, 0), (int(self.model.rect.centerx), int(self.model.rect.centery)), 5)