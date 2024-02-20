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
IMAGE_JAUGE_TIR = pygame.image.load("elements_decor/jauge.png")
IMAGE_FLECHE_JAUGE = pygame.image.load("elements_decor/fleche_jauge.png")
IMAGE_EXPLOSION = pygame.image.load("elements_decor/explosion.png")
IMAGE_COEUR_ROUGE = pygame.image.load("elements_decor/coeur_rouge.png")
IMAGE_COEUR_NOIR = pygame.image.load("elements_decor/coeur_noir.png")
IMAGE_PERSONNAGE = pygame.image.load("elements_decor/personnage.png")
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
INCREMENTATION_VITESSE = 0.83
MULTIPLICATEUR_VITESSE = 1.2

DIVISEUR_VITESSE = 5

DECALAGE_BOULET = 10

POS_X_ROUE_CANON = DECALAGE_X_CANON + 30
POS_Y_ROUE_CANON = HAUTEUR_FENETRE - 80

ANGLE_TIR_MINIMAL = 0.2
ANGLE_TIR_MAXIMAL = 1.4

RAYON_CANON_TIR = LARGEUR_IMAGE_CANON / 2 - 13

DECALAGE_JAUGE = 20

ANGLE_LIMITE_DIMINUTION = -5

ANGLE_ROTATION_INITAL = 1
ANGLE_ROTATION_MAXIMAL = 177

FLECHE_JAUGE_RECT = IMAGE_FLECHE_JAUGE.get_rect()
FLECHE_JAUGE_RECT.x, FLECHE_JAUGE_RECT.y = DECALAGE_JAUGE, DECALAGE_JAUGE
POSITION_CENTRE_FLECHE_JAUGE = FLECHE_JAUGE_RECT.center

DIMINUTION_FLECHE_JAUGE = 10

HAUTEUR_SOL_COLLISION = HAUTEUR_FENETRE - 50
SOL_RECT = pygame.Rect(0, HAUTEUR_SOL_COLLISION, LARGEUR_FENETRE, HAUTEUR_FENETRE)

LARGEUR_MUR_COLLISION = LARGEUR_FENETRE + 60
MUR_RECT = pygame.Rect(LARGEUR_FENETRE, 0, LARGEUR_MUR_COLLISION, HAUTEUR_FENETRE)

DUREE_EXPLOSION = 200

NOMBRE_VIES_INITIAL = 3

LARGEUR_COEUR = 30
POS_X_DERNIER_COEUR = LARGEUR_FENETRE - LARGEUR_COEUR - 25
POS_Y_COEUR = 20
DECALAGE_COEUR = LARGEUR_COEUR + 10

LARGEUR_PERSONNAGE = 29
HAUTEUR_PERSONNAGE = 140
PERSONNAGE_RECT = IMAGE_PERSONNAGE.get_rect()
PERSONNAGE_RECT.x, PERSONNAGE_RECT.y = LARGEUR_FENETRE - 45 - LARGEUR_PERSONNAGE,\
    HAUTEUR_FENETRE + HAUTEUR_SOL_COLLISION - HAUTEUR_FENETRE - HAUTEUR_PERSONNAGE
