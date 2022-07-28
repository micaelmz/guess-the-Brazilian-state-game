import pygame

sound = pygame.mixer

pygame.init()

RIGHT = sound.Sound(file='sounds/right.mp3')

WRONG = sound.Sound(file='sounds/wrong.mp3')
WRONG.set_volume(0.3)

CLICK = sound.Sound(file='sounds/click.mp3')