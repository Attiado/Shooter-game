import pygame
import random
#classe du monster de notre jeu
class Monster(pygame.sprite.Sprite):

    def __init__(self,game):
        super().__init__()
        self.game = game
        #vie initial eli bch tetbadl
        self.health=100
        #vie max
        self.max_health=100
        self.attack =2
        self.image=pygame.image.load('assets/alien2.png')
        self.image=pygame.transform.scale(self.image , (100,100))

        #rect naamlouha bch naajmou nbadlou limage kima nhebou o win nhebu , nrodouha f rectangle yaany
        self.rect=self.image.get_rect()
        self.rect.x=600 + random.randint(0,150)
        self.rect.y=352
        self.velocity=0.07
    def damage(self,amount):
        #amount hua lqtté li bch ya5sr'ha mel health mtee3u
        self.health -= amount
        #verifier si son nouveau vie sup ou egale 0
        if self.health <=0:
            #Reapparaitre comme un nv monstre / najmou nfaskhouh zeda
            self.rect.x=600+ random.randint(0,150)
            self.velocity=0.09
            self.health=self.max_health
            #ajouter le nbre de points
            self.game.add_score(20)
            #si la barre devent est chargé à son max
            if self.game.comet_event.is_full_loaded():
            #retirer du jeu
                self.game.all_monsters.remove(self)

            # appel  de la methode pour essayer de declencher la pluie
                self.game.comet_event.attempt_fall()

    def update_health_bar(self,surface):
        #definir une couleur pour notre jauge de vie
        bar_color=(60, 162, 19)
        #definir une autre couleur pour larriere plan de la jauge
        back_bar_color = (60, 63 , 60)

        #definir la position de notre jauge de vie ainsi que sa largeur et son hauteur
        bar_position = [self.rect.x+6, self.rect.y-10, self.health, 5]
        #definir la position de larriere plan
        back_bar_position = [self.rect.x+6, self.rect.y-10, self.max_health, 5]

        #dessiner notre barre de vie khatr wa7da ta7t lo5raa
        #lezm lordre hedha tee3 les deux jauges
        pygame.draw.rect(surface,back_bar_color,back_bar_position)

        pygame.draw.rect(surface, bar_color, bar_position)


    def forward(self):
        #le deplacement ne se fait ssi il nya pas de collision avec un groupe de joueur
        #fonction de marcher vers le joueur
        if not self.game.check_collision(self,self.game.all_players):
            self.rect.x -= self.velocity
        #si le monstre est en collision avec le joueur
        else:
            #infliger des degats au joueur
            self.game.player.damage(self.attack)