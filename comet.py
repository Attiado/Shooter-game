import pygame
import random
#classe pour gerer cette comete
class Comet(pygame.sprite.Sprite):
    def __init__(self,comet_event):
        super().__init__()
        #limage de la comet
        self.image=pygame.image.load("assets/comet.png")
        self.rect=self.image.get_rect()
        self.velocity =random.randint(1,6)
        self.rect.x=random.randint(20,550)
        self.rect.y= - random.randint(0,600)
        self.comet_event = comet_event
    def remove(self):
        self.comet_event.all_comets.remove(self)

        #verifier si le nbr de comets est de 0
        if len(self.comet_event.all_comets) == 0:
            #event est fini
            #remettre la barre à zero
            self.comet_event.reset_percent()
            #rapparaitre les monstres
            self.comet_event.game.spawn_monster()
            self.comet_event.game.spawn_monster()   

    def fall(self):
        self.rect.y+=self.velocity
        #ne tombe pas sur le sol
        if self.rect.y >=600:
            print ("SOOOOL")
            #retirer la boule de feu
            self.remove()
            #s'il nya plus de boules de feu
            if len(self.comet_event.all_comets) == 0:
                print ("eveneemtn finii ! ")
                #remettre la jauge au depart
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False
        #verifier si la boule touche le joueur
        if self.comet_event.game.check_collision(
                self, self.comet_event.game.all_players):
            print ("joueur touché!")
            #retirer la boule de feu
            self.remove()
            #subir 20 points de degats
            self.comet_event.game.player.damage(20)