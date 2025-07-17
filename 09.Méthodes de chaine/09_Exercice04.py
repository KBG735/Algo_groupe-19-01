phrase = input("Entrez une phrase ou un titre : ")
mots = phrase.split()
acronyme = ""

for mot in mots:
    if mot:  # Vérifie que le mot n'est pas vide
        acronyme += mot[0].upper()

print(f"Acronyme : {acronyme}")