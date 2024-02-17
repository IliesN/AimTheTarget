import pygame

pygame.init()


LARGEUR_FENETRE, HAUTEUR_FENETRE = 1280, 500


# Import de toutes les images ##############################

# Elements principaux
ICONE_JEU = pygame.image.load("elements_principaux/icone_jeu.png")
IMAGE_DECOR_ACCUEIL = pygame.image.load("decors/decor_accueil.jpg")
IMAGE_BOUTON_JOUER = pygame.image.load("elements_principaux/bouton_jouer.png")
IMAGE_EFFET_BOUTON = pygame.image.load("elements_principaux/effet_bouton.png")

# ...


# Decors
IMAGE_DECOR_TERRE = pygame.image.load("decors/decor_type_terre.jpg")

# ...


# Elements decors
IMAGE_CANON_SANS_ROUE = pygame.image.load("elements_decor/canon_sans_roue.png")
IMAGE_ROUE_CANON = pygame.image.load("elements_decor/roue_canon.png")
IMAGE_BOULET_CANON = pygame.image.load("elements_decor/boulet_canon.png")

# ...


# Valeurs constantes

# Principales

IPS = 60

DIMENSION_IMAGE_BOUTON = 150
POS_Y_BT_SUPP = 35

DIMENSION_IMAGE_EFFET_BOUTON = 175
POS_Y_EFFET_BT_SUPP = 10

BOUTON_JOUER_RECT = IMAGE_BOUTON_JOUER.get_rect()
BOUTON_JOUER_RECT.x, BOUTON_JOUER_RECT.y =\
    LARGEUR_FENETRE / 2 - DIMENSION_IMAGE_BOUTON / 2, HAUTEUR_FENETRE / 2 + POS_Y_BT_SUPP
# ...


# En jeu

INTENSITE_PESANTEUR_TERRE = 9.81

# ...

DECALAGE_X_CANON = 25

LARGEUR_IMAGE_CANON = 175
POS_X_CANON = DECALAGE_X_CANON - LARGEUR_IMAGE_CANON / 4 - 10
POS_Y_CANON = HAUTEUR_FENETRE - LARGEUR_IMAGE_CANON + 25

CANON_SANS_ROUE_RECT = IMAGE_CANON_SANS_ROUE.get_rect()
CANON_SANS_ROUE_RECT.x, CANON_SANS_ROUE_RECT.y = POS_X_CANON, POS_Y_CANON
POSTION_CENTRE_CANON_SANS_ROUE = CANON_SANS_ROUE_RECT.center

VITESSE_BOULET_MIN = 60
VITESSE_BOULET_MAX = 140

POS_X_ROUE_CANON = DECALAGE_X_CANON + 30
POS_Y_ROUE_CANON = HAUTEUR_FENETRE - 80

RAYON_CANON_TIR = LARGEUR_IMAGE_CANON / 2 - 13
