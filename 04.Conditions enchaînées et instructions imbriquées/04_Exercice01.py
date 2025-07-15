age = int(input("🎂 Age : "))
statut = input("👤 Statut (étudiant/salarié/retraité) : ").lower()

if age < 18:
    tarif = 5
    categorie = "Jeune"
elif 18 <= age <= 25:
    if statut == "étudiant":
        tarif = 6
        categorie = "Étudiant"
    elif statut == "salarié":
        tarif = 8
        categorie = "Jeune actif"
    else:
        tarif = 10
        categorie = "Jeune adulte"
else:
    if statut == "retraité":
        tarif = 7
        categorie = "Retraité"
    else:
        tarif = 10
        categorie = "Adulte"

print(f"\n💳 Votre tarif : {tarif}€ ({categorie})")
print("\nMerci pour votre confiance ! ✨")