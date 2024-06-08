import sys
import random
import pygame

#couleurs
NOIR = (0, 0, 0)
BLANC = (255, 255, 255)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
GRIS = (240, 240, 240)

#dimensions
LARGEUR_ECRAN = 800
HAUTEUR_ECRAN = 600
TAILLE_SERPENT = 10
TAILLE_POMME = 10

#positions initiales
POSITION_INITIALE_SERPENT = (300, 300)
LIMITES_JEU = (100, 100, 600, 500)


class Jeu:
    # contenir toutes les variables et fonctions utiles au jeu

    def __init__(self):
        # initialisation de tous les modules de Pygame
        pygame.init()
        # on définit les dimensions de la fenêtre de jeu
        self.ecran = pygame.display.set_mode((LARGEUR_ECRAN, HAUTEUR_ECRAN))
        # puis on lui donne un titre
        pygame.display.set_caption("Jeu Snake")
        self.jeu_encours = True
        self.ecran_du_debut = True
        self.image_tete_serpent = pygame.image.load('la_tete_du_serpent.png')
        # charger l'image
        self.image = pygame.image.load('jeu-snake.jpg')
        # retrecir l'image
        self.image_titre = pygame.transform.scale(self.image,(200,100))
        # fixer les fps
        self.clock = pygame.time.Clock()
        

    def gerer_evenements(self):
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                self.jeu_encours = False
                pygame.quit()
                sys.exit()
            if evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RIGHT and self.serpent_direction_x == 0:
                    self.serpent_direction_x = TAILLE_SERPENT
                    self.serpent_direction_y = 0
            elif evenement.key == pygame.K_LEFT and self.serpent_direction_x == 0:
                    self.serpent_direction_x = -TAILLE_SERPENT
                    self.serpent_direction_y = 0
            elif evenement.key == pygame.K_DOWN and self.serpent_direction_y == 0:
                    self.serpent_direction_y = TAILLE_SERPENT
                    self.serpent_direction_x = 0
            elif evenement.key == pygame.K_UP and self.serpent_direction_y == 0:
                    self.serpent_direction_y = -TAILLE_SERPENT
                    self.serpent_direction_x = 0
    def fonction_principale(self):
        while self.ecran_du_debut:
            self.afficher_ecran_debut()

        while self.jeu_encours:
            self.gerer_evenements()
            self.mise_a_jour_jeu()
            self.afficher_les_elements()
            self.creer_limites()
            self.afficher_score()
            self.ajuster_difficulte()
        self.ecran_game_over()

    # fonction de reinitialisation des variables
    def reinitialiser_jeu(self):
        self.serpent_position_x, self.serpent_position_y = POSITION_INITIALE_SERPENT
        self.serpent_direction_x = 0
        self.serpent_direction_y = 0
        # créer une liste contenant toutes les positions du serpent
        self.position_serpent = []
        self.taille_du_serpent = 1
        # variable du score
        self.score = 0
        self.pomme_position_x = random.randrange(110,690,10)
        self.pomme_position_y = random.randrange(110,590,10)

    # créer une fonction permettant de créer un rectangle représentant les limites du jeu
    # aux dimensions: (100, 100, 600, 500), et l'épaisseur du rectangle qui est égale à 3
    def creer_limites(self):
        pygame.draw.rect(self.ecran, BLANC, LIMITES_JEU, 3)

    def fonction_principale(self):
        # permet de gérer les events, d'afficher certains composants du jeu grâce au while loop

        while self.ecran_du_debut:
            for evenement in pygame.event.get():
            # pour permettre de fermer en appuyant sur la croix rouge
                if evenement.type == pygame.QUIT:
                    self.jeu_encours = False
                    pygame.quit()
                    sys.exit()

                if evenement.type == pygame.KEYDOWN:
                    if evenement.key == pygame.K_RETURN:

                        self.ecran_du_debut = False

                self. ecran.fill((0,0,0))
                # methode d'affichage des images et textes
                self.ecran.blit(self.image_titre,(300,50,100,50))
                # self.creer_message('petite','Snake',(300,300, 100,50), (255, 255, 255))
                self.creer_message('petite','Le but du jeu est que le serpent se développe'
                                    ,(250, 200, 200, 5), (240, 240, 240))
                self.creer_message('petite',' pour cela, il a besoin de pommes, mangez-en autants que possible, mais faites bien attention à ne pas vous mordre la queue !!',
                                   (190, 220, 200, 5), (240, 240, 240))
                self.creer_message('moyenne','Appuyer sur Enter pour commencer', (200, 450, 200, 5),
                                   (255, 255, 255))
                
                pygame.display.flip()

        while self.jeu_encours:
            # on récupère chaque event de la méthode "pygame.event.get()" qui contient tous les events du jeu
            for evenement in pygame.event.get():
                # pour permettre de fermer en appuyant sur la croix rouge
                if evenement.type == pygame.QUIT:
                    self.jeu_encours = False
                    pygame.quit()
                    sys.exit()

            # faire bouger le serpent en appuyant sur les touches du clavier
            # et eviter qu'il ne se morde en revenant sur lui-même
                if evenement.type == pygame.KEYDOWN:
                    if evenement.key == pygame.K_RIGHT and self.serpent_direction_x == 0:
                        self.serpent_direction_x = 10
                        self.serpent_direction_y = 0
                elif evenement.key == pygame.K_LEFT and self.serpent_direction_x == 0:
                        self.serpent_direction_x = -10
                        self.serpent_direction_y = 0
                elif evenement.key == pygame.K_DOWN and self.serpent_direction_y == 0:
                        self.serpent_direction_y = 10
                        self.serpent_direction_x = 0
                elif evenement.key == pygame.K_UP and self.serpent_direction_y == 0:
                        self.serpent_direction_y = -10
                        self.serpent_direction_x = 0


            # faire bouger le serpent s'il se trouve dans les limites du jeu
            if self.serpent_position_x <= 100 or self.serpent_position_x >= 700 or self.serpent_position_y <= 100 or self.serpent_position_y >= 600:
                self.jeu_encours = False

            # fonction pour faire bouger le serpent
            self.serpent_mouvement()

            # crée la condition si le serpent mange la pomme
            if self.pomme_position_y == self.serpent_position_y and self.serpent_position_x == self.pomme_position_x:
                self.pomme_position_x = random.randrange(110, 690, 10)
                self.pomme_position_y = random.randrange(110, 590, 10)
                # augmenter la taille du serpent
                self.taille_du_serpent += 1
                # augmenter le score
                self.score += 1

            # créer une liste qui contient la tête du serpent
            tete_serpent = [self.serpent_position_x, self.serpent_position_y]
            # ajouter la tête du serpent à la liste des positions du serpent
            self.position_serpent.append(tete_serpent)
            # condition pour résoudre le problème des positions du serpent avec la taille du serpent
            if len(self.position_serpent) > self.taille_du_serpent:
                self.position_serpent.pop(0)

            self.afficher_les_elements()
            self.se_mord(tete_serpent)
            self.afficher_score()
            self.creer_limites()
            self.ajuster_difficulte()
        
        self.ecran_game_over()


    def serpent_mouvement(self):
        # faire bouger le serpent
        self.serpent_position_x += self.serpent_direction_x
        self.serpent_position_y += self.serpent_direction_y

    def afficher_les_elements(self):
        # on choisit la couleur du background en RGB
        self.ecran.fill(NOIR)
        # afficher le serpent
        # pygame.draw.rect(self.ecran, (0, 255, 0), (self.serpent_position_x, self.serpent_position_y, self.serpent_corps, self.serpent_corps))
        self.ecran.blit(self.image_tete_serpent,(self.serpent_position_x,self.serpent_position_y,TAILLE_SERPENT,TAILLE_SERPENT))
        # afficher la pomme
        pygame.draw.rect(self.ecran, ROUGE, (self.pomme_position_x, self.pomme_position_y, TAILLE_POMME, TAILLE_POMME))
        self.afficher_serpent()

    def mise_a_jour_jeu(self):
        if self.serpent_position_x < 100 or self.serpent_position_x >= 700 or self.serpent_position_y < 100 or self.serpent_position_y >= 600:
            self.jeu_encours = False
        self.serpent_mouvement()
        if self.pomme_position_y == self.serpent_position_y and self.serpent_position_x == self.pomme_position_x:
            self.pomme_position_x = random.randrange(110, 690, 10)
            self.pomme_position_y = random.randrange(110, 590, 10)
            self.taille_du_serpent += 1
            self.score += 1
        tete_serpent = [self.serpent_position_x, self.serpent_position_y]
        self.position_serpent.append(tete_serpent)
        if len(self.position_serpent) > self.taille_du_serpent:
            self.position_serpent.pop(0)
        self.se_mord(tete_serpent)

    # afficher les autres parties du serpent
    def afficher_serpent(self):
        for partie_du_serpent in self.position_serpent[:-1]:
            pygame.draw.rect(self.ecran, (0, 255, 0), (partie_du_serpent[0], partie_du_serpent[1], self.serpent_corps, self.serpent_corps))

    def se_mord(self, tete_serpent):
        # si le serpent se mord la queue alors le jeu s'arrête
        for partie_du_serpent in self.position_serpent[:-1]:
            if partie_du_serpent == tete_serpent:
                self.jeu_encours = False

    # creer une fonction qui permets l'affichage des
    # messages
    def creer_message(self,font,message,message_rectangle,couleur):

        if font == 'petite':
            font = pygame.font.SysFont('Lato',20,False)

        elif font == 'moyenne':
            font = pygame.font.SysFont('Lato',30,False)

        elif font == 'grande':
            font = pygame.font.SysFont('Lato',40,True)

        # on affiche le message
        message = font.render(message,True,couleur)
        self.ecran.blit(message,message_rectangle)
        pygame.display.flip()

    def afficher_score(self):
        self.creer_message('grande','Snake Game', (320,10,100,50), BLANC)
        self.creer_message('grande','{}'.format(str(self.score)), (375,50,50,50), BLANC)

    def ajuster_difficulte(self):
        if self.score < 5:
            self.clock.tick(10)
        elif self.score < 10:
            self.clock.tick(15)
        else:
            self.clock.tick(20)

    def ecran_game_over(self):
        while not self.jeu_encours:
            self.ecran.fill(NOIR)
            self.creer_message('grande', 'Game Over', (300, 200, 200, 50), ROUGE)
            self.creer_message('moyenne', 'Score: {}'.format(self.score), (350, 300, 100, 50), BLANC)
            self.creer_message('petite', 'Appuyer sur Enter pour recommencer ou Esc pour quitter', (200, 400, 400, 50), BLANC)
            pygame.display.flip()

            for evenement in pygame.event.get():
                if evenement.type == pygame.QUIT:
                    pygame.quit()
                    sys;exit()
                if evenement.type == pygame.KEYDOWN:
                    if evenement.key == pygame.K_RETURN:
                        self.__init__()
                        self.fonction_principale()
                    if evenement.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

if __name__ == '__main__':
    Jeu().fonction_principale()
    # pour quitter Pygame correctement
    pygame.quit()
