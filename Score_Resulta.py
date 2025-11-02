# Calculateur de score de jeu video
# l'objectif est de calculer le score final d'un joueur après un niveau.

def obtenir_int(message):

    # fonction pour obtenir un entier de l'utilisateur.
    # boucle jusqu'à ce que l'utilisateur tape un entier valide.

    while True:
        try:
            valeur_str = input(message)
            valeur = int(valeur_str)
            if valeur < 0:
                print("Veuillez entrer un entier positif.")
                continue
            return valeur
        except ValueError:
            print("Entrée invalide ! Veuillez entrer un entier.")

def obtenir_bool(message):

   # fonction pour obtenir un booléen sur une réponse 'oui' ou 'non'.
    # retourne une reponse bool en fonction de la reponse de l'utilisateur .

    while True:
        reponse = input(message).strip().lower()  # Supprime les espaces et met en minuscules
        if reponse == "oui":
            return True
        elif reponse == "non":
            return False
        else:
            print("Entrée invalide ! Répondez par 'oui' ou 'non'.")

def calculer_score_final():
    # Calcule le score final du joueur selon les bonus et conditions.
    print("\n CALCULATEUR DE SCORE ")

    # Phase 1 : Récupération des infos de l'utilisateur
    score_de_base = 1000
    pieces_ramassees = obtenir_int("Nombre de pièces collectées : ")
    sans_degats = obtenir_bool("Avez-vous subi des dégâts ? (oui/non) : ")

    # Phase 2 : Calcul du score
    bonus_pieces = pieces_ramassees * 100
    multiplicateur_degats = 2 if sans_degats else 1  # Double le score si aucun dégât
    score_final = (score_de_base + bonus_pieces) * multiplicateur_degats

    # Phase 3 : Affiche un résultat final
    print("\n RÉSULTAT ")
    print(f"Score de base : {score_de_base}")
    print(f"Bonus (pièces) : +{bonus_pieces}")
    print(f"Multiplicateur (sans dégâts) : x{multiplicateur_degats}")
    print(f"\n Score final : {score_final} ")


def main():
    # Boucle principale du programme, permet de rejouer aussi .
    print(" BIENVENUE ")

    while True:
        # lancer le calcul
        calculer_score_final()

        while True:
            recommencer = input("\nVoulez-vous calculer un autre score ? (oui/non) : ").strip().lower()

            if recommencer == "":
                print("taper une réponse : 'oui' ou 'non'.")
            elif recommencer in ["oui", "non"]:
                break  # Sortie de la boucle si la réponse est valide
            else:
                print("Incorrect ! Répondez par 'oui' ou 'non'.")

        if recommencer == "non":
            print("\nMerci d'avoir joué !")
            break  # Sortie de la boucle principale donc fin du programme


if __name__ == "__main__":
    main()