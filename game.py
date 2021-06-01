import pygame
from player import Player
from monster import Monster
from comet_event import CometFallEvent
from sounds import SoundManager
#classe qui varepresenter le jeu
class Game:
    def __init__(self):
        #definir si notre jeu a commencé ou non
        self.is_playing = False
        self.sound_manager = SoundManager()
        self.all_players=pygame.sprite.Group()
        self.player=Player(self)
        self.all_players.add(self.player)
        self.comet_event = CometFallEvent(self)
        self.all_monsters = pygame.sprite.Group()
        #pressed va contenir toutes les touches actives par le joueur
        self.pressed= {}
        #bsh yjywna 2 monster
        self.score = 0
    def start (self):
        self.is_playing=True
        self.spawn_monster()

    def game_over(self):
        #remettre le jeu à neuf ,retirer les monstres et remettre le joueur à 100 de vie , jeu en attente
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health

        self.is_playing = False
        self.score = 0
    def add_score(self,points=10):
        self.score+= points
    def update (self,screen):
            #afficher le score sur l'ecran
            font = pygame.font.SysFont("monoscpace",35)
            score_text = font.render (f"Score : {self.score}",1,(0,0,0))
            screen.blit(score_text , (20, 20 ))
            # appliquer le joueur  , 7atina rect khatr hia deja feha position
            screen.blit(self.player.image, self.player.rect)
            # actualiser la barre de vie du joueur
            self.player.update_health_bar(screen)
            #actualiser la barre d'evenements du jeu
            self.comet_event.update_bar(screen)
            # recuperer les projectiles du joueur
            for projectile in self.player.all_projectiles:
                projectile.move()

            # recuperer les monstres de notre jeu , bch yemchyw lel arneb
            for monster in self.all_monsters:
                monster.forward()
                monster.update_health_bar(screen)
            #recuperer les cometes
            for comet in self.comet_event.all_comets:
                comet.fall()

            # appliquer lensembles des images de mon groupe des projectiles
            self.player.all_projectiles.draw(screen)

            # appliquer lensemble des monstres
            self.all_monsters.draw(screen)
            #appliquer lensemples des images de mes cometes
            self.comet_event.all_comets.draw(screen)

            # verifier si le joueur souhaite aller a gauche ou a droite
            # l arneb twali temshy
            if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < 635:
                self.player.move_right()
            elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
                self.player.move_left()

    def check_collision (self ,sprite,group):
        #fn bch monster mayfoutch larneb
        return pygame.sprite.spritecollide(sprite,group,False,pygame.sprite.collide_mask)
    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)