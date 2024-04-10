import constantes_test as c
import fonctions_calcul_test as calc
import pygame
import math

# Modifications des paramètres principaux de la fenêtre
pygame.display.set_caption("Astral Shooter")
fenetre_jeu = pygame.display.set_mode((c.LARGEUR_FENETRE, c.HAUTEUR_FENETRE))
pygame.display.set_icon(c.ICONE_JEU)

en_execution = True


def initialiser_variables_jeu(choix_mode_facile=False, choix_niveau_actuel=0, choix_perdu=False, choix_gagne=False,
                              choix_valeur_horodatage=0, choix_victoire=False):
    """
    Initialise les variables du jeu avec les valeurs par défaut ou les valeurs spécifiées en argument.

    :param choix_mode_facile: Indique si le mode facile est activé (bool).
    :param choix_niveau_actuel: Niveau actuel du jeu (int).
    :param choix_perdu: Indique si le joueur a perdu (bool).
    :param choix_gagne: Indique si le joueur a gagné (bool).
    :param choix_valeur_horodatage: Valeur de l'horodatage initial (int).
    :param choix_victoire: Indique si le joueur est en état de victoire (bool).
    """
    # Déclaration des variables globales du jeu
    global position_x_boulet, position_y_boulet
    global position_x_tir, position_y_tir, vitesse_initiale_tir
    global vitesse_initiale, angle_rotation
    global niveau_actuel, coordonnees_animation_impact, nombre_vies_actuel
    global valeur_horodatage_debut, temps_jeu_ecoule, temps_millisecondes
    global en_tir, en_animation_tir, en_explosion, en_pause, en_victoire, en_jeu, en_blessure, nombre_clic_en_jeu
    global mode_facile, tir_possible, regles_affichees, perdu, gagne
    global apparition_meteorite, nombre_meteorites_actuel, liste_meteorites

    # Initialisation des variables du jeu avec les valeurs par défaut ou les valeurs spécifiées
    position_x_boulet = 0
    position_y_boulet = 0

    position_x_tir = 0
    position_y_tir = 0
    vitesse_initiale_tir = 0

    vitesse_initiale = c.VITESSE_BOULET_MIN

    angle_rotation = -c.ANGLE_ROTATION_INITAL

    valeur_horodatage_debut = choix_valeur_horodatage
    coordonnees_animation_impact = 0, 0

    en_tir = False
    en_animation_tir = False

    en_explosion = False
    en_blessure = False

    en_jeu = False
    en_pause = False

    nombre_clic_en_jeu = 0
    tir_possible = False

    mode_facile = choix_mode_facile

    regles_affichees = False

    perdu = choix_perdu
    gagne = choix_gagne

    en_victoire = choix_victoire

    liste_meteorites = []

    temps_jeu_ecoule = 0
    temps_millisecondes = 0

    nombre_meteorites_actuel = 0
    apparition_meteorite = -1

    niveau_actuel = choix_niveau_actuel


