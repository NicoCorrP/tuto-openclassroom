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

        # creer la position de la pomme
        self.pomme_position_x = random.randrange(110,690,10)
        self.pomme_position_y = random.randrange(110,590,10)
        self.pomme = 10
        # fixer les fps
        self.clock = pygame.time.Clock()

        # creer une liste contenant toutes les positions
        # du serpent
        self.position_serpent = []

        # creer la variable liée à la taille du serpent
        self.taille_du_serpent = 1

    # creer une fonction permettant de creer un 
    # rectangle representant les limites du jeu
    # aux dimensions: (100, 100, 600, 500), et
    # l'épaisseur du rectangle qui est égale à 3
    def creer_limites(self):
        pygame.draw.rect(self.ecran, (255, 255, 255), (100, 100, 600, 500), 3)

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
                    self.jeu_encours = False

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
            self.jeu_encours = False

            # faire bouger le serpent
            self.serpent_position_x += self.serpent_direction_x
            self.serpent_position_y += self.serpent_direction_y

            # cree la cond si le serpent mange la pomme
            if self.pomme_position_y == self.serpent_position_y and self.serpent_position_x == self.pomme_position_x:
                self.pomme_position_x = random.randrange(110,690,10)
                self.pomme_position_y = random.randrange(110,590,10)

                # augmenter la taille du serpent

                self.taille_du_serpent += 1

                # creer une liste qui contient la tete du serpent
                la_tete_du_serpent = []
                la_tete_du_serpent.append(self.serpent_position_x)
                la_tete_du_serpent.append(self.pomme_position_y)

                # append la liste des positions du serpent 
                self.position_serpent.append(la_tete_du_serpent)

                # cond pour resoudre le probleme des positions
                # du serpent avec la taille du serpent
                if len(self.position_serpent) > self.taille_du_serpent:

                    self.position_serpent.pop(0)

            # on choisis la couleur du background 
            # en RGB
            self.ecran.fill(((0, 0, 0)))

            # afficher le serpent
            pygame.draw.rect(self.ecran,(0, 255, 0),(self.serpent_position_x,self.serpent_position_y,self.serpent_corps,self.serpent_corps))
            # afficher la pomme
            pygame.draw.rect(self.ecran(255,0,0),(self.pomme_position_x,self.pomme_position_y,self.pomme, self.pomme))

            # afficher les autres parties du serpent
            for partie_du_serpent in self.position_serpent:
                pygame.draw.rect(self.ecran(0,255,0),(partie_du_serpent[0],partie_du_serpent[1],self.serpent_corps,self.serpent_corps))

            # si le serpent se mord la queue alors le jeu s'arrête

            for partie_du_serpent in self.position_serpent[:-1]:

                if la_tete_du_serpent == partie_du_serpent:
            
                    sys.exit()

             # afficher les limites
            self.creer_limites()

            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()
        sys.exit()

if __name__ == '__main__':

    pygame.init()
    Jeu().fonction_principale()
