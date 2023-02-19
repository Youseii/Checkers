class Damier:
    def __init__(self):
        # 0 = case vide; 1 = pion blanc; 2 = pion noir
        self.damier = [[0, 2, 0, 2, 0, 2, 0, 2, 0, 2],
                       [2, 0, 2, 0, 2, 0, 2, 0, 2, 0],
                       [0, 2, 0, 2, 0, 2, 0, 2, 0, 2],
                       [2, 0, 2, 0, 2, 0, 2, 0, 2, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                       [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                       [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                       [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
                       ]
        # Initialisation des variables pour designer qui commence en premier et d'autoriser/restreindre certains mouvements pendant le tour de chacun
        self.joueur_blanc = True
        self.joueur_noir = False
        # Variable nb de pions pour chaque joueurs
        self.nb_pionBlanc = 20
        self.nb_pionNoir = 20
        
        self.check_dame = False
        self.debug = 0
    
    # Methode de tour pour les joueurs
    def white_player(self):
        print("\n\t\tVous êtes le joueur 1 avec les pions blanc (1)\n\
                 Le damier commence index 0 jusqu'à l'index 9")
        i, j = input("\nQuel pion voulez-vous déplacer ? Rentré la position ligne colonne (exemple: 6 1 mettre l'espace entre les deux valeurs)\nchoix: ").split()

        return int(i), int(j)

    def black_player(self):
        print("\n\t\tVous êtes le joueur 2 avec les pions noir (2)\n\
                Le damier commence index 0 jusqu'à l'index 9")
        i, j = input("\nQuel pion voulez-vous déplacer ? Rentré la position ligne colonne (exemple: 6 1 mettre l'espace entre les deux valeurs)\nchoix :").split()

        return int(i), int(j)

    # Methode principal de jeu 
    def maingame(self, damier):
        # var pour la boucle while
        fonc = True
        # compteur pour faire une fin de jeu au bout de 2000tours
        cpt = 0
        while fonc:
            if self.joueur_blanc and self.joueur_noir == False:
                reponse_joueur = Damier.white_player(self)
            elif self.joueur_noir and self.joueur_blanc == False:
                reponse_joueur = Damier.black_player(self)
 
            global i, j
            i, j = reponse_joueur
            
            # Pour le changement en dame et ces deplacements
            self.dames()
            
            # damier[i][j] ; i represente les lignes, j les colonnes 
            # Si la case est vide 
            if damier[i][j] == 0:
                print("Vous avez selectionné une case vide !")
            
            # ------------------------------------------------------------------------
            #                   DAME BLANC MOUVEMENT
            # ------------------------------------------------------------------------
            if self.check_dame == True and self.damier[i][j] == 3:
                if self.joueur_blanc == True:
                    self.debug = 0
                try:
                    # variable de test
                    limit = 0
                    print("\nPossibilitées: \n")
                    # On verifie la case diagonale haut gauche s'il y a un pion adversaire
                    if damier[i-1][j-1] == 0:
                        # Vérifie la position du point pour le déplacer dans la diagonale haut gauche 
                        print(f"(1) Dame Blanche en position {i},{j} peut avancer en diagonale haut GAUCHE et donc aller en position {i-1}, {j-1}")
                        self.limit_check(i-1, j-1)
                    elif damier[i-1][j-1] == 2 and damier[i-2][j-2] == 0:
                        print(f"(2) Vous pouvez manger le pion diago haut GAUCHE et donc aller en position {i-2}, {j-2}")
                        self.limit_check(i-2, j-2)
                    else:
                        print("\nDame Blanche ne peux se deplacer en diagonale haut gauche\n")
                        limit = 1
                except IndexError:
                    print("\nVous sortez du damier, mouvement impossible\n")
                    limit = 2
                cpt += 1
 
                try:
                    limit = 0
                    # On repete les meme actions pour les cases tout autour
                    # self.damier[i-1][j+1] represente diago en haut a droite
                    if damier[i-1][j+1] == 0:
                        print(f"(3) Dame Blanche en position {i},{j} peut avancer en diagonale haut DROITE et donc aller en position {i-1}, {j+1}")
                        self.limit_check(i-1, j+1)
                    elif damier[i-1][j+1] == 2 and damier[i-2][j+2] == 0:
                        print(f"(4) Vous pouvez manger le pion diago haut DROITE et donc aller en position {i-2}, {j+2}")
                        self.limit_check(i-2, j+2)
                    else:
                        print("\nDame Blanche ne peux se deplacer en diagonale haut droite\n")
                        limit = 1
                except IndexError:
                    print("\nVous sortez du damier, mouvement impossible\n")
                    limit = 2

                try:
                    limit = 0
                    if damier[i+1][j-1] == 0:
                        print(f"(5) Dame Blanche en position {i},{j} peut avancer en diagonale bas GAUCHE et donc aller en position {i+1}, {j-1}")
                        # Vérification du postionnement
                        self.limit_check(i+1, j-1)
                        limit = 0
                    elif damier[i+1][j-1] == 1 and damier[i+2][j-2] == 0:
                        print(f"(6) Vous pouvez manger le pion diago bas GAUCHE et donc aller en position {i+2}, {j-2}")
                        self.limit_check(i+2, j-2)
                        limit = 0
                    else:
                        print("\nVous ne pouvez vous deplacez en diagonale bas gauche")
                        limit = 1
                except IndexError:
                    print("\nVous sortez du damier, mouvement impossible\n")
                    limit = 2

                try:
                    limit = 0
                    # On repete les meme actions pour les cases tout autour
                    # self.damier[i+1][j-1] represente diago en bas a droite
                    if damier[i+1][j+1] == 0:
                        print(f"(7) Dame Blanche en position {i},{j} peut avancer en diagonale bas DROITE et donc aller en position {i+1}, {j+1}")
                        self.limit_check(i+1, j+1)
                        limit = 0
                    elif damier[i+1][j+1] == 1 and damier[i+2][j+2] == 0:
                        print(f"(8) Vous pouvez manger le pion diago bas DROITE et donc aller en position {i+2}, {j+2}")
                        self.limit_check(i+2, j+2)
                        limit = 0
                    else:
                        print("\nVous ne pouvez vous deplacez en diagonale bas droite\n")
                        #limit = 1
                except IndexError:
                    print("\nVous sortez du damier, mouvement impossible\n")
                    limit = 2

                # Choix du joueur
                choice = input("Que choississez-vous ?\n\
                    - Diago Gauche d'une case         (1)\n\
                    - Prendre pion noir haut gauche   (2)\n\
                    - Diago Droite d'une case         (3)\n\
                    - Prendre pion noir haut droite   (4)\n\
                    - Diago bas gauche                (5)\n\
                    - Prendre pion noir bas gauche    (6)\n\
                    - Diago bas droite                (7)\n\
                    - Prendre pion noir bas droite    (8)\n")
                # Appel de la methode pour faire avance le pion blanc
                print("limit = ", limit)
                if int(choice) == 1 and limit == 0:
                    if self.debug != 2:
                        Damier.blanc_prise_pion(self, 1)
                        self.damier[i][j] = 0
                    self.affichage()
                # Appel de la methode pour Prendre pion noir haut gauche(2)
                if int(choice) == 2 and limit == 0:
                    if self.debug != 2:
                        Damier.blanc_prise_pion(self, 2)
                        self.damier[i][j] = 0
                        self.nb_pionNoir -= 1
                    self.affichage()
                # Appel de la methode pour Diago Droite d'une case(3)
                if int(choice) == 3 and limit == 0:
                    if self.debug != 2:
                        Damier.blanc_prise_pion(self, 3)
                        self.damier[i][j] = 0
                    self.affichage()
                # Appel de la methode pour Prendre pion noir haut droite(4)
                if int(choice) == 4 and limit == 0:
                    if self.debug != 2:
                        Damier.blanc_prise_pion(self, 4)
                        self.damier[i][j] = 0
                        self.nb_pionNoir -= 1
                    self.affichage()
                # Diago bas gauche
                if int(choice) == 5 and limit == 0:
                    if self.debug != 2:
                        Damier.blanc_prise_pion(self, 5)
                        self.damier[i][j] = 0
                    self.affichage()
                # manger diago bas gauche
                if int(choice) == 6 and limit == 0:
                    if self.debug != 2:
                        Damier.blanc_prise_pion(self, 6)
                        self.damier[i][j] = 0
                        self.nb_pionNoir -= 1
                    self.affichage()
                # Diago bas droite
                if int(choice) == 7 and limit == 0:
                    if self.debug != 2:
                        Damier.blanc_prise_pion(self, 7)
                        self.damier[i][j] = 0
                    self.affichage()
                # manger bas droite
                if int(choice) == 8 and limit == 0:
                    if self.debug != 2:
                        Damier.blanc_prise_pion(self, 8)
                        self.damier[i][j] = 0
                        self.nb_pionNoir -= 1
                    self.affichage()

                # changement de tours des joueurs
                self.joueur_blanc = False
                self.joueur_noir = True

 
            elif self.joueur_blanc == True and damier[i][j] != 1 and self.damier[i][j] != 3:
                print("Ce n'est pas un pion Blanc !\n")
            elif self.joueur_noir == True and damier[i][j] != 2 and self.damier[i][j] != 4:
                print("Ce n'est pas un pion Noir !\n")

            # ------------------------------------------------------------------------
            #                   DAME NOIR MOUVEMENT
            # ------------------------------------------------------------------------
            if self.check_dame == True and self.damier[i][j] == 4:
                if self.joueur_noir == True:
                    self.debug = 0
                try:
                    # variable de test
                    limit = 0
                    print("\nPossibilitées: \n")
                    # On verifie la case diagonale haut gauche s'il y a un pion adversaire
                    if damier[i-1][j-1] == 0:
                        # Vérifie la position du point pour le déplacer dans la diagonale haut gauche 
                        print(f"(1) Dame Noir en position {i},{j} peut avancer en diagonale haut GAUCHE et donc aller en position {i-1}, {j-1}")
                        self.limit_check(i-1, j-1)
                    elif damier[i-1][j-1] == 2 and damier[i-2][j-2] == 0:
                        print(f"(2) Vous pouvez manger le pion diago haut GAUCHE et donc aller en position {i-2}, {j-2}")
                        self.limit_check(i-2, j-2)
                    else:
                        print("\nDame Noir ne peux se deplacer en diagonale haut gauche\n")
                        limit = 1
                except IndexError:
                    print("\nVous sortez du damier, mouvement impossible\n")
                    limit = 2
                cpt += 1
 
                try:
                    limit = 0
                    # On repete les meme actions pour les cases tout autour
                    # self.damier[i-1][j+1] represente diago en haut a droite
                    if damier[i-1][j+1] == 0:
                        print(f"(3) Dame Noir en position {i},{j} peut avancer en diagonale haut DROITE et donc aller en position {i-1}, {j+1}")
                        self.limit_check(i-1, j+1)
                    elif damier[i-1][j+1] == 2 and damier[i-2][j+2] == 0:
                        print(f"(4) Vous pouvez manger le pion diago haut DROITE et donc aller en position {i-2}, {j+2}")
                        self.limit_check(i-2, j+2)
                    else:
                        print("\nDame Noir ne peux se deplacer en diagonale haut droite\n")
                        limit = 1
                except IndexError:
                    print("\nVous sortez du damier, mouvement impossible\n")
                    limit = 2

                try:
                    limit = 0
                    if damier[i+1][j-1] == 0:
                        print(f"(5) Dame Noir en position {i},{j} peut avancer en diagonale bas GAUCHE et donc aller en position {i+1}, {j-1}")
                        # Vérification du postionnement
                        self.limit_check(i+1, j-1)
                        limit = 0
                    elif damier[i+1][j-1] == 1 and damier[i+2][j-2] == 0:
                        print(f"(6) Vous pouvez manger le pion diago bas GAUCHE et donc aller en position {i+2}, {j-2}")
                        self.limit_check(i+2, j-2)
                        limit = 0
                    else:
                        print("\nVous ne pouvez vous deplacez en diagonale bas gauche")
                        limit = 1
                except IndexError:
                    print("\nVous sortez du damier, mouvement impossible\n")
                    limit = 2

                try:
                    limit = 0
                    # On repete les meme actions pour les cases tout autour
                    # self.damier[i+1][j-1] represente diago en bas a droite
                    if damier[i+1][j+1] == 0:
                        print(f"(7) Dame Noir en position {i},{j} peut avancer en diagonale bas DROITE et donc aller en position {i+1}, {j+1}")
                        self.limit_check(i+1, j+1)
                        limit = 0
                    elif damier[i+1][j+1] == 1 and damier[i+2][j+2] == 0:
                        print(f"(8) Vous pouvez manger le pion diago bas DROITE et donc aller en position {i+2}, {j+2}")
                        self.limit_check(i+2, j+2)
                        limit = 0
                    else:
                        print("\nVous ne pouvez vous deplacez en diagonale bas droite\n")
                        #limit = 1
                except IndexError:
                    print("\nVous sortez du damier, mouvement impossible\n")
                    limit = 2

                # Choix du joueur
                choice = input("Que choississez-vous ?\n\
                    - Diago Gauche d'une case         (1)\n\
                    - Prendre pion noir haut gauche   (2)\n\
                    - Diago Droite d'une case         (3)\n\
                    - Prendre pion noir haut droite   (4)\n\
                    - Diago bas gauche                (5)\n\
                    - Prendre pion noir bas gauche    (6)\n\
                    - Diago bas droite                (7)\n\
                    - Prendre pion noir bas droite    (8)\n")
                # Appel de la methode pour faire avance le pion noir
                print("limit = ", limit)
                if int(choice) == 1 and limit == 0:
                    if self.debug != 2:
                        Damier.noir_prise_pion(self, 5)
                        self.damier[i][j] = 0
                    self.affichage()
                # Appel de la methode pour Prendre pion blanc haut gauche(2)
                if int(choice) == 2 and limit == 0:
                    if self.debug != 2:
                        Damier.noir_prise_pion(self, 6)
                        self.damier[i][j] = 0
                        self.nb_pionNoir -= 1
                    self.affichage()
                # Appel de la methode pour Diago Droite d'une case(3)
                if int(choice) == 3 and limit == 0:
                    if self.debug != 2:
                        Damier.noir_prise_pion(self, 7)
                        self.damier[i][j] = 0
                    self.affichage()
                # Appel de la methode pour Prendre pion blanc haut droite(4)
                if int(choice) == 4 and limit == 0:
                    if self.debug != 2:
                        Damier.noir_prise_pion(self, 8)
                        self.damier[i][j] = 0
                        self.nb_pionNoir -= 1
                    self.affichage()
                # Diago bas gauche
                if int(choice) == 5 and limit == 0:
                    if self.debug != 2:
                        Damier.noir_prise_pion(self, 1)
                        self.damier[i][j] = 0
                    self.affichage()
                # manger diago bas gauche
                if int(choice) == 6 and limit == 0:
                    if self.debug != 2:
                        Damier.noir_prise_pion(self, 2)
                        self.damier[i][j] = 0
                        self.nb_pionNoir -= 1
                    self.affichage()
                # Diago bas droite
                if int(choice) == 7 and limit == 0:
                    if self.debug != 2:
                        Damier.noir_prise_pion(self, 3)
                        self.damier[i][j] = 0
                    self.affichage()
                # manger bas droite
                if int(choice) == 8 and limit == 0:
                    if self.debug != 2:
                        Damier.noir_prise_pion(self, 4)
                        self.damier[i][j] = 0
                        self.nb_pionNoir -= 1
                    self.affichage()

                # changement de tours des joueurs
                self.joueur_blanc = True
                self.joueur_noir = False

 
            elif self.joueur_blanc == True and damier[i][j] != 1 and self.damier[i][j] != 3:
                print("Ce n'est pas un pion Blanc !\n")
            elif self.joueur_noir == True and damier[i][j] != 2 and self.damier[i][j] != 4:
                print("Ce n'est pas un pion Noir !\n")
            # ---------------------------------------------------------------
            #                   PION BLANC verification
            # ------------------------------------------------------------------------
            if self.joueur_blanc == True and damier[i][j] == 1:
                self.debug = 0
                try:
                    # variable de test
                    limit = 0
                    
                    print("\nPossibilitées: ")
                    # On verifie la case diagonale haut gauche s'il y a un pion adversaire
                    if damier[i-1][j-1] == 0:
                        # Vérifie la position du point pour le déplacer dans la diagonale haut gauche 
                        print(f"(1) Pion Blanc en position {i},{j} peut avancer en diagonale haut GAUCHE et donc aller en position {i-1}, {j-1}")
                        self.limit_check(i-1, j-1)
                    elif damier[i-1][j-1] == 2 and damier[i-2][j-2] == 0:
                        print(f"(2) Vous pouvez manger le pion diago haut GAUCHE et donc aller en position {i-2}, {j-2}")
                        self.limit_check(i-2, j-2)
                    else:
                        print("\nPion Blanc ne peux se deplacer en diagonale haut gauche\n")
                        limit = 1
                except IndexError:
                    print("\nVous sortez du damier, mouvement impossible\n")
                    limit = 2
                cpt += 1
 
                try:
                    limit = 0
                    # On repete les meme actions pour les cases tout autour
                    # self.damier[i-1][j+1] represente diago en haut a droite
                    if damier[i-1][j+1] == 0:
                        print(f"(3) Pion Blanc en position {i},{j} peut avancer en diagonale haut DROITE et donc aller en position {i-1}, {j+1}")
                        self.limit_check(i-1, j+1)
                    elif damier[i-1][j+1] == 2 and damier[i-2][j+2] == 0:
                        print(f"(4) Vous pouvez manger le pion diago haut DROITE et donc aller en position {i-2}, {j+2}")
                        self.limit_check(i-2, j+2)
                    else:
                        print("\nPion Blanc ne peux se deplacer en diagonale haut droite\n")
                        limit = 1
                except IndexError:
                    print("\nVous sortez du damier, mouvement impossible\n")
                    limit = 2

                # Choix du joueur
                choice = input("\nQue choississez-vous ?\n\
                        - Diago Gauche d'une case         (1)\n\
                        - Prendre pion noir haut gauche   (2)\n\
                        - Diago Droite d'une case         (3)\n\
                        - Prendre pion noir haut droite   (4)\n")
                # Appel de la methode pour faire avance le pion blanc
                if int(choice) == 1 and limit == 0:
                    if self.debug != 2:
                        Damier.blanc_prise_pion(self, 1)
                        self.damier[i][j] = 0
                    self.affichage()
                # Appel de la methode pour Prendre pion noir haut gauche(2)
                if int(choice) == 2 and limit == 0:
                    if self.debug != 2:
                        Damier.blanc_prise_pion(self, 2)
                        self.damier[i][j] = 0
                        self.nb_pionNoir -= 1
                    self.affichage()
                # Appel de la methode pour Diago Droite d'une case(3)
                if int(choice) == 3 and limit == 0:
                    if self.debug != 2:
                        Damier.blanc_prise_pion(self, 3)
                        self.damier[i][j] = 0
                    self.affichage()
                # Appel de la methode pour Prendre pion noir haut droite(4)
                if int(choice) == 4 and limit == 0:
                    if self.debug != 2:
                        Damier.blanc_prise_pion(self, 4)
                        self.damier[i][j] = 0
                        self.nb_pionNoir -= 1
                    self.affichage()

                # changement de tours des joueurs
                self.joueur_blanc = False
                self.joueur_noir = True

 
            elif self.joueur_blanc == True and damier[i][j] != 1:
                print("Ce n'est pas un pion Blanc !\n")
            elif self.joueur_noir == True and damier[i][j] != 2:
                print("Ce n'est pas un pion Noir !\n")


            # ------------------------------------------------------------------------
            #                    PION NOIR verification
            # ------------------------------------------------------------------------
            if self.joueur_noir == True and damier[i][j] == 2:
                cpt += 1
                self.debug = 1
                try:
                    limit = 0
                    print("\nPossibilitées :")
                    # On repete les meme actions pour toutes les cases tout autours
                    # self.damier[i+1][j-1] represente diago en bas a droite
                    if damier[i+1][j-1] == 0:
                        print(f"(1) Pion Noir en position {i},{j} peut avancer en diagonale bas GAUCHE et donc aller en position {i+1}, {j-1}")
                        # Vérification du postionnement
                        self.limit_check(i+1, j-1)
                    elif damier[i+1][j-1] == 1 and damier[i+2][j-2] == 0:
                        print(f"(2) Vous pouvez manger le pion diago bas GAUCHE et donc aller en position {i+2}, {j-2}")
                        self.limit_check(i+2, j-2)
                    else:
                        print("\nVous ne pouvez vous deplacez en diagonale bas gauche")
                        limit = 1
                except IndexError:
                    print("\nVous sortez du damier, mouvement impossible\n")
                    limit = 2

                try:
                    # On repete les meme actions pour les cases tout autour
                    # self.damier[i+1][j-1] represente diago en bas a droite
                    if damier[i+1][j+1] == 0:
                        print(f"(3) Pion Noir en position {i},{j} peut avancer en diagonale bas DROITE et donc aller en position {i+1}, {j+1}")
                        self.limit_check(i+1, j+1)
                    elif damier[i+1][j+1] == 1 and damier[i+2][j+2] == 0:
                        print(f"(4) Vous pouvez manger le pion diago bas DROITE et donc aller en position {i+2}, {j+2}")
                        self.limit_check(i+2, j+2)
                    else:
                        print("\nVous ne pouvez vous deplacez en diagonale bas droite\n")
                        limit = 1
                except IndexError:
                    print("\nVous sortez du damier, mouvement impossible\n")
                    limit = 2


                # Choix du joueur
                choice = input("\nQue choississez-vous ?\n\
                        - Diago bas Gauche d'une case     (1)\n\
                        - Prendre pion blanc bas gauche   (2)\n\
                        - Diago bas Droite d'une case     (3)\n\
                        - Prendre pion blanc bas droite   (4)\n")
                # Appel de la methode pour faire avance les pions noir
                if int(choice) == 1 and limit == 0:
                    if self.debug != 2:
                        Damier.noir_prise_pion(self, 1)
                        self.damier[i][j] = 0
                    self.affichage()
                # Appel de la methode pour Prendre pion blanc bas gauche(2)
                if int(choice) == 2 and limit == 0:
                    if self.debug != 2:
                        Damier.noir_prise_pion(self, 2)
                        self.damier[i][j] = 0
                        self.nb_pionBlanc -= 1
                    self.affichage()
                # Appel de la methode pour Diago bas Droite d'une case(3)
                if int(choice) == 3 and limit == 0:
                    if self.debug != 2:
                        Damier.noir_prise_pion(self, 3)
                        self.damier[i][j] = 0
                    self.affichage()
                # Appel de la methode pour Prendre pion blanc bas droite(4)
                if int(choice) == 4 and limit == 0:
                    if self.debug != 2:
                        Damier.noir_prise_pion(self, 4)
                        self.damier[i][j] = 0
                        self.nb_pionBlanc -= 1
                    self.affichage()

                # AU tour du joueur blanc et fin de tour du joueur noir
                self.joueur_noir = False
                self.joueur_blanc = True
                
            self.no_pawns()

        # Au bout de 2000 tours, le partie est finie
        if cpt == 2000:
            print("Match nul, la partie est finie ")
            fonc = False

    # Methode pour le deplacement et la prise de pions (argument n qui nous permet de choisir dans quelle situation nous sommes) pour les dames blanches aussi
    def blanc_prise_pion(self, n):
        if n == 1 and self.debug != 2:
            # Pour dame blanche
            if self.damier[i][j] == 3:
                self.damier[i-1][j-1] = 3
            else:
                # Pion blanc placer en diago haut gauche
                self.damier[i-1][j-1] = 1
        if n == 2 and self.debug != 2:
            if self.damier[i][j] == 3:
                self.damier[i-2][j-2] = 3
                self.damier[i-1][j-1] = 0
            else:
                #Pion blanc prend pion noir haut gauche(2)
                self.damier[i-2][j-2] = 1
                # Pion capture enleve du jeu
                self.damier[i-1][j-1] = 0
        if n == 3 and self.debug != 2:
            if self.damier[i][j] == 3:
                self.damier[i-1][j+1] = 3
            else:
                #Diago Droite d'une case(3)
                self.damier[i-1][j+1] = 1
        if n == 4 and self.debug != 2:
            if self.damier[i][j] == 3:
                self.damier[i-2][j+2] = 3
                self.damier[i-1][j+1] = 0
            else:
                #Prendre pion noir haut droite(4)
                self.damier[i-2][j+2] = 1
                # Pion capture enleve du jeu
                self.damier[i-1][j+1] = 0
        #bas gauche
        if n == 5 and self.debug != 2:
            self.damier[i+1][j-1] = 3
        #manger bas gauche
        if n == 6 and self.debug != 2:
            self.damier[i+2][j-2] = 3
            self.damier[i+1][j-1] = 0
        # bas droite
        if n == 7 and self.debug != 2:
            self.damier[i+1][j+1] = 3
        #manger bas droite
        if n == 8 and self.debug != 2:
            self.damier[i+2][j+2] = 3
            self.damier[i+1][j+1] = 0

    # Methode pour le deplacement et la prise de pions (argument n qui nous permet de choisir dans quelle situation nous sommes)
    def noir_prise_pion(self, n):
        if n == 1 and self.debug != 2:
            if self.damier[i][j] == 4:
                self.damier[i+1][j-1] = 4
            else:
                # Pion noir placer en diago bas gauche
                self.damier[i+1][j-1] = 2
        if n == 2 and self.debug != 2:
            if self.damier[i][j] == 4:
                self.damier[i+2][j-2] = 4
                self.damier[i+1][j-1] = 0
            else:
                # Pion noir prend pion blanc bas gauche(2)
                self.damier[i+2][j-2] = 2
                # Pion capture qui est enleve du jeu
                self.damier[i+1][j-1] = 0
        if n == 3 and self.debug != 2:
            if self.damier[i][j] == 4:
                self.damier[i+1][j+1] = 4
            else:
                # Diago bas Droite d'une case(3)
                self.damier[i+1][j+1] = 2
        if n == 4 and self.debug != 2:
            if self.damier[i][j] == 4:
                self.damier[i+2][j+2] = 4
                self.damier[i+1][j+1] = 0
            else:
                # Prendre pion blanc bas droite(4)
                self.damier[i+2][j+2] = 2
                # Pion capture qui est enleve du jeu
                self.damier[i+1][j+1] = 0
        # diago haut gauche
        if n == 5 and self.debug != 2:
            self.damier[i-1][j-1] = 4
        # prendre pion diago haut gauche
        if n == 6 and self.debug != 2:
            self.damier[i-2][j-2] = 4
            self.damier[i-1][j-1] = 0
        # diago haut droite
        if n == 7 and self.debug != 2:
            self.damier[i-1][j+1] = 4
        # prendre pion diago haut droite
        if n == 8 and self.debug != 2:
            self.damier[i-2][j+2] = 4
            self.damier[i-1][j+1] = 0
    
    # Méthode pour eviter les deplacement de pion en dehors du damier
    def limit_check(self, i, j):
        # Vérification des lignes
        if i > len(self.damier) or i < 0:
            print("Mouvement impossible sortie du damier (lignes)")
            self.debug == 2
        # Vérification des colonnes
        elif j > len(self.damier) or j < 0:
            print("Mouvement impossible sortie du damier (colonnes)")
            self.debug == 2
    
    # Methode de fin de jeu si l'un des 2 joueurs n'a plus de pion
    def no_pawns(self):
        if self.nb_pionNoir == 0:
            print("Joueur 2 n'a plus de pion noir (2)\n     Victoire pour le Joueur 1 !")
            quit()
        elif self.nb_pionBlanc == 0:
            print("Joueur 1 n'a plus de pion blanc (1)\n    Victoire pour le Joueur 2 !")
    
    # ------------------------------------------------------------------------
    #                       Evolution pions vers dames
    # ------------------------------------------------------------------------
    # Methode pour l'evolution des pions en dame
    def dames(self):
        # Pion blanc (1) se transforme en Dame Blanche (3)
        if self.damier[i][j] == 1 and self.damier[i] is self.damier[0]:
            self.check_dame = True
            self.damier[i][j] = 3
            self.affichage()
        # Pion noir (2) se transforme en Dame Noir (4)
        elif self.damier[i][j] == 2 and self.damier[i] is self.damier[9]:
            self.check_dame = True
            self.damier[i][j] = 4
            self.affichage()
    
    
    # Methode pour espacer et rendre la matrice plus compréhensible sur le terminal
    def affichage(self):
        c = 0
        for i in self.damier:
            print(f"index{c}:", end="\t")
            c += 1
            for ele in i:
                print(ele, end="\t")
            print()

    def appel(self):
        self.affichage()

if __name__ == "__main__":
    # Le nom inst pour instance, j'avais pas d'idée de nom de variable pour l'instance de la classe :/
    inst = Damier()
    inst.appel()
    print(inst.maingame(inst.damier))