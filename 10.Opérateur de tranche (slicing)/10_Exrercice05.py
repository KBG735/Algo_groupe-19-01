entree = input("Entrez des nombres séparés par des espaces : ")
liste = entree.split()

elements_pairs = [liste[i] for i in range(len(liste)) if i % 2 == 0]

print(f"Éléments aux indices pairs : {elements_pairs}")