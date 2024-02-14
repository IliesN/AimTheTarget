import pygame


pygame.init()

LARGEUR, HAUTEUR = 1280, 720


# Import de toutes les images
icone_jeu = pygame.image.load("icone_jeu.png")

image_meteorite = pygame.image.load("elements_decor/meteorite.png")
image_boulet_canon = pygame.image.load("elements_decor/boulet_canon.png")
image_roue_canon = pygame.image.load("elements_decor/roue_canon.png")
image_canon_sans_roue = pygame.image.load("elements_decor/canon_sans_roue.png")
image_personnage = pygame.image.load("elements_decor/personnage.png")
image_monstre_1 = pygame.image.load("elements_decor/monstre_1.png")

image_decor_accueil = pygame.image.load("decors/decor_accueil.jpg")

# image_boulet_canon = pygame.image.load("decors/boulet_canon.png")
# image_roue_canon = pygame.image.load("decors/roue_canon.png")
# image_canon_sans_roue = pygame.image.load("decors/canon_sans_roue.png")
# image_personnage = pygame.image.load("decors/personnage.png")
# image_monstre_1 = pygame.image.load("decors/monstre_1.png")
#...


# Modifications des paramètres principaux de la fenêtre
pygame.display.set_caption("Astral Shooter")
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_icon(icone_jeu)


en_execution = True

while en_execution:

    fenetre.blit(image_decor_accueil, (0, 0))



    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            en_execution = False
            pygame.quit()


