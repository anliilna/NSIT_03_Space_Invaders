# importation de la librairie pygame
import pygame
import space
# pour fermer correctement l'application
import sys
# lancement des modules inclus dans pygame
pygame.init()

# musique de fond
pygame.mixer.music.load("Metal_Crusher.mp3")
# jouer la musique en boucle
pygame.mixer.music.play(-1)
# création d'une fenêtre de 1024 par 723
screen = pygame.display.set_mode((1024, 723))
pygame.display.set_caption("Mettaton fight")
# chargement de l'image de fond
fond = pygame.image.load('undertale_bg.jpg')
# creation du joueur
player = space.Joueur()
# creation de la balle
tir = space.Balle(player)
tir.etat = "chargee"
# creation des ennemis
listeEnnemis = []
pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# création d'une liste pour l'animation
frames = [pygame.image.load("Mettaton00.png"),
          pygame.image.load("Mettaton00.png"),
          pygame.image.load("Mettaton01.png"),
          pygame.image.load("Mettaton02.png"),
          pygame.image.load("Mettaton03.png"),
          pygame.image.load("Mettaton04.png"),
          pygame.image.load("Mettaton05.png"),
          pygame.image.load("Mettaton06.png"),
          pygame.image.load("Mettaton07.png"),
          pygame.image.load("Mettaton08.png"),
          pygame.image.load("Mettaton09.png"),
          pygame.image.load("Mettaton10.png"),
          pygame.image.load("Mettaton11.png"),
          pygame.image.load("Mettaton12.png"),
          pygame.image.load("Mettaton13.png"),
          pygame.image.load("Mettaton14.png"),
          pygame.image.load("Mettaton15.png")]

# création d'un objet "temps" pour suivre le temps
temps = pygame.time.Clock()

# création d'une nouvelle variable qui va aider
# à répéter le changement d'image de la liste
value = 0

for indice in range(space.Ennemi.NbEnnemis):
    vaisseau = space.Ennemi()
    listeEnnemis.append(vaisseau)

# BOUCLE DE JEU

running = True  # variable pour laisser la fenêtre ouverte

while running:  # boucle infinie pour laisser la fenêtre ouverte
    screen.blit(fond, (0, 0))  # dessin du fond

    # animation 25fps
    temps.tick(25)

    # remet value à 0 si elle est plus grande que la longueur de la liste
    if value >= len(frames):
        value = 0

    # ranger le sprite dans une variable image
    image = frames[value]

    # placement de l'image dans la fenêtre
    screen.blit(image, (415, 62))

    # augmentation de value après chaque changement d'image
    value += 1

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
                if tir.etat == "chargee":
                    shoot = pygame.mixer.Sound("shoot.wav")
                    shoot.play()
                player.tirer()
                tir.etat = "tiree"
            if event.key == pygame.K_ESCAPE:
                sys.exit()

    # Actualisation de la scene
    # Gestions des collisions
    for ennemi in listeEnnemis:
        if tir.toucher(ennemi):
                ennemi.disparaitre()
                player.marquer()

    print(f"Score = {player.score} points")
    print(f"pv = {player.pv} pv")
    # placement des objets
    # le joueur
    player.deplacer()
    # v appel de la fonction qui dessine le vaisseau du joueur
    screen.blit(tir.image, [tir.depart, tir.hauteur])
    # la balle
    tir.bouger()
    # v appel de la fonction qui dessine le vaisseau du joueur
    screen.blit(player.image, [player.position, 440])
    # les ennemis
    for ennemi in listeEnnemis:
        ennemi.avancer()
        # v appel de la fonction qui dessine le vaisseau du joueur
        screen.blit(ennemi.image, [ennemi.depart, ennemi.hauteur])

    pygame.display.update()  # pour ajouter tout changement à l'écran