from pygame.mixer import Sound
from pygame import init



class SoundEffect:
    def __init__(self):
        init()
        self.click = Sound(file='sounds/right.mp3')

    def click(self):
        self.click.play()
'''
    def right_answer():
        sound.load('sounds/right.mp3')
        sound.set_volume(0.5)
        sound.play()


    def wrong_answer():
        sound.load('sounds/right.mp3')
        sound.set_volume(0.5)
        sound.play()


    def game_over():
        pygame.init()
        pygame.mixer.music.load('sounds/game_over.mp3')
        pygame.mixer.music.play()
'''