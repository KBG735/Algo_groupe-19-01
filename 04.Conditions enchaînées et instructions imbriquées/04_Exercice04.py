print("💰 Calcul de prime annuelle\n")

try:
    anciennete = int(input("🕒 Années d'ancienneté : "))
    note = int(input("⭐ Note de performance (1-5) : "))

    # Validation des entrées
    if anciennete < 0 or note < 1 or note > 5:
        raise ValueError("Valeurs invalides")

    # Calcul de la prime
    if anciennete >= 5:
        prime = 2000 if note >= 4 else 1000
        categorie = "Senior"
    else:
        prime = 500 if note >= 4 else 0
        categorie = "Junior"

    # Affichage détaillé
    print(f"\n📊 Résultats :")
    print(f"- Ancienneté : {anciennete} ans ({categorie})")
    print(f"- Performance : {note}/5")
    print(f"💶 Prime attribuée : {prime}€")

    if prime == max(2000, 1000, 500, 0):
        print("🎉 Félicitations pour votre excellente performance !")
    elif prime == 0:
        print("💡 Conseil : Amélioration nécessaire pour la prochaine évaluation")

except ValueError:
    print("\n❌ Erreur : Veuillez entrer des valeurs valides")
finally:
    print("\nMerci pour votre engagement ! 👏")