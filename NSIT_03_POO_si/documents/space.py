# necessaire pour charger les images et les sons
import pygame
import random
import math

# classe pour créer le vaisseau du joueur
class Joueur():
    def __init__(self):
        self.position = 500 - 32
        self.image = pygame.image.load("yellow_heart.png")
        self.sens = "O"
        self.vitesse = 10
        self.score = 0
        self.pv = 20

    # fait bouger le vaisseau de joueur
    def deplacer(self):
        if (self.sens == "droite") and (self.position < 870):
            self.position = self.position + self.vitesse
        elif (self.sens == "gauche") and (self.position > 95):
            self.position = self.position - self.vitesse

    # envoie une munition
    def tirer(self):
        self.sens = "O"

    # augmente le score
    def marquer(self):
        self.score = self.score + 1

class PV():
    def __init_(self, player):
        self.pv = player.pv
        self.font = pygame.font.Font('undertale_font.ttf', 32)

    def damage(self, player):
        font.render({player.pv}, '/20', True, (255, 0, 255))

# classe pour créer les munitions
class Balle():
    def __init__(self, tireur):
        self.tireur = tireur
        self.depart = tireur.position
        self.hauteur = 437
        self.image = pygame.image.load("balle.png")
        self.etat = "chargee"
        self.vitesse = 8
        self.longueur = 95

    # dirige la balle vers le haut de la fenêtre
    def bouger(self):
        if self.etat == "chargee":
            self.depart = self.tireur.position
            self.hauteur = 437
        elif self.etat == "tiree":
            self.hauteur = self.hauteur - self.vitesse
        if self.hauteur < 0:
            self.etat = "chargee"

    # recharge une balle quand la précedente disparaît
    def toucher(self, vaisseau, player):
        if (math.fabs(self.hauteur - vaisseau.hauteur) < 40):
            if(math.fabs(self.depart - vaisseau.depart) < 40):
                if self.etat == "chargee":
                    damage = pygame.mixer.Sound("damage.wav")
                    damage.play()
                    player.pv -= 1
                    self.longueur -= self.longueur/20
                    if player.pv <=0:
                        player.pv = 0
                    return True

                else:
                    self.etat = "chargee"
                    shot = pygame.mixer.Sound("shot.wav")
                    shot.play()
                    return True

# classe pour créer les ennemis
class Ennemi():
    NbEnnemis = 6

    def __init__(self):
        self.depart = random.randint(90, 800)
        self.hauteur = 10
        self.type = random.randint(1, 4)
        self.vitesse = 5
        self.image = pygame.image.load('invader2.png')

    # fait avancer un ennemi vers le bas de l'écran
    def avancer(self):
        self.hauteur = self.hauteur + self.vitesse

    # fait disparaitre un ennemi quand il est touché par une munition
    def disparaitre(self):
        self.depart = random.randint(90, 800)
        self.hauteur = 10
        self.type = random.randint(1, 4)
        if (self.type == 1):
            self.image = pygame.image.load("invader1.png")
            self.vitesse = 1
        elif (self.type == 2):
            self.image = pygame.image.load("invader2.png")
            self.vitesse = 2
        elif (self.type == 3):
            self.image = pygame.image.load("invader3.png")
            self.vitesse = 3
        elif (self.type == 4):
            self.image = pygame.image.load("invader4.png")
            self.vitesse = 4