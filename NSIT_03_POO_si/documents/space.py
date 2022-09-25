import pygame  # necessaire pour charger les images et les sons
import random
import math

class Joueur():  # classe pour créer le vaisseau du joueur
    def __init__(self):
        self.position = 500 - 32
        self.image = pygame.image.load("yellow_heart.png")
        self.sens = "O"
        self.vitesse = 10
        self.score = 0
        self.pv = 20

    def deplacer(self):  # fait bouger le vaisseau de joueur
        if (self.sens == "droite") and (self.position < 870):
            self.position = self.position + self.vitesse
        elif (self.sens == "gauche") and (self.position > 95):
            self.position = self.position - self.vitesse

    def tirer(self):  # envoie une munition
        self.sens = "O"

    def marquer(self):  # augmente le score
        self.score = self.score + 1

class Balle():  # classe pour créer les munitions
    def __init__(self, tireur):
        self.tireur = tireur
        self.depart = tireur.position
        self.hauteur = 437
        self.image = pygame.image.load("balle.png")
        self.etat = "chargee"
        self.vitesse = 8

    def bouger(self):  # dirige la balle vers les ennemis
        if self.etat == "chargee":
            self.depart = self.tireur.position
            self.hauteur = 437
        elif self.etat == "tiree":
            self.hauteur = self.hauteur - self.vitesse

        if self.hauteur < 0:
            self.etat = "chargee"

    # v recharge une balle quand la précedente touche un ennemi
    def toucher(self, vaisseau):
        if (math.fabs(self.hauteur - vaisseau.hauteur) < 40):
            if(math.fabs(self.depart - vaisseau.depart) < 40):
                self.etat = "chargee"
                return True

class Ennemi():  # classe pour créer les ennemis
    NbEnnemis = 6

    def __init__(self):
        self.depart = random.randint(90, 800)
        self.hauteur = 10
        self.type = random.randint(1, 4)
        self.vitesse = 5
        self.image = pygame.image.load('invader2.png')

    def avancer(self):  # fait avancer un ennemi vers le bas de l'écran
        self.hauteur = self.hauteur + self.vitesse

    # v fait disparaitre un ennemi quand il est touché par une munition
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