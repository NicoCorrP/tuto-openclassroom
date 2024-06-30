import pygame
import sys
import random

# Définir les couleurs
NOIR = (0, 0, 0)
BLANC = (255, 255, 255)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)

class Jeu:
    def __init__(self):
        pygame.init()
        self.ecran = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Jeu Snake")

        # variables du jeu
        self.jeu_encours = True
        self.ecran_du_debut = True

        # Définir la zone de jeu et la bordure
        self.zone_jeu = pygame.Rect(50, 50, 700, 500)
        self.bordure = 10

        # Initialisation du serpent
        self.serpent_position_x = 300
        self.serpent_position_y = 300
        self.serpent_direction_x = 0
        self.serpent_direction_y = 0
        self.serpent_corps = 10

        # position de la pomme
        self.pomme_position_x = random.randrange(110, 690, 10)
        self.pomme_position_y = random.randrange(110, 590, 10)
        self.pomme = 10
        # Fixer les fps
        self.clock = pygame.time.Clock()

        # créer une liste contenant toutes les positions 
        # du serpent
        self.position_serpent = []

        # Variables de taille du serpent
        self.taille_du_serpent = 1
        self.ecran_du_debut = True

        # Définir les couleurs initiales
        self.couleur_serpent = (0, 255, 0)
        self.couleur_pomme = (255, 0, 0)
        self.couleur_fond = (0, 0, 0)

        # Initialisation des images
        self.image_tete_serpent = pygame.image.load('la_tete_du_serpent.png')
        self.image = pygame.image.load('jeu-snake.jpg')
        self.image_titre = pygame.transform.scale(self.image, (200, 100))

        # variable du serpent
        self.score = 0
        self.meilleur_score = 0

        # créer la position et taille du bouton de pause
        self.bouton_pause = pygame.Rect(700, 500, 100, 50)
        self.jeu_en_pause = False

        # Créer des couleurs aléatoires à chaque démarrage
        self.couleur_serpent = self.couleur_aleatoire()
        self.couleur_pomme = self.couleur_aleatoire()
        self.couleur_fond = self.couleur_aleatoire()

    def couleur_aleatoire(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # créer une fonction permettant de créer un rectangle représentant les limites du jeu
    # aux dimensions: (100, 100, 600, 500), et l'épaisseur du rectangle qui est égale à 3
    def creer_limites(self):
        pygame.draw.rect(self.ecran, BLANC, (100, 100, 600, 500), 3)

    def creer_message(self, taille, message, rectangle, couleur):
        if taille == 'petite':
            police = pygame.font.SysFont('Lato', 20, False)
        elif taille == 'moyenne':
            police = pygame.font.SysFont('Lato', 30, False)
        elif taille == 'grande':
            police = pygame.font.SysFont('Lato', 40, True)
        texte = police.render(message, True, couleur)
        self.ecran.blit(texte, rectangle)

    def sauvegarder_meilleur_score(self):
        with open('meilleur_score.txt', 'w') as fichier:
            fichier.write(str(self.meilleur_score))

    def charger_meilleur_score(self):
        try:
            with open('meilleur_score.txt', 'r') as fichier:
                self.meilleur_score = int(fichier.read())
        except:
            self.meilleur_score = 0

    def fonction_principale(self):

        while self.ecran_du_debut:
            for evenement in pygame.event.get():
                if evenement.type == pygame.QUIT:
                    self.jeu_encours = False
                    pygame.quit()
                    sys.exit()
                    
                if evenement.type == pygame.KEYDOWN:
                    if evenement.key == pygame.K_RETURN:
                        self.ecran_du_debut = False

            self.ecran.fill(self.couleur_fond)
            self.ecran.blit(self.image_titre, (300, 50, 100, 50))
            self.creer_message('petite', 'Le but du jeu est que le serpent se développe', (250, 200, 200, 5), (240, 240, 240))
            self.creer_message('petite', 'pour cela, il a besoin de pommes, mangez-en autants que possible,mais faites bien attention à ne pas vous mordre la queue !!', (190, 220, 200, 5), (240, 240, 240))
            self.creer_message('moyenne', 'Appuyer sur Enter pour commencer', (200, 450, 200, 5), BLANC)

            pygame.display.flip()

        while self.jeu_encours:
            for evenement in pygame.event.get():
                if evenement.type == pygame.QUIT:
                    self.jeu_encours = False
                    pygame.quit()
                    sys.exit()

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
                
                if evenement.type == pygame.MOUSEBUTTONDOWN:
                    if self.bouton_pause.collidepoint(evenement.pos):
                        self.jeu_en_pause = not self.jeu_en_pause

            if not self.jeu_en_pause:
                if self.serpent_position_x <= 100 or self.serpent_position_x >= 700 or self.serpent_position_y <= 100 or self.serpent_position_y >= 600:
                    self.jeu_encours = False

                self.serpent_mouvement()

            # crée la condition si le serpent mange la pomme
            if self.pomme_position_y == self.serpent_position_y and self.serpent_position_x == self.pomme_position_x:
                self.pomme_position_x = random.randrange(110, 690, 10)
                self.pomme_position_y = random.randrange(110, 590, 10)
                # augmenter la taille du serpent
                self.taille_du_serpent += 1
                # augmenter le score
                self.score += 1
                if self.score > self.meilleur_score:
                    self.meilleur_score = self.score

            tete_serpent = [self.serpent_position_x, self.serpent_position_y]
            self.position_serpent.append(tete_serpent)
            if len(self.position_serpent) > self.taille_du_serpent:
                self.position_serpent.pop(0)

            self.afficher_les_elements()
            self.se_mord(tete_serpent)
            self.afficher_score()
            self.creer_limites()
            self.ajuster_difficulte()

            for segment in self.position_serpent[:-1]:
                if segment == tete_serpent:
                    self.jeu_encours = False

            self.ecran.fill(NOIR)
            for segment in self.position_serpent:
                pygame.draw.rect(self.ecran, VERT, (segment[0], segment[1], self.serpent_corps, self.serpent_corps))
            pygame.draw.rect(self.ecran, ROUGE, (self.pomme_position_x, self.pomme_position_y, self.pomme, self.pomme))

            if self.serpent_position_x == self.pomme_position_x and self.serpent_position_y == self.pomme_position_y:
                self.pomme_position_x = random.randrange(110, 690, 10)
                self.pomme_position_y = random.randrange(110, 590, 10)
                self.taille_du_serpent += 1
                self.score += 1

            self.creer_message('grande', 'Snake Game', (320, 10, 100, 50), BLANC)
            self.creer_message('grande', '{}'.format(str(self.score)), (375, 50, 50, 50), BLANC)
            pygame.draw.rect(self.ecran, BLANC, self.bouton_pause)
            self.creer_message('moyenne', 'Pause', (710, 510, 80, 30), NOIR)
            pygame.display.flip()

        self.ecran_game_over()

    def serpent_mouvement(self):
        self.serpent_position_x += self.serpent_direction_x
        self.serpent_position_y += self.serpent_direction_y

    def afficher_les_elements(self):
        self.ecran.fill(self.couleur_fond)
        self.ecran.blit(self.image_tete_serpent, 
            (self.serpent_position_x, self.serpent_position_y, self.serpent_corps, self.serpent_corps))
        pygame.draw.rect(self.ecran, self.couleur_pomme, (self.pomme_position_x, self.pomme_position_y, self.pomme, self.pomme))
        self.afficher_serpent()

    def afficher_serpent(self):
        for partie_du_serpent in self.position_serpent[:-1]:
            pygame.draw.rect(self.ecran, self.couleur_serpent, (partie_du_serpent[0], partie_du_serpent[1], self.serpent_corps, self.serpent_corps))

    def se_mord(self, tete_serpent):
        for partie_du_serpent in self.position_serpent[:-1]:
            if partie_du_serpent == tete_serpent:
                self.jeu_encours = False

    def afficher_score(self):
        self.creer_message('grande', 'Snake Game', (320, 10, 100, 50), (255, 255, 255))
        self.creer_message('grande', '{}'.format(str(self.score)), (375, 50, 50, 50), (255, 255, 255, 255))

    def ajuster_difficulte(self):
        if self.score < 5:
            self.clock.tick(10)
        elif self.score < 10:
            self.clock.tick(15)
        else:
            self.clock.tick(20)

    def pause(self):
        paused = True
        while paused:
            for evenement in pygame.event.get():
                if evenement.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evenement.type == pygame.KEYDOWN:
                    if evenement.key == pygame.K_c:
                        paused = False
                    elif evenement.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
            self.creer_message('grande', 'Pause', (300, 200, 200, 50), BLANC)
            self.creer_message('moyenne', 'Appuyer sur C pour continuer ou Q pour quitter', (150, 300, 500, 50), BLANC)
            pygame.display.flip()
            self.clock.tick(5)

    def ecran_game_over(self):
        if self.score > self.meilleur_score:
            self.meilleur_score = self.score
            self.sauvegarder_meilleur_score()

        while not self.jeu_encours:
            self.ecran.fill(NOIR)
            self.creer_message('grande', 'Game Over', (300, 200, 200, 50), ROUGE)
            self.creer_message('moyenne', 'Score: {}'.format(self.score), (350, 300, 100, 50), BLANC)
            self.creer_message('moyenne', 'Meilleur Score: {}'.format(self.meilleur_score), (350, 350, 100, 50), BLANC)
            self.creer_message('petite', 'Appuyer sur Enter pour recommencer ou Esc pour quitter', (200, 400, 400, 50), BLANC)
            self.creer_message('moyenne', 'Recommencer', (320, 510, 160, 30), NOIR)
            pygame.display.flip()

            for evenement in pygame.event.get():
                if evenement.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evenement.type == pygame.KEYDOWN:
                    if evenement.key == pygame.K_RETURN:
                        self.__init__()
                        self.fonction_principale()
                    if evenement.key == pygame.K_ESCAPE:
                        pygame
                        pygame.quit()
                        sys.exit()

if __name__ == "__main__":
    jeu = Jeu()
    jeu.fonction_principale()
