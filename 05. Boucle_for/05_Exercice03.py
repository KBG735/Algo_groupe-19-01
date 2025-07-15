texte = input("🔤 Entrez une chaîne de caractères : ")

# Version optimale avec slicing
inverse = texte[::-1]

print(f"\n🔄 Chaîne inversée : {inverse}")

# Bonus : Analyse supplémentaire
print(f"\n📊 Statistiques :")
print(f"- Longueur : {len(texte)} caractères")
print(f"- Palindrome : {'Oui' if texte == inverse else 'Non'}")

if len(texte) > 20:
    print("\n⚠️ Attention : Chaîne très longue !")
elif not texte:
    print("\n❌ Vous n'avez rien saisi !")