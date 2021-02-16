##########################IMPORTS#########################
import pygame

##########################################################

###################DISPLAY VARIABLES######################
WIDTH = 800
HEIGHT = 800

ROWS = 8
COLS = 8

SQUARE_SIZE = WIDTH//COLS

#RGB REFERENCE
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (44, 25))