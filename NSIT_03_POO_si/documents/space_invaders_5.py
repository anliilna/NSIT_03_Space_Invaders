import pygame  # importation de la librairie pygame
import space
import sys  # pour fermer correctement l'application

pygame.init()  # lancement des modules inclus dans pygame

screen = pygame.display.set_mode((800, 600)) # création d'une fenêtre de 800 par 600
pygame.display.set_caption("Space Invaders")
fond = pygame.image.load('background.png')  # chargement de l'image de fond

player = space.Joueur()  # creation du joueur
tir = space.Balle(player)  # creation de la balle
tir.etat = "chargee"
listeEnnemis = []  # creation des ennemis

for indice in range(space.Ennemi.NbEnnemis):
    vaisseau = space.Ennemi()
    listeEnnemis.append(vaisseau)

# BOUCLE DE JEU

running = True  # variable pour laisser la fenêtre ouverte

while running:  # boucle infinie pour laisser la fenêtre ouverte
    screen.blit(fond, (0, 0))  # dessin du fond
    # Gestion des événements
    # v parcours de tous les event pygame dans cette fenêtre
    for event in pygame.event.get():
        # v si l'événement est le clic sur la fermeture de la fenêtre
        if event.type == pygame.QUIT:
            running = False  # running est sur False
            sys.exit()  # pour fermer correctement

        # gestion du clavier
        # v si une touche a été tapée KEYUP quand on relache la touche
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:  # si la touche est la fleche gauche
                # v on déplace le vaisseau de 1 pixel sur la gauche
                player.sens = "gauche"
            # v si la touche est la fleche droite
            if event.key == pygame.K_RIGHT:
                # v on déplace le vaisseau de 1 pixel sur la gauche
                player.sens = "droite"
            if event.key == pygame.K_SPACE:  # espace pour tirer
                player.tirer()
                tir.etat = "tiree"

    # Actualisation de la scene
    # Gestions des collisions
    for ennemi in listeEnnemis:
        if tir.toucher(ennemi):
            ennemi.disparaitre()
            player.marquer()
    print(f"Score = {player.score} points")
    # placement des objets
    # le joueur
    player.deplacer()
    # v appel de la fonction qui dessine le vaisseau du joueur
    screen.blit(tir.image, [tir.depart, tir.hauteur])
    # la balle
    tir.bouger()
    # v appel de la fonction qui dessine le vaisseau du joueur
    screen.blit(player.image, [player.position, 500])
    # les ennemis
    for ennemi in listeEnnemis:
        ennemi.avancer()
        # v appel de la fonction qui dessine le vaisseau du joueur
        screen.blit(ennemi.image, [ennemi.depart, ennemi.hauteur])

    pygame.display.update()  # pour ajouter tout changement à l'écran