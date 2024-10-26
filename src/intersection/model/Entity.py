class Entity:

    def __init__(self, type, speed, direction_x=0, direction_y=0, image_path="src/intersection/default.png"):
        self.type = type
        self.speed = speed
        self.direction_x = direction_x
        self.direction_y = direction_y
        self.image_path = image_path

    def set_image_path(self, image_path):
        self.image_path = image_path