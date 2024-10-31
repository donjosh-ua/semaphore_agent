# Constantes
TURN_GREEN_TIME = 2
YELLOW_TIME = 2
STRAIGHT_GREEN_TIME = 2 + TURN_GREEN_TIME + YELLOW_TIME
STRAIGHT_RED_TIME = 10
PEDESTRIAN_GREEN_TIME = STRAIGHT_RED_TIME - TURN_GREEN_TIME - YELLOW_TIME
FRAME_TIME = 0.1
DELAY_TIME = 1

MIN_SPEED = 5
MAX_SPEED = 20
FRAME_RATE = 30

SCREEN_SIZE = (1000, 1000)

TRAFFIC_LIGHT_LENGTH = 93
TRAFFIC_LIGHT_WIDTH = 25

PEDESTRIAN_LIGHT_LENGTH = 60
PEDESTRIAN_LIGHT_WIDTH = 20

BUS_LENGTH = 130
BUS_WIDTH = 65

PERSON_LENGTH = 30
PERSON_WIDTH = 30