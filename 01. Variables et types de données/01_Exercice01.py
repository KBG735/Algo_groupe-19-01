prenom = input("Entrez votre prénom : ")
age = int(input("Entrez votre âge : "))
ville = input("Entrez votre ville : ")
metier = input("Entrez votre métier : ")

jours_vecus = age * 365 + (age // 4)

print("\n🌟 PROFIL PERSONNALISÉ 🌟")
print(f"✨ Prénom : {prenom.upper()}")
print(f"🎂 Âge : {age} ans (soit {jours_vecus} jours de bonheur !)")
print(f"🌆 Ville : {ville.capitalize()}")
print(f"💼 Métier : {metier.title()}")
print("\nMerci pour votre participation ! 🚀")