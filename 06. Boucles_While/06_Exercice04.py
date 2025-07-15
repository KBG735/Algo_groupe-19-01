print("🔒 SYSTÈME DE CONTRÔLE D'ACCÈS 🔒")
print("-------------------------------")

essais = 0
max_essais = 3
mdp_correct = "Python2025"

while essais < max_essais:
    mdp = input("\nEntrez le mot de passe : ")
    essais += 1

    if mdp == mdp_correct:
        print("\n✅ Mot de passe correct !")
        print("🔓 Accès autorisé - Bienvenue !")
        break
    else:
        restants = max_essais - essais
        print(f"❌ Mot de passe incorrect (essais restants: {restants})")

        # Indice après 2 essais
        if essais == 2:
            print("💡 Indice: Le mot de passe contient 'Python' et une année future")
else:
    print("\n🚫 Trop de tentatives - Accès bloqué")
    print("Veuillez contacter l'administrateur")

print("\nSécurité système activée 🔐")