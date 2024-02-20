import constantes as c
import pygame
import math

# Modifications des paramètres principaux de la fenêtre
pygame.display.set_caption("Astral Shooter")
fenetre_jeu = pygame.display.set_mode((c.LARGEUR_FENETRE, c.HAUTEUR_FENETRE))
pygame.display.set_icon(c.ICONE_JEU)

CENTRE_CANON = c.POSTION_CENTRE_CANON_SANS_ROUE
D_EFF_BOUTON = c.DIMENSION_IMAGE_EFFET_BOUTON

intensite_pesanteur = c.INTENSITE_PESANTEUR_TERRE

position_x_boulet = 0
position_y_boulet = 0

position_x_tir = 0
position_y_tir = 0
vitesse_initiale_tir = 0

vitesse_initiale = c.VITESSE_BOULET_MIN

angle_rotation = -c.ANGLE_ROTATION_INITAL

temps_debut_explosion = 0
coordonnees_explosion = 0, 0

nombre_vies_actuel = c.NOMBRE_VIES_INITIAL

en_tir = False
en_animation_tir = False

en_explosion = False

nombre_clic_en_jeu = 0
tir_possible = False

en_execution = True
en_jeu = False


def game_over():
    global intensite_pesanteur, position_x_boulet, position_y_boulet, position_x_tir, position_y_tir, vitesse_initiale_tir, vitesse_initiale, angle_rotation
    global temps_debut_explosion, coordonnees_explosion, nombre_vies_actuel, en_tir, en_animation_tir, en_explosion, nombre_clic_en_jeu
    global tir_possible, en_jeu

    intensite_pesanteur = c.INTENSITE_PESANTEUR_TERRE

    position_x_boulet = 0
    position_y_boulet = 0

    position_x_tir = 0
    position_y_tir = 0
    vitesse_initiale_tir = 0

    vitesse_initiale = c.VITESSE_BOULET_MIN

    angle_rotation = -c.ANGLE_ROTATION_INITAL

    temps_debut_explosion = 0
    coordonnees_explosion = 0, 0

    nombre_vies_actuel = c.NOMBRE_VIES_INITIAL

    en_tir = False
    en_animation_tir = False

    en_explosion = False

    nombre_clic_en_jeu = 0
    tir_possible = False

    en_jeu = False


def en_collision_boulet(boulet_canon_rect):
    return boulet_canon_rect.colliderect(c.SOL_RECT) or boulet_canon_rect.colliderect(c.MUR_RECT)\
        or boulet_canon_rect.colliderect(c.PERSONNAGE_RECT)


def fonction_trajectoire(x, alpha, v0, g):
    return (-1 / 2) * g * (x / (v0 * math.cos(alpha))) ** 2 + x * math.tan(alpha)


def pivoter_fleche_jauge():
    global angle_rotation

    if not en_animation_tir:
        if en_tir and angle_rotation >= -c.ANGLE_ROTATION_MAXIMAL:
            angle_rotation -= (c.ANGLE_ROTATION_MAXIMAL - c.ANGLE_ROTATION_INITAL) * c.INCREMENTATION_VITESSE / \
                              (c.VITESSE_BOULET_MAX - c.VITESSE_BOULET_MIN)

    else:
        if angle_rotation < -5:
            angle_rotation += 10
        else:
            angle_rotation = -c.ANGLE_ROTATION_INITAL

    image_fleche_pivote = pygame.transform.rotate(c.IMAGE_FLECHE_JAUGE, angle_rotation)
    fleche_pivote_rect = image_fleche_pivote.get_rect(center=c.POSITION_CENTRE_FLECHE_JAUGE)

    fenetre_jeu.blit(image_fleche_pivote, fleche_pivote_rect)

def angle_tir_canon(position_x, position_y):
    longueur_adjacent = position_x - CENTRE_CANON[0]
    longueur_oppose = CENTRE_CANON[1] - position_y
    longueur_hypotenuse = math.sqrt(longueur_adjacent ** 2 + longueur_oppose ** 2)

    angle_tir = math.acos(longueur_adjacent / longueur_hypotenuse)
    if angle_tir < 0.2:
        angle_tir = 0.2
    elif angle_tir > 1.4:
        angle_tir = 1.4

    return angle_tir