def actualisation_jeu(position_x, position_y):
    """
    Actualise l'affichage du jeu en fonction des événements en cours.

    :param position_x: La coordonnée x de la position de la souris (int).
    :param position_y: La coordonnée y de la position de la souris (int).
    :return: None
    """
    # Déclaration des variables globales utilisées dans la fonction
    global position_x_boulet, position_y_boulet
    global position_x_tir, position_y_tir, vitesse_initiale_tir, vitesse_initiale, angle_rotation
    global en_animation_tir, en_explosion, en_victoire, tir_possible, en_blessure, perdu
    global valeur_horodatage_debut, coordonnees_animation_impact
    global nombre_meteorites_actuel, apparition_meteorite, liste_meteorites
    global nombre_vies_actuel, niveau_actuel

    # Affichage du décor du niveau actuel
    fenetre_jeu.blit(c.LISTE_DECORS_NIVEAU[niveau_actuel], (0, 0))

    # Intensité de la pesanteur en fonction du niveau actuel
    intensite_pesanteur = c.INTENSITE_PESANTEUR_NIVEAU[niveau_actuel]

    # Si le nombre de météorites atteint le maximum pour le niveau actuel et il n'y a plus de météorites en jeu
    if nombre_meteorites_actuel == c.NOMBRE_METEORITES_NIVEAU[niveau_actuel] and not liste_meteorites:
        niveau_actuel += 1
        if niveau_actuel == 3:
            initialiser_variables_jeu(choix_gagne=True)
        else:
            initialiser_variables_jeu(choix_mode_facile=mode_facile, choix_niveau_actuel=niveau_actuel,
                                      choix_valeur_horodatage=pygame.time.get_ticks(), choix_victoire=True)

    # Rotation de l'image du canon en fonction de la position de la souris
    image_canon_pivote = pygame.transform.rotate(c.IMAGE_CANON_SANS_ROUE,
                                                 math.degrees(calc.angle_tir_canon(position_x, position_y)))

    # Obtention du rectangle englobant du canon
    canon_pivote_rect = image_canon_pivote.get_rect(center=c.POSTION_CENTRE_CANON_SANS_ROUE)

    # Affichage du nombre de vies restantes
    somme_decalage_coeur = c.POS_X_DERNIER_COEUR

    # Si le temps écoulé est un multiple de 2 et il n'y a pas de météorites apparues à ce moment
    # et le nombre de météorites actuelles est inférieur au nombre maximum de météorites pour le niveau
    if temps_jeu_ecoule % 2 == 0 and apparition_meteorite != temps_jeu_ecoule \
            and nombre_meteorites_actuel < c.NOMBRE_METEORITES_NIVEAU[niveau_actuel]:
        # Création d'une nouvelle météorite
        liste_meteorites = calc.creer_meteorite(liste_meteorites)
        apparition_meteorite = temps_jeu_ecoule
        nombre_meteorites_actuel += 1

    # Détermination du nombre de vies initial en fonction du mode de jeu
    if mode_facile:
        nombre_vies_initial = c.NOMBRE_VIES_INITIAL_MODE_FACILE
    else:
        nombre_vies_initial = c.NOMBRE_VIES_INITIAL_MODE_NORMAL

    # Affichage des coeurs de vies
    for indice_coeur_noir in range(nombre_vies_initial - nombre_vies_actuel):
        fenetre_jeu.blit(c.IMAGE_COEUR_NOIR, (somme_decalage_coeur, c.POS_Y_COEUR))
        somme_decalage_coeur -= c.DECALAGE_COEUR

    for indice_coeur_rouge in range(nombre_vies_actuel):
        fenetre_jeu.blit(c.IMAGE_COEUR_ROUGE, (somme_decalage_coeur, c.POS_Y_COEUR))
        somme_decalage_coeur -= c.DECALAGE_COEUR

    # Affichage du personnage, du canon pivoté et de la roue du canon
    fenetre_jeu.blit(c.IMAGE_PERSONNAGE, c.PERSONNAGE_RECT)
    fenetre_jeu.blit(image_canon_pivote, canon_pivote_rect)
    fenetre_jeu.blit(c.IMAGE_ROUE_CANON, (c.POS_X_ROUE_CANON, c.POS_Y_ROUE_CANON))

    # Affichage de la jauge de tir
    fenetre_jeu.blit(c.IMAGE_JAUGE_TIR, (c.DECALAGE_JAUGE, c.DECALAGE_JAUGE))
    pivoter_fleche_jauge()

    # Boucle de traitement de chaque météorite
    indice_composants_meteorite = 0
    while indice_composants_meteorite < len(liste_meteorites):
        # Actualisation de la position de la météorite
        liste_meteorites[indice_composants_meteorite] = \
            calc.actualiser_pos_meteorite(liste_meteorites[indice_composants_meteorite])
        rect_meteorite_collision = liste_meteorites[indice_composants_meteorite]["rect_zone_collision"]

        # Collision entre la météorite et le personnage
        if rect_meteorite_collision.colliderect(c.PERSONNAGE_RECT):
            # Réduction du nombre de vies
            nombre_vies_actuel -= 1
            coordonnees_animation_impact = liste_meteorites[indice_composants_meteorite]["rect_zone_collision"].center
            valeur_horodatage_debut = pygame.time.get_ticks()
            en_blessure = True

            # Si le joueur n'a plus de vies, il a perdu
            if nombre_vies_actuel == 0:
                initialiser_variables_jeu(choix_mode_facile=mode_facile, choix_perdu=True)
                break  # Sortie de la boucle, car le jeu est terminé
            else:
                # Suppression de la météorite en cas de collision avec le personnage
                del liste_meteorites[indice_composants_meteorite]
        else:
            # Affichage de la météorite si aucune collision n'est détectée
            fenetre_jeu.blit(c.IMAGE_METEORITE, liste_meteorites[indice_composants_meteorite]["rect_meteorite"])
            indice_composants_meteorite += 1

    # Affichage de la trajectoire anticipée en mode facile
    if mode_facile:
        trajectoire_mode_facile(position_x, position_y, intensite_pesanteur)

    # Si une animation de tir est en cours
    if en_animation_tir:
        # Calcul de l'angle de tir
        angle_tir = calc.angle_tir_canon(position_x_tir, position_y_tir)

        # Calcul des coordonnées du centre de la bouche du canon
        pos_x_centre_bouche_canon, pos_y_centre_bouche_canon = \
            c.POSTION_CENTRE_CANON_SANS_ROUE[0] + c.RAYON_CANON_TIR * math.cos(angle_tir), \
            c.POSTION_CENTRE_CANON_SANS_ROUE[1] - c.RAYON_CANON_TIR * math.sin(angle_tir)

        # Calcul de la nouvelle position du boulet
        position_x_boulet += vitesse_initiale_tir // c.DIVISEUR_VITESSE
        position_y_boulet = calc.fonction_trajectoire_boulet(position_x_boulet, angle_tir, vitesse_initiale_tir,
                                                             intensite_pesanteur)

        # Création du rectangle englobant du boulet
        boulet_canon_rect = c.IMAGE_BOULET_CANON.get_rect()
        boulet_canon_rect.center = position_x_boulet + pos_x_centre_bouche_canon - c.DECALAGE_BOULET, \
            pos_y_centre_bouche_canon - position_y_boulet

        # Boucle de traitement de chaque météorite
        indice_composants_meteorite = 0
        while indice_composants_meteorite < len(liste_meteorites):
            # Si le boulet touche une météorite
            if liste_meteorites[indice_composants_meteorite]["rect_zone_collision"].colliderect(boulet_canon_rect):
                del liste_meteorites[indice_composants_meteorite]  # Suppression de la météorite touchée

                # Réinitialisation des paramètres après une collision
                position_x_boulet, position_y_boulet = 0, 0
                position_x_tir, position_y_tir, vitesse_initiale_tir = 0, 0, 0
                vitesse_initiale = c.VITESSE_BOULET_MIN
                angle_rotation = -c.ANGLE_ROTATION_INITAL
                en_animation_tir = False
                en_explosion = True
                coordonnees_animation_impact = boulet_canon_rect.center
                valeur_horodatage_debut = pygame.time.get_ticks()
                break
            else:
                indice_composants_meteorite += 1

        # Si le boulet ne touche pas d'obstacle
        if not (boulet_canon_rect.colliderect(c.SOL_RECT) or boulet_canon_rect.colliderect(c.MUR_RECT) or
                boulet_canon_rect.colliderect(c.PLAFOND_RECT) or boulet_canon_rect.colliderect(c.PERSONNAGE_RECT)):
            fenetre_jeu.blit(c.IMAGE_BOULET_CANON, boulet_canon_rect)  # Affichage du boulet
        else:
            # Réinitialisation des paramètres après une collision
            position_x_boulet, position_y_boulet = 0, 0
            position_x_tir, position_y_tir, vitesse_initiale_tir = 0, 0, 0
            vitesse_initiale = c.VITESSE_BOULET_MIN
            angle_rotation = -c.ANGLE_ROTATION_INITAL
            en_animation_tir = False
            coordonnees_animation_impact = boulet_canon_rect.center
            valeur_horodatage_debut = pygame.time.get_ticks()

            # Si le boulet touche le personnage
            if boulet_canon_rect.colliderect(c.PERSONNAGE_RECT):
                nombre_vies_actuel -= 1
                en_blessure = True

                # Si le joueur n'a plus de vies, il a perdu
                if nombre_vies_actuel == 0:
                    initialiser_variables_jeu(choix_mode_facile=mode_facile, choix_perdu=True)
            else:
                en_explosion = True

        # Si une explosion est en cours
    if en_explosion or en_blessure:
        # Si le temps écoulé depuis le début de l'explosion est inférieur à la durée définie
        if pygame.time.get_ticks() - valeur_horodatage_debut < c.DUREE_EXPLOSION:
            # Affichage de l'explosion
            if en_explosion:
                explosion_rect = c.IMAGE_EXPLOSION.get_rect()
                explosion_rect.center = coordonnees_animation_impact
                fenetre_jeu.blit(c.IMAGE_EXPLOSION, explosion_rect)
            elif en_blessure:
                blessure_rect = c.IMAGE_BLESSURE.get_rect()
                blessure_rect.center = (coordonnees_animation_impact[0] - c.RECUL_BLESSURE,
                                        coordonnees_animation_impact[1])
                fenetre_jeu.blit(c.IMAGE_BLESSURE, blessure_rect)
        else:
            # Fin de l'explosion
            if en_explosion:
                en_explosion = False
            elif en_blessure:
                en_blessure = False
            valeur_horodatage_debut = 0


