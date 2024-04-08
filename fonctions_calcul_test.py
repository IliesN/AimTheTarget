import constantes_test as c
import math
import random
import pygame


def fonction_trajectoire_boulet(x, alpha, v0, g):
    """
    Calcule la trajectoire d'un projectile en fonction de plusieurs paramètres.

    :param x: La distance horizontale parcourue par le projectile.
    :param alpha: L'angle de tir en radians.
    :param v0: La vitesse initiale du projectile.
    :param g: L'accélération gravitationnelle.
    :return: La hauteur atteinte par le projectile à une distance donnée.
    """
    # Calcul de la hauteur de la trajectoire en fonction de la distance horizontale x
    hauteur = (-1 / 2) * g * (x / (v0 * math.cos(alpha))) ** 2 + x * math.tan(alpha)

    return hauteur


def fonction_trajectoire_meteorite(x, composants_meteorite):
    position_x_initiale_meteorite = composants_meteorite["coordonnees_initiales"][0]

    coefficient_directeur_traj = (c.PERSONNAGE_RECT.center[1] - c.POS_Y_METEORITES) / \
                                 (c.PERSONNAGE_RECT.center[0] - position_x_initiale_meteorite)

    # Calculer la trajectoire de chaque meteorite allant de leur position initale vers le centre du personnage
    hauteur = coefficient_directeur_traj * x + c.POS_Y_METEORITES -\
        coefficient_directeur_traj * position_x_initiale_meteorite

    return hauteur


def creer_meteorite(liste_meteorites):
    positions_x_initiales = []
    for composants_meteorite in liste_meteorites:
        positions_x_initiales.append(composants_meteorite["coordonnees_initiales"][0])

    position_x_meteorite = random.choice([
        position_x
        for position_x in range(c.INTERVALLE_POS_X_METEORITES[0], c.INTERVALLE_POS_X_METEORITES[1],
                                c.DIMENSION_METEORITE)
        if position_x not in positions_x_initiales  # Permet de faire apparaître des météorites là où elles ne sont
        # encore jamais apparues
    ])

    meteorite_rect = c.IMAGE_METEORITE.get_rect()
    meteorite_rect.x, meteorite_rect.y = (position_x_meteorite, c.POS_Y_METEORITES)

    collision_meteorite_rect = pygame.Rect(0, 0, c.DIMENSION_METEORITE, c.DIMENSION_METEORITE)
    collision_meteorite_rect.center = meteorite_rect.center

    liste_meteorites.append({
        "coordonnees_initiales": (position_x_meteorite, c.POS_Y_METEORITES),  # Coordonnées initiales, servant à ne pas
        # superposer les meteorites

        "rect_meteorite": meteorite_rect,  # Rect correspondant à la météorite
        "rect_zone_collision": collision_meteorite_rect,  # Rect correspondant à la zone de collision de la météorite

        "coordonnees_actuelles": [position_x_meteorite, c.POS_Y_METEORITES],  # Coordonnées actuelles de la météorite
    }
    )

    return liste_meteorites


def actualiser_pos_meteorite(composants_meteorite):
    nouvelle_pos_x = composants_meteorite["coordonnees_actuelles"][0] + c.VITESSE_METEORITE
    nouvelle_pos_y = int(fonction_trajectoire_meteorite(nouvelle_pos_x, composants_meteorite))

    composants_meteorite["coordonnees_actuelles"] = [nouvelle_pos_x, nouvelle_pos_y]

    meteorite_rect = composants_meteorite["rect_meteorite"]
    meteorite_rect.x, meteorite_rect.y = nouvelle_pos_x, nouvelle_pos_y
    composants_meteorite["rect_meteorite"] = meteorite_rect

    zone_collision_rect = composants_meteorite["rect_zone_collision"]
    zone_collision_rect.center = meteorite_rect.center
    composants_meteorite["rect_zone_collision"] = zone_collision_rect

    return composants_meteorite


def angle_tir_canon(position_x, position_y):
    """
    Calcule l'angle de tir du canon en fonction de la position du joueur.

    :param position_x: La coordonnée x de la position du joueur.
    :param position_y: La coordonnée y de la position du joueur.
    :return: L'angle de tir du canon.
    """
    # Calcul des longueurs des côtés du triangle formé par le joueur et le centre du canon
    longueur_adjacent = position_x - c.POSTION_CENTRE_CANON_SANS_ROUE[0]
    longueur_oppose = c.POSTION_CENTRE_CANON_SANS_ROUE[1] - position_y

    # Calcul de la longueur de l'hypoténuse du triangle
    longueur_hypotenuse = math.sqrt(longueur_adjacent ** 2 + longueur_oppose ** 2)

    # Calcul de l'angle de tir en radians
    angle_tir = math.acos(longueur_adjacent / longueur_hypotenuse)

    # Limite l'angle de tir entre les valeurs minimales et maximales spécifiées
    if angle_tir < c.ANGLE_TIR_MINIMAL:
        angle_tir = c.ANGLE_TIR_MINIMAL
    elif angle_tir > c.ANGLE_TIR_MAXIMAL:
        angle_tir = c.ANGLE_TIR_MAXIMAL

    return angle_tir
