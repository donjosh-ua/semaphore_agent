class ImageView:
    def __init__(self, model) -> None:
        self.model = model
        
    def draw(self, screen):
        screen.blit(self.model.image, self.model.rect)