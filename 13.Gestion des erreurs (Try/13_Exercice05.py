import math

try:
    x = float(input("Entrez un nombre : "))
    if x < 0:
        raise ValueError("Nombre négatif, pas de racine réelle.")
    racine = math.sqrt(x)
except ValueError as e:
    print(f"Erreur : {e}")
except:
    print("Erreur : Entrée invalide")
else:
    print(f"Racine carrée : {racine:.4f}")
finally:
    print("Fin du calcul.")