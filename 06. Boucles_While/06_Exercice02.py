print("🌟 MENU INTERACTIF 🌟")

while True:
    print("\n=== MENU PRINCIPAL ===")
    print("1. Dire Bonjour 👋")
    print("2. Additionner deux nombres ➕")
    print("3. Calculer l'âge 🎂")
    print("0. Quitter ❌")

    choix = input("\nChoisissez une option : ")

    if choix == "1":
        nom = input("Comment vous appelez-vous ? ")
        print(f"\nBonjour {nom.capitalize()} ! 😊")

    elif choix == "2":
        print("\n➕ ADDITION DE DEUX NOMBRES")
        try:
            a = float(input("Nombre 1 : "))
            b = float(input("Nombre 2 : "))
            print(f"Résultat : {a + b:.2f}")
        except:
            print("❌ Veuillez entrer des nombres valides !")

    elif choix == "3":
        print("\n🎂 CALCUL D'ÂGE")
        try:
            naissance = int(input("Année de naissance : "))
            age = 2023 - naissance
            print(f"Vous avez {age} ans cette année !")
        except:
            print("❌ Veuillez entrer une année valide !")

    elif choix == "0":
        print("\n👋 Au revoir et à bientôt !")
        break

    else:
        print("\n⚠️ Option invalide - Veuillez choisir 1, 2, 3 ou 0")

    input("\nAppuyez sur Entrée pour continuer...")