import constantes as c
import math


def fonction_trajectoire(x, alpha, v0, g):
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


def en_collision_boulet(boulet_canon_rect):
    """
    Vérifie si un boulet canon est en collision avec des éléments du jeu.

    :param boulet_canon_rect: Le rectangle représentant le boulet canon.
    :return: True si le boulet canon est en collision avec le sol, un mur ou le personnage, False sinon.
    """
    # Vérifie si le boulet canon est en collision avec le sol, un mur ou le personnage
    return (boulet_canon_rect.colliderect(c.SOL_RECT) or boulet_canon_rect.colliderect(c.MUR_RECT) or
            boulet_canon_rect.colliderect(c.PERSONNAGE_RECT))