def affichage_accueil(position_x, position_y):
    fenetre_jeu.blit(c.IMAGE_DECOR_ACCUEIL, (0, 0))
    fenetre_jeu.blit(c.IMAGE_BOUTON_JOUER, c.BOUTON_JOUER_RECT)

    if (c.LARGEUR_FENETRE / 2 - D_EFF_BOUTON / 2 < position_x < c.LARGEUR_FENETRE / 2 - D_EFF_BOUTON / 2 + D_EFF_BOUTON
            and c.HAUTEUR_FENETRE / 2 + c.POS_Y_BT_SUPP <
            position_y < c.HAUTEUR_FENETRE / 2 + c.POS_Y_BT_SUPP + D_EFF_BOUTON):
        fenetre_jeu.blit(c.IMAGE_EFFET_BOUTON, (c.LARGEUR_FENETRE / 2 - D_EFF_BOUTON / 2, c.HAUTEUR_FENETRE / 2 +
                                                c.POS_Y_BT_SUPP - c.POS_Y_EFFET_BT_SUPP))
    else:
        fenetre_jeu.blit(c.IMAGE_EFFET_BOUTON, (c.LARGEUR_FENETRE / 2 - D_EFF_BOUTON / 2, c.HAUTEUR_FENETRE))


def actualisation_jeu(position_x, position_y):
    global position_x_boulet, position_y_boulet
    global position_x_tir, position_y_tir, vitesse_initiale_tir
    global en_animation_tir, en_explosion
    global temps_debut_explosion
    global coordonnees_explosion
    global vitesse_initiale, vitesse_initiale_tir
    global angle_rotation
    global nombre_vies_actuel

    fenetre_jeu.blit(c.IMAGE_DECOR_TERRE, (0, 0))

    image_canon_pivote = pygame.transform.rotate(c.IMAGE_CANON_SANS_ROUE,
                                                 math.degrees(angle_tir_canon(position_x, position_y)))

    canon_pivote_rect = image_canon_pivote.get_rect(center=CENTRE_CANON)

    somme_decalage_coeur = c.POS_X_DERNIER_COEUR
    for indice_coeur_noir in range(c.NOMBRE_VIES_INITIAL - nombre_vies_actuel):
        fenetre_jeu.blit(c.IMAGE_COEUR_NOIR, (somme_decalage_coeur, c.POS_Y_COEUR))
        somme_decalage_coeur -= c.DECALAGE_COEUR

    for indice_coeur_rouge in range(nombre_vies_actuel):
        fenetre_jeu.blit(c.IMAGE_COEUR_ROUGE, (somme_decalage_coeur, c.POS_Y_COEUR))
        somme_decalage_coeur -= c.DECALAGE_COEUR

    fenetre_jeu.blit(c.IMAGE_PERSONNAGE, c.PERSONNAGE_RECT)

    fenetre_jeu.blit(image_canon_pivote, canon_pivote_rect)
    fenetre_jeu.blit(c.IMAGE_ROUE_CANON, (c.POS_X_ROUE_CANON, c.POS_Y_ROUE_CANON))

    fenetre_jeu.blit(c.IMAGE_JAUGE_TIR, (c.DECALAGE_JAUGE, c.DECALAGE_JAUGE))
    pivoter_fleche_jauge()

    if en_animation_tir:
        """
        Lorsque vous avez les coordonnées de deux points, disons O et M, vous pouvez créer un vecteur en soustrayant les coordonnées de O de celles de M. Ce vecteur représente la direction et la distance entre les deux points.

        Dans notre cas, le vecteur OM représente la direction et la distance du point O (centre du cercle) au point M (un point en dehors du cercle).

        La norme d'un vecteur est sa longueur dans l'espace. Dans un espace 2D, la norme d'un vecteur (x, y) est donnée par la formule :

        Cette direction normalisée nous indique la direction de OM. Nous multiplions ensuite cette direction par le rayon du cercle pour obtenir un vecteur avec la même direction mais une longueur égale au rayon du cercle. En ajoutant ce vecteur au point O, nous trouvons les coordonnées de l'intersection entre la droite OM et le cercle.

        En résumé, la normalisation du vecteur OM est importante car elle nous donne une direction à suivre à partir du point O vers le point M. En multipliant cette direction par le rayon du cercle, nous obtenons un vecteur qui pointe vers le point d'intersection entre la droite OM et le cercle.
        """

        # Vectorisation pour déterminer l'emplacement de l'apparition du boulet pour l'animation de tir

        # Soit le point O, de coordonnées = au centre du canon, et M, de coordonnées = à position de la souris;
        # Les coordonées du vecteur OM sont donc :
        om_pos_x_vect, om_pos_y_vect = position_x - CENTRE_CANON[0], position_y - CENTRE_CANON[1]

        # Norme du vecteur OM
        norme_vect_om = math.sqrt(om_pos_x_vect ** 2 + om_pos_y_vect ** 2)

        # Normalisation du vecteur OM
        direction_om_x, direction_om_y = om_pos_x_vect / norme_vect_om, om_pos_y_vect / norme_vect_om

        # Coordonnées de l'intersection avec le cercle
        pos_x_centre_bouche_canon = CENTRE_CANON[0] + direction_om_x * c.RAYON_CANON_TIR
        pos_y_centre_bouche_canon = CENTRE_CANON[1] + direction_om_y * c.RAYON_CANON_TIR

        position_x_boulet += vitesse_initiale_tir / 5
        position_y_boulet = fonction_trajectoire(position_x_boulet, angle_tir_canon(position_x_tir, position_y_tir),
                                                 vitesse_initiale_tir, intensite_pesanteur)

        boulet_canon_rect = c.IMAGE_BOULET_CANON.get_rect()
        boulet_canon_rect.x, boulet_canon_rect.y = \
            position_x_boulet + pos_x_centre_bouche_canon - 30, pos_y_centre_bouche_canon - position_y_boulet

        if not en_collision_boulet(boulet_canon_rect):
            fenetre_jeu.blit(c.IMAGE_BOULET_CANON, boulet_canon_rect)

        else:
            if boulet_canon_rect.colliderect(c.PERSONNAGE_RECT):
                nombre_vies_actuel -= 1

                if nombre_vies_actuel == 0:
                    game_over()

            position_x_boulet = 0
            position_y_boulet = 0

            position_x_tir = 0
            position_y_tir = 0
            vitesse_initiale_tir = 0

            vitesse_initiale = c.VITESSE_BOULET_MIN

            angle_rotation = -c.ANGLE_ROTATION_INITAL

            en_animation_tir = False
            en_explosion = True

            coordonnees_explosion = boulet_canon_rect.center
            temps_debut_explosion = pygame.time.get_ticks()

    if en_explosion:
        if pygame.time.get_ticks() - temps_debut_explosion < c.DUREE_EXPLOSION:
            explosion_rect = c.IMAGE_EXPLOSION.get_rect()
            explosion_rect.center = coordonnees_explosion
            fenetre_jeu.blit(c.IMAGE_EXPLOSION, explosion_rect)
        else:
            en_explosion = False
            temps_debut_explosion = 0


while en_execution:
    position_souris_x, position_souris_y = pygame.mouse.get_pos()

    if en_jeu:
        actualisation_jeu(position_souris_x, position_souris_y)

    else:
        affichage_accueil(position_souris_x, position_souris_y)

    if pygame.mouse.get_pressed()[0]:
        if not en_animation_tir and vitesse_initiale < c.VITESSE_BOULET_MAX and tir_possible:
            en_tir = True
            vitesse_initiale += c.INCREMENTATION_VITESSE

    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            en_execution = False
            pygame.quit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not en_jeu and c.BOUTON_JOUER_RECT.collidepoint(event.pos):
                en_jeu = True

        elif en_jeu and event.type == pygame.MOUSEBUTTONUP:
            nombre_clic_en_jeu += 1

            if tir_possible and not en_animation_tir:
                en_animation_tir = True
                en_tir = False

                position_x_tir, position_y_tir = position_souris_x, position_souris_y
                vitesse_initiale_tir = vitesse_initiale * c.MULTIPLICATEUR_VITESSE

            else:
                if nombre_clic_en_jeu > 0:
                    tir_possible = True

    pygame.time.Clock().tick(c.IPS)
