import sys, random
import pygame

class Jeu:
    # contenir toutes les variables et fonctions
    # utiles au jeu

    def __init__ (self):
        # on définis les dimensions de la fenetre 
        # de jeu 
        self.ecran = pygame.display.set_mode((800, 600))
        # puis on lui donne un titre
        pygame.display.set_caption("Jeu Snake")
        self.jeu_encours = True

        # creer les variables de position et 
        # direction du serpent
        self.serpent_position_x = 300
        self.serpent_position_y = 300
        self.serpent_direction_x = 0
        self.serpent_direction_y = 0
        self.serpent_corps = 10

    def fonction_principale(self):
        # permets de gérer les events, d'afficher
        # certains composants du jeu grace au while loop

        while self.jeu_encours:

            # on récupère chaque event de la méthode
            # "pygame.event.get()" qui contient tous 
            # les events du jeu
            for evenement in pygame.event.get():
                # pour permettre de fermer en appuyant 
                # sur la croix rouge
                if evenement.type == pygame.QUIT:
                    sys.exit()

                if evenement.type == pygame.KEYDOWN:

                    if evenement.key == pygame.K_RIGHT:
                        self.serpent_direction_x = 10
                        self.serpent_direction_y = 0

                    if evenement.key == pygame.K_LEFT:
                        self.serpent_direction_x = -10
                        self.serpent_direction_y = 0

                    if evenement.key == pygame.K_DOWN:
                        self.serpent_direction_y = 10
                        self.serpent_direction_x = 0

                    if evenement.key == pygame.K_UP:
                        self.serpent_direction_y = -10
                        self.serpent_direction_x = 0

            # faire bouger le serpent s'il se trouve dans
            # les limites du jeu
        if self.serpent_position_x <= 100 or self.serpent_position_x >= 700 \
            or self.serpent_position_y <= 100 or self.serpent_position_y >= 600:

            sys.exit()

            # faire bouger le serpent
            self.serpent_position_x += self.serpent_direction_x
            self.serpent_position_y += self.serpent_direction_y

            # creer une fonction permettant de creer un 
            # rectangle representant les limites du jeu
            # aux dimensions: (100, 100, 600, 500), et
            # l'épaisseur du rectangle qui est égale à 3
            def creer_limites(self):
                pygame.draw.rect(self.ecran,(255,255,255),(100,100,600,500),3)

            # afficher le serpent
            pygame.draw.rect(self.ecran,(0, 255, 0),(self.serpent_position_x,self.serpent_position_y,self.serpent_corps,self.serpent_corps))

             # afficher les limites
            self.creer_limites()
                    
            # on choisis la couleur du background 
            # en RGB
            self.ecran.fill(((0, 0, 0)))

            pygame.display.flip()

if __name__ == '__main__':

    pygame.init()
    Jeu().fonction_principale()
    pygame.quit()
