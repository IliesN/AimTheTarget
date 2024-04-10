RADOUANE Ismaël, NASR Ilies, PELPOIR Justin, BROSSET Mael, PINTO RIBEIRO Clément

Le dossier contient :
- Un fichier README.txt (vous êtes en train de le lire)
- Un répertoire "image", contenant l'ensemble des images utilisées par le jeu
- Deux fichiers "meilleur_score_facile.txt" et "meilleur_score_normal.txt", contenant (ou non) les meilleurs scores atteint par le joueur dans le mode facile et le mode normal
- Plusieurs fichiers Python :
     ~ "main.py", fichier principal du projet, chargé de l'affichage du jeu et de son actualisation
     ~ "cosntantes.py", contenant l'ensemble des constantes définies pour le jeu
     ~ "fonctions_calcul.py", contenant toutes les fonctions de "calcul", telles que celles des trajectoires

Notice d'utilisation :

Les fichiers nécessaires à la bonne exécution du programme sont :
- Le répertoire "images" contenant toutes les images en son intégralité
- Les fichiers Python "main.py", "cosntantes.py", "fonctions_calcul.py"

Pour lancer le jeu, exécutez le fichier Python "main.py".
Voici les explications du jeu:
Le jeu s'intitule "Astral Shooter" et tourne autour des planètes. Le joueur contrôle l'angle de tir d'un canon avec le déplacement de la souris, et la puissance de tir avec la durée d'enfoncement du clic (relâcher pour tirer), et doit détruire les météorites pour protéger l'individu.
Lorsque l'individu reçoit un boulet de canon ou une météorite, il perd une vie; il ne faut surtout pas toutes les perdres !
Le menu principal permet d'activer le mode facile qui augmente le nombre de vie et qui affiche une pré-visualisation de la trajectoire de tir.
Le joueur peut, à tout moment, mettre le jeu en pause en appuyant sur la touche Entrée, et revenir en jeu en ré-appuyant sur cette touche (ou la touche Échap pour quitter)
Un score (correspondant aux millisecondes durant lesquelles le joueur a survécu) augmente et indique l'avancée du joueur; essayez d'atteindre la plus haute valeur possible !
Pour que le meilleur score soit sauvegardé, assurez-vous d'être retourné au menu principal (ou d'avoir perdu) avant de quitter le jeu.
Le jeu se décompose en 3 parties :
    - La première planète sur lequel le joueur apparaît a une gravité semblable à celle sur Terre
    - La deuxième planète a une gravité semblable à celle sur Lune
    - La troisième planète a une gravité semblable à celle de Jupiter; il faut survivre le plus longtemps possible !
