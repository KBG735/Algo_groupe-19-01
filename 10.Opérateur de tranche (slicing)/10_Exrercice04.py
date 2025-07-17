numero = input("Entrez un numero : ")
if len(numero) > 3:
    masque = "*" * (len(numero) - 3) + numero[-3:]
    print(f"Numero masqué : {masque}")
else:
    print("Numero trop court pour masquer.")