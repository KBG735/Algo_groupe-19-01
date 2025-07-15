age = int(input("🎂 Entrez votre âge : "))
pays = input("🌍 Entrez votre pays : ").lower()

print("\n🔍 Vérification en cours...")

if age >= 18 and pays in ["congo", "cameroun", "rdc"]:
    print("\n✅ Inscription autorisée ! Bienvenue 👋")
elif age < 18:
    print("\n❌ Désolé, vous devez avoir 18 ans minimum")
else:
    print("\n⚠️ Programme réservé aux ressortissants :")
    print("- Congo 🇨🇬")
    print("- Cameroun 🇨🇲")
    print("- RDC 🇨🇩")

print("\nMerci pour votre intérêt ! ✨")