class Entity:

    def __init__(self, type, speed, position, image):
        self.type = type
        self.speed = speed
        self.position = position
        self.image = image

    def set_image(self, image):
        self.image = image
    