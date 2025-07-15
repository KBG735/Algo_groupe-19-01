mdp = input("🔒 Entrez votre mot de passe : ")

if len(mdp) >= 8 and any(c.isdigit() for c in mdp) and any(c.isupper() for c in mdp):
    print("\n✅ Mot de passe valide !")
    print("💪 Sécurité forte")
else:
    print("\n❌ Mot de passe invalide")
    print("⚠️ Doit contenir :")
    print("- 8 caractères minimum")
    print("- Au moins 1 chiffre")
    print("- Au moins 1 majuscule")

print("\n🔐 Sécurité importante !")