def calcul_factorielle(n):
    """Calcule la factorielle de manière récursive"""
    return 1 if n == 0 else n * calcul_factorielle(n - 1)


print("🧮 CALCUL DE FACTORIELLE 🧮")
print("--------------------------")

while True:
    try:
        n = int(input("\nEntrez un entier positif (ou -1 pour quitter) : "))

        if n == -1:
            print("\nAu revoir ! 👋")
            break

        if n < 0:
            print("⚠️ Erreur: Entrez un nombre positif !")
            continue

        # Calcul avec vérification de la taille
        if n > 20:
            print("⚠️ Attention: n > 20 peut causer un overflow !")
            confirm = input("Voulez-vous continuer ? (o/n) : ").lower()
            if confirm != 'o':
                continue

        resultat = calcul_factorielle(n)

        # Affichage formaté pour les grands nombres
        print(f"\n🔢 Factorielle de {n} ({n}!) = ")
        if n <= 10:
            print(f"→ {resultat}")
        else:
            print(f"→ {resultat:.2e} (notation scientifique)")
            print(f"→ Soit environ {len(str(resultat))} chiffres")

    except ValueError:
        print("❌ Erreur: Entrez un nombre valide !")

print("\nFin du programme. Merci ! ✨")