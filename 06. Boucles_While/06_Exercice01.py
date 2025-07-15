import random

print("🎲 Jeu : Devine le nombre secret (1-100) 🎲\n")
print("💡 Astuce : Le nombre est entre 1 et 100")
print("----------------------------------------")

nombre_secret = random.randint(1, 100)
essais = 0
historique = []

while True:
    essai = int(input("\n🤔 Ton essai : "))
    essais += 1
    historique.append(essai)

    if essai < 1 or essai > 100:
        print("⚠️ Entre un nombre entre 1 et 100 !")
        continue

    if essai < nombre_secret:
        print("⬆️ Plus grand !")
    elif essai > nombre_secret:
        print("⬇️ Plus petit !")
    else:
        print(f"\n🎉 Bravo ! Trouvé en {essais} essais")
        print(f"📊 Historique : {historique}")
        print(f"🔢 Le nombre était : {nombre_secret}")
        break

    # Indice après 5 essais
    if essais == 5:
        if nombre_secret % 2 == 0:
            print("💡 Indice : Le nombre est pair")
        else:
            print("💡 Indice : Le nombre est impair")