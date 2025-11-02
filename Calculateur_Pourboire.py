# FONCTIONS DE SAISIE ET VALIDATION

def demander_float(message):

    # Demande à l'utilisateur un nombre à virgule (float).
   # Répète la saisie tant que l'entrée est invalide.

    while True:
        valeur_str = input(message)  # demander l'entrée utilisateur
        try:
            valeur = float(valeur_str)  # essayer de convertir en float
            if valeur < 0:
                print("Le montant doit être positif. Réessayez.")
                continue  # retourne au début de la boucle si négatif
            return valeur  # sortie de la fonction avec la valeur valide
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre.")  # message d'erreur


def demander_int(message):

   # demande à l'utilisateur un entier.
   # Répète la saisie tant que l'entrée est invalide.

    while True:
        valeur_str = input(message)
        try:
            valeur = int(valeur_str)  # essayer de convertir le type en int
            if valeur <= 0:
                print("Le nombre doit être supérieur à 0. Réessayez.")
                continue
            return valeur  # sortie de la fonction avec la valeur valide
        except ValueError:
            print("Incorrect ! entrer un entier.")


# fonction calcul

def calculer_part_par_personne(montant_facture, pourcentage_pourboire, nombre_personnes):

    # Calcule la part que chaque personne doit payer,
   # en incluant le pourboire.
    montant_pourboire = montant_facture * (pourcentage_pourboire / 100)  # calcul du pourboire
    montant_total = montant_facture + montant_pourboire  # montant total avec pourboire
    part_par_personne = montant_total / nombre_personnes  # montant par personne
    return round(part_par_personne, 2), round(montant_total, 2)  # arrondi à 2 décimales


# fonction pour afficher resultat

def afficher_resultat(montant_total, part_par_personne, montant_facture, pourcentage_pourboire, nombre_personnes):

    # Affiche le résumé du paiement de manière claire.

    print("\n Resultat ")
    print(f"Montant total (avec pourboire) : {montant_total} €")
    print(f"Chaque personne doit payer : {part_par_personne} €")
    print(f" une facture de {montant_facture} € avec un pourboire de {pourcentage_pourboire}% repartit entre {nombre_personnes} personnes.")


# point d'entré

def main():
    print("Bienvenue dans le calculateur de pourboire !")

    while True:
        # Collecte des informations
        montant_facture = demander_float("Entrez le montant total de la facture (€) : ")
        pourcentage_pourboire = demander_int("Entrez le pourcentage de pourboire souhaité : ")
        nombre_personnes = demander_int("Entrez le nombre de personnes partageant la note : ")

        # Calculs
        part_par_personne, montant_total = calculer_part_par_personne(
            montant_facture, pourcentage_pourboire, nombre_personnes
        )

        # Affichage
        afficher_resultat(montant_total, part_par_personne, montant_facture, pourcentage_pourboire, nombre_personnes)

        # Demander si l'utilisateur veut refaire
        refaire = input("\nVoulez-vous refaire un calcul ? (o/n) : ").strip().lower()
        if refaire not in [ 'oui' , 'o']: # on quitte la boucle si la reponse n'est pas oui
            print("Merci d'avoir utilisé le calculateur de pourboire !")
            break # sortie de la boucle


# Exécution du programme
if __name__ == "__main__":
    main()
