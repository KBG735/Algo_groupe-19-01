texte = input("Entrez une phrase : ").strip()

# Calcul des statistiques
nb_mots = len(texte.split()) if texte else 0
nb_caracteres = len(texte)
nb_espaces = texte.count(' ')
nb_voyelles = sum(1 for char in texte.lower() if char in 'aeiouyéèêàùïüö')

with open("rapport.txt", "w", encoding="utf-8") as f:
    f.write("=== Rapport d'analyse ===\n\n")
    f.write(f"Phrase analysée : \"{texte}\"\n\n")
    f.write(f"- Nombre de mots : {nb_mots}\n")
    f.write(f"- Nombre de caractères : {nb_caracteres}\n")
    f.write(f"- Nombre d'espaces : {nb_espaces}\n")
    f.write(f"- Nombre de voyelles : {nb_voyelles}\n")

print("Rapport complet sauvegardé dans 'rapport.txt'.")