def affichage_menu_perdu(position_x, position_y):
    """
    Affiche le menu de fin de partie lorsque le joueur a perdu.

    :param position_x: La coordonnée x de la position de la souris (int).
    :param position_y: La coordonnée y de la position de la souris (int).
    :return: None
    """
    # Affichage du fond du menu
    fenetre_jeu.blit(c.IMAGE_FOND_MENUS, (0, 0))

    # Affichage du texte "Échouage" et du texte "Réessayer"
    fenetre_jeu.blit(c.IMAGE_TEXTE_ECHOUAGE, c.TEXTE_ECHOUAGE_RECT)
    fenetre_jeu.blit(c.IMAGE_TEXTE_REESSAYER, c.TEXTE_RESSAYER_RECT)

    # Vérification si la souris survole le bouton "Réessayer"
    if c.BOUTON_REESSAYER_RECT.topleft[0] < position_x < c.BOUTON_REESSAYER_RECT.topleft[0] + c.LARGEUR_BOUTON_MENU \
            and c.BOUTON_REESSAYER_RECT.topleft[1] < position_y < c.BOUTON_REESSAYER_RECT.topleft[1] + \
            c.HAUTEUR_BOUTON_MENU:
        fenetre_jeu.blit(c.IMAGE_BOUTON_REESSAYER_EFFET, c.BOUTON_REESSAYER_RECT)  # Affichage du bouton avec effet
    else:
        fenetre_jeu.blit(c.IMAGE_BOUTON_REESSAYER, c.BOUTON_REESSAYER_RECT)  # Affichage du bouton sans effet

    # Vérification si la souris survole le bouton "Retour au menu principal"
    if c.BOUTON_RETOUR_ACC_PERDU_RECT.topleft[0] < position_x < c.BOUTON_RETOUR_ACC_PERDU_RECT.topleft[0] + \
        c.LARGEUR_BOUTON_MENU and c.BOUTON_RETOUR_ACC_PERDU_RECT.topleft[1] < position_y \
            < c.BOUTON_RETOUR_ACC_PERDU_RECT.topleft[1] + c.HAUTEUR_BOUTON_MENU:
        # Affichage du bouton avec effet
        fenetre_jeu.blit(c.IMAGE_BOUTON_RETOUR_ACC_EFFET, c.BOUTON_RETOUR_ACC_PERDU_RECT)
    else:
        fenetre_jeu.blit(c.IMAGE_BOUTON_RETOUR_ACC, c.BOUTON_RETOUR_ACC_PERDU_RECT)  # Affichage du bouton sans effet


