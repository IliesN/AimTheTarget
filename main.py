import pygame


pygame.init()

LARGEUR_FENETRE, HAUTEUR_FENETRE = 1280, 500


# Import de toutes les images
icone_jeu = pygame.image.load("icone_jeu.png")

image_meteorite = pygame.image.load("elements_decor/meteorite.png")
image_boulet_canon = pygame.image.load("elements_decor/boulet_canon.png")
image_roue_canon = pygame.image.load("elements_decor/roue_canon.png")
image_canon_sans_roue = pygame.image.load("elements_decor/canon_sans_roue.png")
image_personnage = pygame.image.load("elements_decor/personnage.png")
image_monstre_1 = pygame.image.load("elements_decor/monstre_1.png")

image_decor_accueil = pygame.image.load("decors/decor_accueil.jpg")

image_effet_bouton = pygame.image.load("effet_bouton.png")
DIMENSION_EFFET_BOUTON = 175
Y_EFFET_BT_SUPP = 10

image_bouton_jouer = pygame.image.load("bouton_jouer.png")
bouton_jouer_rect = image_bouton_jouer.get_rect()
DIMENSION_BOUTON = 150
Y_BT_SUPP = 35
bouton_jouer_rect.x = LARGEUR_FENETRE / 2 - DIMENSION_BOUTON / 2
bouton_jouer_rect.y = HAUTEUR_FENETRE / 2 + Y_BT_SUPP

image_fond_terre = pygame.image.load("decors/decor_type_terre.jpg")
# image_roue_canon = pygame.image.load("decors/roue_canon.png")
# image_canon_sans_roue = pygame.image.load("decors/canon_sans_roue.png")
# image_personnage = pygame.image.load("decors/personnage.png")
# image_monstre_1 = pygame.image.load("decors/monstre_1.png")
#...


# Modifications des paramètres principaux de la fenêtre
pygame.display.set_caption("Astral Shooter")
fenetre_jeu = pygame.display.set_mode((LARGEUR_FENETRE, HAUTEUR_FENETRE))
pygame.display.set_icon(icone_jeu)


en_execution = True
en_jeu = False


def actualisation(fenetre):
    fenetre.blit(image_fond_terre, (0, 0))



while en_execution:

    souris_x, souris_y = pygame.mouse.get_pos()

    if en_jeu:
        actualisation(fenetre_jeu)

    else:
        fenetre_jeu.blit(image_decor_accueil, (0, 0))
        fenetre_jeu.blit(image_bouton_jouer, bouton_jouer_rect)

        if LARGEUR_FENETRE / 2 - DIMENSION_EFFET_BOUTON / 2 < souris_x < LARGEUR_FENETRE / 2 - DIMENSION_EFFET_BOUTON /\
                2 + DIMENSION_EFFET_BOUTON and HAUTEUR_FENETRE / 2 + Y_BT_SUPP < souris_y < HAUTEUR_FENETRE / 2 +\
                Y_BT_SUPP + DIMENSION_EFFET_BOUTON:
            fenetre_jeu.blit(image_effet_bouton,
                             (LARGEUR_FENETRE / 2 - DIMENSION_EFFET_BOUTON / 2, HAUTEUR_FENETRE / 2 +
                              Y_BT_SUPP - Y_EFFET_BT_SUPP))
        else:
            fenetre_jeu.blit(image_effet_bouton, (LARGEUR_FENETRE / 2 - DIMENSION_EFFET_BOUTON / 2, HAUTEUR_FENETRE))

    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            en_execution = False
            pygame.quit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if bouton_jouer_rect.collidepoint(event.pos):
                en_jeu = True

