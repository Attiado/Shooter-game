import pygame
from comet import Comet
import random

#creer une classe pour gerer cet event
class CometFallEvent :
    #lors du chargement => creer un compteur
    def __init__(self,game):
        self.percent=0
        self.percent_speed = 10
        self.game = game
        self.fall_mode=False
    #definir un groupe de sprites pour stocker nos cometes
        self.all_comets = pygame.sprite.Group()
    def add_percent(self):
        self.percent+=self.percent_speed/100
    def is_full_loaded (self):
        #nshufuha kemlet wla
        return self.percent>=100
    def reset_percent(self):
        self.percent=0
    def meteor_fall(self):
        #apparaite ma premiere comet
        x=random.randint(5,15)
        for i in range(x):
            self.all_comets.add(Comet(self))


    def attempt_fall(self):
        #la jauge est totalement chargé
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            print("Pluie des cometes !!")
            self.meteor_fall()
            self.fall_mode  = True #activer levenement
    def update_bar(self,surface):
        #ajouter pourcentage à la bar
        self.add_percent()

        #barre noir en arrie plan
        pygame.draw.rect(surface,(0,0,0),[
            0, #laxe des x
            surface.get_height()-20,#l'axe de y'
            surface.get_width() , #longueur
            10
        ])

        #barre rouge du jauge d'evenement
        pygame.draw.rect(surface, (187, 11, 11), [
            0,  # laxe des x
            surface.get_height()-20,  # l'axe de y'
            (surface.get_width()/100)*self.percent,  # longueur
            10
        ])