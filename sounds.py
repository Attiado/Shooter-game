import pygame

class SoundManager:
    def __init__(self):
        self.sounds= {
            'click' : pygame.mixer.Sound("assets/click.ogg")

        }
    def play(self,name):
        self.sounds[name].play()