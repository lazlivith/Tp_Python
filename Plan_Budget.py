# Planificateur de budget carburant pour un voyage.

def saisir_nombre_positif(message):

    # fonction qui demande à l'utilisateur un nombre positif.
    # répète la saisie tant que l'utilisateur n'entre pas un nombre valide.

    while True:
        try:
            valeur = float(input(message))
            if valeur <= 0:
                print("Erreur : la valeur doit être strictement supérieure à zéro.\n")
            else:
                return valeur
        except ValueError:
            print("Erreur : veuillez entrer un nombre valide.\n")

def calcul_budget_carburant():
    while True:
        # Phase 1 : saisie des infos
        distance_km = saisir_nombre_positif("Entrez la distance totale du voyage (en km) : ")
        consommation = saisir_nombre_positif("Entrez la consommation de carburant de la voiture (L/100 km) : ")
        prix_litre = saisir_nombre_positif("Entrez le prix actuel d'un litre de carburant (€) : ")

        # Phase 2 : Calcul de la consommation et du coût
        carburant_necessaire = (distance_km / 100) * consommation
        cout_total = carburant_necessaire * prix_litre
        cout_total_arrondi = round(cout_total, 2)  # arrondi à 2 décimales

        # Phase 3 : rapport de budget carburant
        print("\n Budget carburant estimé ")
        print(f"Distance totale du voyage : {distance_km} km")
        print(f"Carburant nécessaire pour le voyage : {carburant_necessaire:.2f} litres")
        print(f"Coût total estimé du carburant : {cout_total_arrondi} €")

        # refaire un autre calcul si besoin
        refaire = input("\nVoulez-vous refaire le calcul ? (oui/non) : ").strip().lower()
        if refaire not in ['oui', 'o']:
            print("Merci d'avoir utilisé le planificateur de budget carburant !")
            break  # Sort de la boucle et termine le programme

# Appel de la fonction
calcul_budget_carburant()
