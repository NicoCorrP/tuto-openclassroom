import sys
import random
import pygame

class Jeu:
    # contenir toutes les variables et fonctions utiles au jeu

    def __init__(self):
        # on définit les dimensions de la fenêtre de jeu
        self.ecran = pygame.display.set_mode((800, 600))
        # puis on lui donne un titre
        pygame.display.set_caption("Jeu Snake")
        self.jeu_encours = True

        # créer les variables de position et direction du serpent
        self.serpent_position_x = 300
        self.serpent_position_y = 300
        self.serpent_direction_x = 0
        self.serpent_direction_y = 0
        self.serpent_corps = 10

        # créer la position de la pomme
        self.pomme_position_x = random.randrange(110, 690, 10)
        self.pomme_position_y = random.randrange(110, 590, 10)
        self.pomme = 10
        # fixer les fps
        self.clock = pygame.time.Clock()

        # créer une liste contenant toutes les positions du serpent
        self.position_serpent = []

        # créer la variable liée à la taille du serpent
        self.taille_du_serpent = 1

    # créer une fonction permettant de créer un rectangle représentant les limites du jeu
    # aux dimensions: (100, 100, 600, 500), et l'épaisseur du rectangle qui est égale à 3
    def creer_limites(self):
        pygame.draw.rect(self.ecran, (255, 255, 255), (100, 100, 600, 500), 3)

    def fonction_principale(self):
        # permet de gérer les events, d'afficher certains composants du jeu grâce au while loop

        while self.jeu_encours:
            # on récupère chaque event de la méthode "pygame.event.get()" qui contient tous les events du jeu
            for evenement in pygame.event.get():
                # pour permettre de fermer en appuyant sur la croix rouge
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

            # faire bouger le serpent s'il se trouve dans les limites du jeu
            if self.serpent_position_x <= 100 or self.serpent_position_x >= 700 \
                    or self.serpent_position_y <= 100 or self.serpent_position_y >= 600:
                self.jeu_encours = False

            # fonction pour faire bouger le serpent
            self.serpent_mouvement()

            # crée la condition si le serpent mange la pomme
            if self.pomme_position_y == self.serpent_position_y and self.serpent_position_x == self.pomme_position_x:
                self.pomme_position_x = random.randrange(110, 690, 10)
                self.pomme_position_y = random.randrange(110, 590, 10)

                # augmenter la taille du serpent
                self.taille_du_serpent += 1

            # créer une liste qui contient la tête du serpent
            tete_serpent = [self.serpent_position_x, self.serpent_position_y]

            # ajouter la tête du serpent à la liste des positions du serpent
            self.position_serpent.append(tete_serpent)

            # condition pour résoudre le problème des positions du serpent avec la taille du serpent
            if len(self.position_serpent) > self.taille_du_serpent:
                self.position_serpent.pop(0)

            self.afficher_les_elements()
            self.se_mord(tete_serpent)

            # afficher les limites
            self.creer_limites()
            self.clock.tick(30)

    def serpent_mouvement(self):
        # faire bouger le serpent
        self.serpent_position_x += self.serpent_direction_x
        self.serpent_position_y += self.serpent_direction_y

    def afficher_les_elements(self):
        # on choisit la couleur du background en RGB
        self.ecran.fill((0, 0, 0))

        # afficher le serpent
        pygame.draw.rect(self.ecran, (0, 255, 0), (self.serpent_position_x, self.serpent_position_y, self.serpent_corps, self.serpent_corps))
        
        # afficher la pomme
        pygame.draw.rect(self.ecran, (255, 0, 0), (self.pomme_position_x, self.pomme_position_y, self.pomme, self.pomme))

        self.afficher_serpent()

    # afficher les autres parties du serpent
    def afficher_serpent(self):
        for partie_du_serpent in self.position_serpent:
            pygame.draw.rect(self.ecran, (0, 255, 0), (partie_du_serpent[0], partie_du_serpent[1], self.serpent_corps, self.serpent_corps))

    def se_mord(self, tete_serpent):
        # si le serpent se mord la queue alors le jeu s'arrête
        for partie_du_serpent in self.position_serpent[:-1]:
            if partie_du_serpent == tete_serpent:
                self.jeu_encours = False

        pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    Jeu().fonction_principale()
    pygame.quit()
    sys.exit()
