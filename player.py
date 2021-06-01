import pygame
from projectile import Projectile
#creer la classe pour le joueur
class Player (pygame.sprite.Sprite) :
    #ay classe bch nhotouh f jeu lezmou yheriti mel sprite
    def __init__(self,game):
        super().__init__()
        self.game=game
        #health c la vie du joueur qui ca va changer kif yakhser
        self.health = 100
        self.max_health = 100

        self.attack = 10
        #velocity hya lvitesse
        self.velocity = 3
        self.all_projectiles = pygame.sprite.Group()
        self.image=pygame.image.load('assets/player.png')
        self.image=pygame.transform.scale(self.image , (100,100))

        #get rect pour pouvoir deplacer limage
        self.rect = self.image.get_rect()
        self.rect.x=50
        self.rect.y=350

    def damage (self,amount):
        if self.health - amount > amount :
            self.health -= amount
        else :
            #si la joueur a decédé
            self.game.game_over()

    def update_health_bar(self,surface):
        pygame.draw.rect(surface, (60, 63 , 60),[self.rect.x+6, self.rect.y-10, self.max_health, 5])
        pygame.draw.rect(surface,(60, 162, 19),[self.rect.x+6, self.rect.y-10, self.health, 5])
    def launch_projectile (self):
        #creer une nouvelle instance de la classe Projecitle
       # projectile = Projectile()
        self.all_projectiles.add(Projectile(self))

    def move_right(self):
        #si le joueur nest pas en collision avec un monster
        if not self.game.check_collision(self,self.game.all_monsters):
            self.rect.x +=self.velocity

    def move_left(self):
        self.rect.x -=self.velocity