def affichage_gagne(position_x, position_y):
    """
    Affiche le menu de victoire lorsque le joueur a gagné.

    :param position_x: La coordonnée x de la position de la souris (int).
    :param position_y: La coordonnée y de la position de la souris (int).
    :return: None
    """
    # Affichage du fond du menu
    fenetre_jeu.blit(c.IMAGE_FOND_MENUS, (0, 0))

    # Affichage du texte "Gagné"
    fenetre_jeu.blit(c.IMAGE_TEXTE_GAGNE, c.TEXTE_GAGNE_RECT)

    # Vérification si la souris survole le bouton "Retour au menu principal"
    if c.BOUTON_RETOUR_ACC_GAGNE_RECT.topleft[0] < position_x < c.BOUTON_RETOUR_ACC_GAGNE_RECT.topleft[0] + \
        c.LARGEUR_BOUTON_MENU and c.BOUTON_RETOUR_ACC_GAGNE_RECT.topleft[1] < position_y \
            < c.BOUTON_RETOUR_ACC_PERDU_RECT.topleft[1] + c.HAUTEUR_BOUTON_MENU:
        # Affichage du bouton avec effet
        fenetre_jeu.blit(c.IMAGE_BOUTON_RETOUR_ACC_EFFET, c.BOUTON_RETOUR_ACC_GAGNE_RECT)
    else:
        fenetre_jeu.blit(c.IMAGE_BOUTON_RETOUR_ACC, c.BOUTON_RETOUR_ACC_GAGNE_RECT)  # Affichage du bouton sans effet


