import pygame
import math
from game import Game
pygame.init()

#generer la fenetre de notre jeu

pygame.display.set_caption("Game dhouha")
screen = pygame.display.set_mode((635,600))


background = pygame.image.load('assets/bg.jpg')
# importer charger notre banniére
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (300,300))
banner_rect = banner.get_rect()
banner_rect.x = screen.get_width()/3.5
banner_rect.y = math.ceil(screen.get_height()/5)

#importer ou charger notre bouton pour lancer la partie

play_button = pygame.image.load("assets/button.png")
play_button = pygame.transform.scale(play_button , (60,60))
play_button_rect = play_button.get_rect()
play_button_rect.x =math.ceil( screen.get_width()/2.15)
play_button_rect.y = math.ceil(screen.get_height()/1.4)
#charger notre jeu
game =Game()
#running variable bch fenetre to93ed te5dem
running = True

 # boucle tant que cette condition est vrai
while running:
     #appliquer larriere plan a notre jeu , blit donner le background avec le positionnement
     screen.blit(background , (0,-150))

     # verifier si notre jeu a commencé ou non
     if game.is_playing:
         #delencher les instructs de la partie update game
         game.update(screen)
    #verifier si notre jeu n'a pas commencé
     else:
         #ajouter mon ecran de bienvenue
         screen.blit(banner, banner_rect )
         screen.blit(play_button ,play_button_rect)
     #mettre a jour lecran

     pygame.display.flip()
     # si le joueur ferme cette fenetre
     for event in pygame.event.get():
         #verifier que levnmnt est fermeture de genetre
         if event.type == pygame.QUIT:
             running = False
             #quiiter le jeu
             pygame.quit()
             print ("au revoir !")
        #detecter si un jouruer lache une touche du clavier
         elif event.type==pygame.KEYDOWN:
            game.pressed[event.key] =True

            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
         elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
         elif event.type == pygame.MOUSEBUTTONDOWN:
             #verification si la souris est en collision avec le bouton jouer
             if (play_button_rect.collidepoint(event.pos)):
                 #ma3neha la personne a cliqué sur la bouton  w yheb yal3éb , nhelou jeu so
                 game.start()
                 game.sound_manager.play('click')
