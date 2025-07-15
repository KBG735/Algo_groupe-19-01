n = int(input("🔢 Entrez un nombre entier : "))

if n % 15 == 0:
    print("\n🎯 Résultat : divisible par 3 ET 5 !")
    print("💡 Astuce : C'est aussi divisible par 15")
else:
    print("\n❌ Non divisible par 3 et 5 simultanément")
    if n % 3 == 0:
        print("➗ Divisible uniquement par 3")
    elif n % 5 == 0:
        print("➗ Divisible uniquement par 5")
    else:
        print("🚫 Non divisible ni par 3 ni par 5")

print("\n✨ Analyse terminée !")