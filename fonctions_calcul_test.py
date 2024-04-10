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
    """
    Calcule la hauteur à laquelle se trouve une météorite à une position x donnée sur l'écran.

    :param x: Position horizontale sur l'écran où la hauteur de la météorite est calculée (float).
    :param composants_meteorite: Dictionnaire contenant les composants de la météorite, notamment ses coordonnées initiales (dict).

    :return: Hauteur de la météorite à la position x spécifiée (float).
    """
    # Récupération de la position initiale en x de la météorite depuis le dictionnaire de composants
    position_x_initiale_meteorite = composants_meteorite["coordonnees_initiales"][0]

    # Calcul du coefficient directeur de la trajectoire, basé sur la position initiale de la météorite et du personnage
    coefficient_directeur_traj = (c.PERSONNAGE_RECT.center[1] - c.POS_Y_METEORITES) / \
                                 (c.PERSONNAGE_RECT.center[0] - position_x_initiale_meteorite)

    # Calcul de la hauteur à laquelle la météorite se trouve à une position donnée 'x' sur l'écran
    hauteur = coefficient_directeur_traj * x + c.POS_Y_METEORITES -\
        coefficient_directeur_traj * position_x_initiale_meteorite

    return hauteur


def creer_meteorite(liste_meteorites):
    """
    Crée une nouvelle météorite et l'ajoute à la liste des météorites existantes.

    :param liste_meteorites: Liste des météorites existantes (list).
    :return: Liste mise à jour des météorites, avec la nouvelle météorite ajoutée (list).
    """
    # Obtention des positions initiales en x de toutes les météorites existantes
    positions_x_initiales = []
    for composants_meteorite in liste_meteorites:
        positions_x_initiales.append(composants_meteorite["coordonnees_initiales"][0])

    # Choix d'une position initiale x pour la nouvelle météorite, en évitant les positions déjà occupées
    position_x_meteorite = random.choice([
        position_x
        for position_x in range(c.INTERVALLE_POS_X_METEORITES[0], c.INTERVALLE_POS_X_METEORITES[1],
                                c.DIMENSION_METEORITE)
        if position_x not in positions_x_initiales
    ])

    # Création du rectangle pour la nouvelle météorite
    meteorite_rect = c.IMAGE_METEORITE.get_rect()
    meteorite_rect.x, meteorite_rect.y = (position_x_meteorite, c.POS_Y_METEORITES)

    # Création du rectangle de collision pour la nouvelle météorite
    collision_meteorite_rect = pygame.Rect(0, 0, c.DIMENSION_METEORITE, c.DIMENSION_METEORITE)
    collision_meteorite_rect.center = meteorite_rect.center

    # Ajout des informations de la nouvelle météorite à la liste des météorites
    liste_meteorites.append({
        "coordonnees_initiales": (position_x_meteorite, c.POS_Y_METEORITES),
        "rect_meteorite": meteorite_rect,
        "rect_zone_collision": collision_meteorite_rect,
        "coordonnees_actuelles": [position_x_meteorite, c.POS_Y_METEORITES],
    })

    return liste_meteorites


def actualiser_pos_meteorite(composants_meteorite):
    """
    Actualise la position de la météorite en fonction de sa trajectoire.

    :param composants_meteorite: Dictionnaire contenant les composants de la météorite à actualiser (dict).
    :return: Dictionnaire des composants de la météorite avec les positions actualisées (dict).
    """
    # Calcul des nouvelles positions x et y en fonction de la vitesse de déplacement de la météorite
    nouvelle_pos_x = composants_meteorite["coordonnees_actuelles"][0] + c.VITESSE_METEORITE
    nouvelle_pos_y = int(fonction_trajectoire_meteorite(nouvelle_pos_x, composants_meteorite))

    # Mise à jour des coordonnées actuelles de la météorite
    composants_meteorite["coordonnees_actuelles"] = [nouvelle_pos_x, nouvelle_pos_y]

    # Mise à jour du rectangle de la météorite avec les nouvelles positions
    meteorite_rect = composants_meteorite["rect_meteorite"]
    meteorite_rect.x, meteorite_rect.y = nouvelle_pos_x, nouvelle_pos_y
    composants_meteorite["rect_meteorite"] = meteorite_rect

    # Mise à jour du rectangle de collision de la météorite avec les nouvelles positions
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
