# Ajusteur d'ingrédients de recette
# L'objectif est d'ajuster la quantité d'un ingrédient en fonction du nombre de portions.

def obtenir_float(message):

    # fonction pour obtenir un nombre (float) de l'utilisateur.
    # elle boucle jusqu'à ce qu'une valeur valide soit entrée.

    while True:
        try:
            valeur_str = input(message)
            valeur = float(valeur_str)   # conversion en float
            if valeur < 0:
                print("Veuillez entrer un nombre positif.")
                continue
            return valeur
        except ValueError:
            print("Entrée invalide ! Veuillez entrer un nombre.")

def obtenir_int(message):

    # Fonction pour obtenir un entier (int) de l'utilisateur.
    # Elle boucle jusqu'à ce qu'une valeur valide soit entrée.

    while True:
        try:
            valeur_str = input(message)
            valeur = int(valeur_str)     # conversion en int
            if valeur <= 0:
                print("Veuillez entrer un entier positif.")
                continue
            return valeur
        except ValueError:
            print("Entrée invalide ! Veuillez entrer un entier.")

def ajuster_recette():
    print("\n AJUSTEUR D'INGRÉDIENTS \n")

    # phase 1: Entrer les détails
    quantite_originale = obtenir_float("Entrez la quantité originale de l'ingrédient : ")
    portions_originales = obtenir_int("nombres de personnes prévue pour la recette ? : ")
    portions_desirees = obtenir_int("Pour combien de personnes voulez-vous cuisiner ? : ")

    # phase 2: Calcul de la nouvelle quantité
    facteur_ajuster = portions_desirees / portions_originales
    nouvelle_quantite = round(quantite_originale * facteur_ajuster, 1) # application du ratio et arrondi

    # phase 3: Affichage du résultat
    print("\n RECETTE AJUSTÉE ")
    print(f"La recette originale est pour {portions_originales} personne(s).")
    print(f"Pour {portions_desirees} personne(s), il vous faut {nouvelle_quantite} unités de votre ingrédient.\n")

def refaire_ajustement():
    while True:
        ajuster_recette()
        reponse = input(" ajuster un autre ingrédient ? (oui/non) : ").strip().lower()
        if reponse not in ['oui', 'o']: # Si l'utilisateur répond non, on quitte la boucle
            print("Merci d'avoir utilisé l'ajusteur d'ingrédients !")
            break # sortie de la boucle

# Lancement du programme
refaire_ajustement()