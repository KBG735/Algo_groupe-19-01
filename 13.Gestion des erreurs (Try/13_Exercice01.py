try:
    a = float(input("Nombre 1 : "))
    b = float(input("Nombre 2 : "))
    result = a / b
except ZeroDivisionError:
    print("Erreur : Division par zéro !")
except ValueError:
    print("Erreur : Veuillez entrer des nombres valides !")
else:
    print(f"Résultat : {result:.2f}")
finally:
    print("Fin de l'opération.")