print("🚪 Système de contrôle d'accès\n")

role = input("👤 Rôle (employé/visiteur/sécurité) : ").lower()

if role == "employé":
    badge = input("🪪 Badge valide ? (oui/non) : ").lower()
    if badge == "oui":
        print("\n✅ Accès autorisé - Bonne journée collègue !")
    else:
        print("\n❌ Accès refusé - Veuillez contacter les RH")
elif role == "visiteur":
    rdv = input("📅 Rendez-vous confirmé ? (oui/non) : ").lower()
    if rdv == "oui":
        print("\n✅ Accès autorisé - Merci de patienter")
    else:
        print("\n❌ Accès refusé - Prenez rendez-vous au 01 23 45 67 89")
elif role == "sécurité":
    print("\n🔒 Accès prioritaire autorisé - Sécurité activée")
else:
    print("\n⚠️ Alerte : Rôle non reconnu - Contactez la réception")

print("\nSystème sécurisé v3.0 🔐")