def affichage_ecran_niveau_suivant():
    """
    Affiche l'écran annonçant le passage au niveau suivant.

    :return: None
    """
    # Affichage du fond de l'écran
    fenetre_jeu.blit(c.IMAGE_FOND_MENUS, (0, 0))

    # Affichage du texte "Niveau Suivant"
    fenetre_jeu.blit(c.IMAGE_TEXTE_NIVEAU_SUIVANT, c.TEXTE_NIVEAU_SUIVANT_RECT)


def affichage_pause():
    """
    Affiche l'écran de pause avec les options disponibles.

    :return: None
    """
    # Affichage du fond de l'écran de pause
    fenetre_jeu.blit(c.IMAGE_FOND_PAUSE, (0, 0))

    # Affichage des options de menu de pause
    for indice_ligne_pause in range(len(c.TEXTE_MENU_PAUSE)):
        # Affichage de chaque ligne de texte avec un espacement
        fenetre_jeu.blit(c.POLICE_TEXTE_MENU_PAUSE.render(c.TEXTE_MENU_PAUSE[indice_ligne_pause],
                                                          True, "white"),
                         (c.COORDONNEES_TEXTE_PAUSE[0], c.COORDONNEES_TEXTE_PAUSE[1] +
                          (c.HAUTEUR_TEXTE_MENU_PAUSE + 7) * indice_ligne_pause))


