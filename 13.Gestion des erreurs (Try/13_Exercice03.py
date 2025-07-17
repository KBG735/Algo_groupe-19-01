nom_fichier = input("Nom du fichier à lire : ")

try:
    with open(nom_fichier, "r", encoding="utf-8") as f:
        contenu = f.read()
except FileNotFoundError:
    print("Erreur : Fichier introuvable.")
except PermissionError:
    print("Erreur : Permission refusée.")
else:
    print("\nContenu du fichier :")
    print("--------------------")
    print(contenu)
    print("--------------------")
finally:
    print("\nOpération terminée.")