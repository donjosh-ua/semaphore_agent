# Constantes
FIRST_STATE = 3
SECOND_STATE = 5
THIRD_STATE = 8
FOURTH_STATE = 10

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

VERTICAL_SPAWN_BUS = [(BUS_LENGTH/2, 459), (BUS_LENGTH/2, 539)]
HORIZONTAL_SPAWN_BUS = [(459, SCREEN_SIZE[1]-BUS_LENGTH/2), (539, SCREEN_SIZE[1]-BUS_LENGTH/2)]

SPAWN_POSICION = {
    "HORIZONTAL": {
        "bus": [(int(BUS_LENGTH/2), 459), (int(BUS_LENGTH/2), 539)], 
        "person":[]},
    "VERTICAL": {
        "bus": [(459, int(SCREEN_SIZE[1]-BUS_LENGTH/2)), (539, int(SCREEN_SIZE[1]-BUS_LENGTH/2))], 
        "person": []}}

#VERTICAL_SPAWN_PERSON = [(BUS_LENGTH/2, 459), (BUS_LENGTH/2, 539)]
#HORIZONTAL_SPAWN_PERSON = [(459, SCREEN_SIZE[1]-BUS_LENGTH/2), (539, SCREEN_SIZE[1]-BUS_LENGTH/2)]