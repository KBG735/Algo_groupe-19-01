def est_palindrome(mot):
    mot = mot.lower()  # Convertir en minuscules pour une comparaison insensible à la casse
    return mot == mot[::-1]

mot = input("Entrez un mot : ").strip()  # Supprimer les espaces éventuels
if est_palindrome(mot):
    print(f"'{mot}' est un palindrome.")
else:
    print(f"'{mot}' n'est pas un palindrome.")