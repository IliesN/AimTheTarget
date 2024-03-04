import pygame

pygame.init()


LARGEUR_FENETRE, HAUTEUR_FENETRE = 1280, 500


# Import de toutes les images ##############################

# Elements principaux
ICONE_JEU = pygame.image.load("elements_principaux/icone_jeu.png")
IMAGE_DECOR_ACCUEIL = pygame.image.load("decors/decor_accueil.jpg")
IMAGE_BOUTON_JOUER = pygame.image.load("elements_principaux/bouton_jouer.png")
IMAGE_EFFET_BOUTON = pygame.image.load("elements_principaux/effet_bouton.png")
IMAGE_CASE_ENCOCHE = pygame.image.load("elements_principaux/case_encoche.png")
IMAGE_CASE_ENCOCHE_EFFET = pygame.image.load("elements_principaux/case_encoche_effet.png")
IMAGE_ENCOCHE_VERTE = pygame.image.load("elements_principaux/encoche_verte.png")
IMAGE_TEXTE_MODE_ON = pygame.image.load("elements_principaux/texte_mode_facile_on.png")
IMAGE_TEXTE_MODE_OFF = pygame.image.load("elements_principaux/texte_mode_facile_off.png")
IMAGE_TEXTE_NOM_JEU = pygame.image.load("elements_principaux/texte_nom_jeu.png")
IMAGE_TEXTE_CLIQUEZ = pygame.image.load("elements_principaux/texte_cliquez.png")


# Decors
IMAGE_DECOR_TERRE = pygame.image.load("decors/decor_type_terre.jpg")


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


# Valeurs constantes

# Principales

IPS = 60

TEXTE_NOM_JEU_RECT = IMAGE_TEXTE_NOM_JEU.get_rect()
TEXTE_NOM_JEU_RECT.center = LARGEUR_FENETRE / 2, 100

TEXTE_CLIQUEZ_RECT = IMAGE_TEXTE_CLIQUEZ.get_rect()
TEXTE_CLIQUEZ_RECT.center = LARGEUR_FENETRE / 2, 220

DIMENSION_IMAGE_BOUTON = 150
DIMENSION_IMAGE_EFFET_BOUTON = 175

DECALAGE_EFFET_BOUTON = 10

DECALAGE_BOUTON_HAUT = 80

BOUTON_JOUER_RECT = IMAGE_BOUTON_JOUER.get_rect()
BOUTON_JOUER_RECT.center = LARGEUR_FENETRE / 2, HAUTEUR_FENETRE / 2 + DECALAGE_BOUTON_HAUT

EFFET_BOUTON_RECT = IMAGE_BOUTON_JOUER.get_rect()
EFFET_BOUTON_RECT.center = LARGEUR_FENETRE / 2 - DECALAGE_EFFET_BOUTON,\
    HAUTEUR_FENETRE / 2 + DECALAGE_BOUTON_HAUT - DECALAGE_EFFET_BOUTON

POS_X_SUPP_MODE_FACILE = 205

ENCOCHE_RECT = IMAGE_CASE_ENCOCHE.get_rect()
ENCOCHE_RECT.center = LARGEUR_FENETRE / 2 - 115, HAUTEUR_FENETRE / 2 + POS_X_SUPP_MODE_FACILE

LARGEUR_ENCOCHE, HAUTEUR_ENCOCHE = 50, 43

ENCOCHE_EFFET_RECT = IMAGE_CASE_ENCOCHE_EFFET.get_rect()
ENCOCHE_EFFET_RECT.center = ENCOCHE_RECT.center

TEXTE_MODE_FACILE_RECT = IMAGE_TEXTE_MODE_ON.get_rect()
TEXTE_MODE_FACILE_RECT.center = LARGEUR_FENETRE / 2 + 30, HAUTEUR_FENETRE / 2 + POS_X_SUPP_MODE_FACILE


# En jeu

INTENSITE_PESANTEUR_TERRE = 9.81


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
ANGLE_TIR_MAXIMAL = 1.1

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

LARGEUR_MARQUEUR_TRAJECTOIRE = 5
POS_DEBUT_MARQUEUR_TRAJ = 10
AJOUT_POS_MARQUEUR_TRAJ = 30
POS_FIN_MARQUEUR_TRAJ = 350
