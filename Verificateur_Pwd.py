def verifier_longueur(mot_de_passe):
    # Vérifie si le mot de passe respecte la longueur minimale et maximale.
    if len(mot_de_passe) < 8:
        return False, "Mot de passe trop court (minimum 8 caractères)"
    elif len(mot_de_passe) > 50:
        return False, "Mot de passe trop long (maximum 50 caractères)"
    else:
        return True, "Longueur correcte"

def contient_majuscule(mot_de_passe):
    # Vérifie qu'il y'a au moins une majuscule.
    return any(c.isupper() for c in mot_de_passe)

def contient_minuscule(mot_de_passe):
    # Vérifie qu'il y'a au moins une minuscule.
    return any(c.islower() for c in mot_de_passe)

def contient_chiffre(mot_de_passe):
    # Vérifie qu'il y'a au moins un chiffre.
    return any(c.isdigit() for c in mot_de_passe)

def verifier_force_mot_de_passe():
    # fonction principale qui demande le mot de passe et affiche le resultat complet.
    while True:
        try:
            mot_de_passe = input("Veuillez saisir votre mot de passe : ")

            # Vérifier la longueur
            longueur_valide, message_longueur = verifier_longueur(mot_de_passe)

            # Vérifier majuscule, minuscule et chiffre
            a_majuscule = contient_majuscule(mot_de_passe)
            a_minuscule = contient_minuscule(mot_de_passe)
            a_chiffre = contient_chiffre(mot_de_passe)

            # Vérification globale
            est_fort = longueur_valide and a_majuscule and a_minuscule and a_chiffre

            # Affichage du resultat
            print("\n--- RAPPORT DE FORCE DU MOT DE PASSE ---")
            print(f"Longueur : {message_longueur} - {'OK' if longueur_valide else 'NON'}")
            print(f"Contient une majuscule : {'Oui' if a_majuscule else 'Non'}")
            print(f"Contient une minuscule : {'Oui' if a_minuscule else 'Non'}")
            print(f"Contient un chiffre : {'Oui' if a_chiffre else 'Non'}")

            # resultat final
            if est_fort:
                print("\nRéponse : mot de passe considéré comme fort !")
                break  # Sort de la boucle si le mot de passe est fort
            else:
                print("\nRéponse : mot de passe est faible. Veuillez réessayer.\n")

        except Exception as erreur:
            print(f"Erreur possible : {erreur}")

# Appel de la fonction
verifier_force_mot_de_passe()
