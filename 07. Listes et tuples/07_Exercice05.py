entree = input("Entrez des elements : ")
liste = entree.split()

liste_inversee = []

for i in range(len(liste) - 1, -1, -1):
    liste_inversee.append(liste[i])

print(f"Liste inversée : {liste_inversee}")