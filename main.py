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

en_animation_tir = False

nombre_clic_en_jeu = 0
tir_possible = False

en_execution = True
en_jeu = False


def fonction_trajectoire(x, alpha, v0, g):
    return (-1/2) * g * (x / (v0 * math.cos(alpha))) ** 2 + x * math.tan(alpha)


def angle_tir_canon(position_x, position_y):
    limite_pos_x = 30
    limite_pos_y = 30

    if not (position_x >= CENTRE_CANON[0] + limite_pos_x and position_y <= CENTRE_CANON[1] - limite_pos_y):
        if position_x < CENTRE_CANON[0] + limite_pos_x:
            position_x = CENTRE_CANON[0] + limite_pos_x
        elif position_y > CENTRE_CANON[1] - limite_pos_y:
            position_y = CENTRE_CANON[1] - limite_pos_y

    longueur_adjacent = position_x - CENTRE_CANON[0]
    longueur_oppose = CENTRE_CANON[1] - position_y
    longueur_hypotenuse = math.sqrt(longueur_adjacent ** 2 + longueur_oppose ** 2)

    return math.acos(longueur_adjacent / longueur_hypotenuse)


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

    fenetre_jeu.blit(c.IMAGE_DECOR_TERRE, (0, 0))

    image_canon_pivote = pygame.transform.rotate(c.IMAGE_CANON_SANS_ROUE,
                                                 math.degrees(angle_tir_canon(position_x, position_y)))
    canon_pivote_rect = image_canon_pivote.get_rect(center=CENTRE_CANON)

    fenetre_jeu.blit(image_canon_pivote, canon_pivote_rect)
    fenetre_jeu.blit(c.IMAGE_ROUE_CANON, (c.POS_X_ROUE_CANON, c.POS_Y_ROUE_CANON))

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
        boulet_canon_rect.x, boulet_canon_rect.y =\
            position_x_boulet + pos_x_centre_bouche_canon - 30, pos_y_centre_bouche_canon - position_y_boulet

        fenetre_jeu.blit(c.IMAGE_BOULET_CANON, boulet_canon_rect)


while en_execution:

    position_souris_x, position_souris_y = pygame.mouse.get_pos()

    if en_jeu:
        actualisation_jeu(position_souris_x, position_souris_y)

    else:
        affichage_accueil(position_souris_x, position_souris_y)

    pygame.display.flip()

    if pygame.mouse.get_pressed()[0]:
        if not en_animation_tir and vitesse_initiale < c.VITESSE_BOULET_MAX and tir_possible:
            vitesse_initiale += 0.83

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

                position_x_tir = position_souris_x
                position_y_tir = position_souris_y
                vitesse_initiale_tir = vitesse_initiale

            else:
                if nombre_clic_en_jeu > 0:
                    tir_possible = True

    pygame.time.Clock().tick(c.IPS)