def affichage_accueil(position_x, position_y):
    """
    Affiche l'écran d'accueil du jeu.

    :param position_x: La coordonnée x de la position de la souris (int).
    :param position_y: La coordonnée y de la position de la souris (int).
    :return: None
    """
    global mode_facile  # Utilisation de la variable globale mode_facile

    # Affichage des éléments de l'écran d'accueil
    fenetre_jeu.blit(c.IMAGE_DECOR_ACCUEIL, (0, 0))  # Affichage du fond d'écran
    fenetre_jeu.blit(c.IMAGE_TEXTE_NOM_JEU, c.TEXTE_NOM_JEU_RECT)  # Affichage du texte du nom du jeu
    fenetre_jeu.blit(c.IMAGE_TEXTE_CLIQUEZ, c.TEXTE_CLIQUEZ_RECT)  # Affichage du texte "cliquez"

    if not regles_affichees:  # Si les règles ne sont pas affichées
        # Affichage du mode de jeu (facile ou normal) avec le texte et l'encoche associés
        if mode_facile:  # Si le mode de jeu est facile
            # Affichage de l'encoche verte
            fenetre_jeu.blit(c.IMAGE_ENCOCHE_VERTE, (c.ENCOCHE_RECT.x, c.ENCOCHE_RECT.y))
            fenetre_jeu.blit(c.IMAGE_TEXTE_MODE_ON, c.TEXTE_MODE_FACILE_RECT)  # Affichage du texte "facile"
        else:
            fenetre_jeu.blit(c.IMAGE_TEXTE_MODE_OFF, c.TEXTE_MODE_FACILE_RECT)  # Affichage du texte "normal"

        # Affichage de l'encoche et du bouton de jouer avec effet au survol de la souris
        if c.ENCOCHE_RECT.topleft[0] < position_x < c.ENCOCHE_RECT.topleft[0] + c.LARGEUR_ENCOCHE \
                and c.ENCOCHE_RECT.topleft[1] < position_y < c.ENCOCHE_RECT.topleft[1] + c.HAUTEUR_ENCOCHE:
            fenetre_jeu.blit(c.IMAGE_CASE_ENCOCHE_EFFET, c.ENCOCHE_EFFET_RECT)  # Affichage de l'encoche avec effet
        else:
            fenetre_jeu.blit(c.IMAGE_CASE_ENCOCHE, c.ENCOCHE_RECT)  # Affichage de l'encoche sans effet

        # Affichage du bouton jouer avec effet au survol de la souris
        if c.BOUTON_JOUER_RECT.topleft[0] < position_x < c.BOUTON_JOUER_RECT.topleft[0] + c.DIMENSION_IMAGE_BOUTON \
                and c.BOUTON_JOUER_RECT.topleft[1] < position_y < c.BOUTON_JOUER_RECT.topleft[1] + \
                c.DIMENSION_IMAGE_BOUTON:
            fenetre_jeu.blit(c.IMAGE_EFFET_BOUTON, c.EFFET_BOUTON_RECT)  # Affichage du bouton avec effet
        else:
            fenetre_jeu.blit(c.IMAGE_BOUTON_JOUER, c.BOUTON_JOUER_RECT)  # Affichage du bouton sans effet

        # Affichage du bouton pour afficher les règles avec effet au survol de la souris
        if c.REGLES_RECT.topleft[0] < position_x < c.REGLES_RECT.topleft[0] + c.DIMENSION_IMAGE_REGLES \
                and c.REGLES_RECT.topleft[1] < position_y < c.REGLES_RECT.topleft[1] + c.DIMENSION_IMAGE_REGLES:
            fenetre_jeu.blit(c.IMAGE_REGLES_EFFET, c.REGLES_RECT)  # Affichage du bouton avec effet
        else:
            fenetre_jeu.blit(c.IMAGE_REGLES, c.REGLES_RECT)  # Affichage du bouton sans effet

    else:  # Si les règles sont affichées
        pygame.draw.rect(fenetre_jeu, "white", c.SURFACE_REGLES_RECT)  # Affichage de la surface pour les règles
        pygame.draw.rect(fenetre_jeu, "black", c.SURFACE_REGLES_RECT, 3)  # Contour de la surface pour les règles

        # Affichage des règles
        for indice_ligne_regles in range(len(c.TEXTE_REGLES)):
            fenetre_jeu.blit(c.POLICE_TEXTE_REGLES.render(c.TEXTE_REGLES[indice_ligne_regles], True, "black"),
                             (c.COORDONNEES_TEXTE_REGLES[0],
                              c.COORDONNEES_TEXTE_REGLES[1] + (c.HAUTEUR_TEXTE_REGLES + 3) * indice_ligne_regles))

            # Affichage du bouton pour fermer les règles avec effet au survol de la souris
        if c.CROIX_RECT.topleft[0] < position_x < c.CROIX_RECT.topleft[0] + c.DIMENSION_CROIX_ROUGE \
                and c.CROIX_RECT.topleft[1] < position_y < c.CROIX_RECT.topleft[1] + c.DIMENSION_CROIX_ROUGE:
            fenetre_jeu.blit(c.IMAGE_CROIX_EFFET, c.CROIX_EFFET_RECT)  # Affichage de la croix avec effet
        else:
            fenetre_jeu.blit(c.IMAGE_CROIX, c.CROIX_RECT)  # Affichage de la croix sans effet


def trajectoire_mode_facile(position_x, position_y, intensite_pesanteur):
    """
    Affiche la trajectoire anticipée du boulet en mode facile.

    :param position_x: La coordonnée x de la position du joueur.
    :param position_y: La coordonnée y de la position du joueur.
    :param intensite_pesanteur: Intensité de pesanteur
    :return: None
    """
    # Si un tir est en cours
    if en_tir:
        # Calcul de l'angle de tir
        angle_tir = calc.angle_tir_canon(position_x, position_y)

        # Calcul des coordonnées du centre de la bouche du canon
        pos_x_centre_bouche_canon, pos_y_centre_bouche_canon = \
            c.POSTION_CENTRE_CANON_SANS_ROUE[0] + c.RAYON_CANON_TIR * math.cos(angle_tir), \
            c.POSTION_CENTRE_CANON_SANS_ROUE[1] - c.RAYON_CANON_TIR * math.sin(angle_tir)

        # Pour chaque marqueur de trajectoire
        for position_x_marqueur in range(c.POS_DEBUT_MARQUEUR_TRAJ, c.POS_FIN_MARQUEUR_TRAJ, c.AJOUT_POS_MARQUEUR_TRAJ):
            # Calcul de la position en y du marqueur de trajectoire
            position_y_marqueur = calc.fonction_trajectoire_boulet(position_x_marqueur, angle_tir, vitesse_initiale,
                                                                   intensite_pesanteur)

            # Dessin du marqueur de trajectoire
            pygame.draw.circle(fenetre_jeu, "yellow", (position_x_marqueur + pos_x_centre_bouche_canon,
                                                       pos_y_centre_bouche_canon - position_y_marqueur),
                               c.LARGEUR_MARQUEUR_TRAJECTOIRE)

            # Dessin du contour du marqueur de trajectoire
            pygame.draw.circle(fenetre_jeu, "black", (position_x_marqueur + pos_x_centre_bouche_canon,
                                                      pos_y_centre_bouche_canon - position_y_marqueur),
                               c.LARGEUR_MARQUEUR_TRAJECTOIRE, 1)


def pivoter_fleche_jauge():
    """
    Pivoter la flèche de la jauge de tir.

    :return: None
    """
    global angle_rotation

    # Si le jeu n'est pas en animation de tir
    if not en_animation_tir:
        # Si le joueur tire et l'angle de rotation est inférieur au maximum autorisé
        if en_tir and angle_rotation >= -c.ANGLE_ROTATION_MAXIMAL:
            # Calcul de l'angle de rotation en fonction de la vitesse du boulet
            angle_rotation -= (c.ANGLE_ROTATION_MAXIMAL - c.ANGLE_ROTATION_INITAL) * c.INCREMENTATION_VITESSE / \
                              (c.VITESSE_BOULET_MAX - c.VITESSE_BOULET_MIN)
    # Si le jeu est en animation de tir
    else:
        # Si l'angle de rotation est inférieur à l'angle limite de diminution
        if angle_rotation < c.ANGLE_LIMITE_DIMINUTION:
            # Diminution de l'angle de rotation
            angle_rotation += c.DIMINUTION_FLECHE_JAUGE
        else:
            # Réinitialisation de l'angle de rotation
            angle_rotation = -c.ANGLE_ROTATION_INITAL

    # Rotation de l'image de la flèche
    image_fleche_pivote = pygame.transform.rotate(c.IMAGE_FLECHE_JAUGE, angle_rotation)
    fleche_pivote_rect = image_fleche_pivote.get_rect(center=c.POSITION_CENTRE_FLECHE_JAUGE)

    # Affichage de la flèche pivotée sur la fenêtre de jeu
    fenetre_jeu.blit(image_fleche_pivote, fleche_pivote_rect)


initialiser_variables_jeu()  # Initialisation des variables nécessaires au bon fonctionnement du jeu

while en_execution:
    # Obtention des coordonnées de la souris
    position_souris_x, position_souris_y = pygame.mouse.get_pos()

    # Si le jeu est en cours
    if en_jeu:
        # Si le jeu n'est pas en pause
        if not en_pause:
            # Comptabilisation du temps écoulé pour le jeu
            temps_millisecondes += int(1000 / c.IMAGES_PAR_SECONDE)
            if temps_millisecondes > 1000:
                temps_jeu_ecoule += 1
                temps_millisecondes = 0

            # Actualisation du jeu en fonction des coordonnées de la souris
            actualisation_jeu(position_souris_x, position_souris_y)

    # Si le jeu n'est pas en cours et que le joueur a perdu
    elif perdu:
        # Affichage du menu de perte en fonction des coordonnées de la souris
        affichage_menu_perdu(position_souris_x, position_souris_y)

    # Si le joueur a gagné
    elif en_victoire:
        # Affichage de l'écran de passage au niveau suivant
        affichage_ecran_niveau_suivant()
        # Si le délai est écoulé, passer au niveau suivant
        if pygame.time.get_ticks() - valeur_horodatage_debut >= c.DELAI_NIVEAU_SUIVANT:
            en_victoire = False
            en_jeu = True
            valeur_horodatage_debut = 0
            nombre_clic_en_jeu = 1
            tir_possible = True

    # Si le joueur a gagné
    elif gagne:
        # Affichage de l'écran de victoire en fonction des coordonnées de la souris
        affichage_gagne(position_souris_x, position_souris_y)

    else:
        # Affichage de l'écran d'accueil en fonction des coordonnées de la souris
        affichage_accueil(position_souris_x, position_souris_y)

    # Si le bouton gauche de la souris est enfoncé
    if pygame.mouse.get_pressed()[0]:
        # Si le jeu n'est pas en animation de tir et que la vitesse initiale est inférieure à la
        # vitesse maximale et qu'un tir est possible
        if not en_animation_tir and vitesse_initiale < c.VITESSE_BOULET_MAX and tir_possible:
            # Activer le tir
            en_tir = True
            # Incrémenter la vitesse initiale du boulet
            vitesse_initiale += c.INCREMENTATION_VITESSE

    # Mettre à jour l'affichage
    pygame.display.flip()

    # Gérer les événements pygame
    for event in pygame.event.get():
        # Si l'événement est de fermer la fenêtre
        if event.type == pygame.QUIT:
            # Mettre fin à l'exécution du jeu
            en_execution = False
            pygame.quit()

        # Si un bouton de la souris est enfoncé
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Si le jeu n'est pas en cours
            if not en_jeu and not perdu and not en_victoire and not gagne:
                if not regles_affichees:
                    # Si le bouton "Jouer" est cliqué
                    if c.BOUTON_JOUER_RECT.collidepoint(event.pos):
                        # Commencer le jeu
                        en_jeu = True

                        if mode_facile:
                            nombre_vies_actuel = c.NOMBRE_VIES_INITIAL_MODE_FACILE
                        else:
                            nombre_vies_actuel = c.NOMBRE_VIES_INITIAL_MODE_NORMAL
                    # Si la case d'encoche pour le mode facile est cliquée
                    elif c.ENCOCHE_RECT.collidepoint(event.pos) or c.TEXTE_MODE_FACILE_RECT.collidepoint(event.pos):
                        # Inverser le mode de difficulté
                        mode_facile = not mode_facile

                    elif c.REGLES_RECT.collidepoint(event.pos):
                        regles_affichees = True

                elif c.CROIX_RECT.collidepoint(event.pos):
                    regles_affichees = False

            # Si le joueur a perdu
            elif perdu:
                # Si le bouton "Retour à l'accueil" est cliqué
                if c.BOUTON_RETOUR_ACC_PERDU_RECT.collidepoint(event.pos):
                    perdu = False
                # Si le bouton "Réessayer" est cliqué
                elif c.BOUTON_REESSAYER_RECT.collidepoint(event.pos):
                    en_jeu = True

                    if mode_facile:
                        nombre_vies_actuel = c.NOMBRE_VIES_INITIAL_MODE_FACILE
                    else:
                        nombre_vies_actuel = c.NOMBRE_VIES_INITIAL_MODE_NORMAL

                    perdu = False

                    # Si le joueur a gagné
                elif gagne:
                    # Si le bouton "Retour à l'accueil" est cliqué
                    if c.BOUTON_RETOUR_ACC_GAGNE_RECT.collidepoint(event.pos):
                        initialiser_variables_jeu()

        # Si un bouton de la souris est relâché et le jeu est en cours
        elif en_jeu and event.type == pygame.MOUSEBUTTONUP:
            # Incrémenter le nombre de clics en jeu
            nombre_clic_en_jeu += 1

            # Si un tir est possible et le jeu n'est pas en animation de tir
            if tir_possible and not en_animation_tir:
                # Début de l'animation de tir
                en_animation_tir = True
                en_tir = False

                # Enregistrer les coordonnées de tir et la vitesse initiale du tir
                position_x_tir, position_y_tir = position_souris_x, position_souris_y
                vitesse_initiale_tir = vitesse_initiale * c.MULTIPLICATEUR_VITESSE
            else:
                # Si le nombre de clics en jeu est supérieur à 0, un tir est possible
                if nombre_clic_en_jeu > 0:
                    tir_possible = True

        # Si une touche du clavier est enfoncée
        elif en_jeu and event.type == pygame.KEYDOWN:

            # Si la touche enfoncée est "Entrée", mettre le jeu en pause ou le reprendre
            if event.key == pygame.K_RETURN:
                en_pause = not en_pause

                if en_pause:
                    affichage_pause()

            # Si le jeu est en pause et la touche "Échap" est enfoncée, réinitialiser les variables du jeu
            elif en_pause and event.key == pygame.K_ESCAPE:
                initialiser_variables_jeu(choix_mode_facile=mode_facile)

    # Régler le nombre d'images par seconde
    pygame.time.Clock().tick(c.IMAGES_PAR_SECONDE)
