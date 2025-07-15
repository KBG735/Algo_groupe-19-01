print("🏥 Auto-évaluation médicale\n")

# Question initiale
fievre = input("🌡️ Avez-vous de la fièvre ? (oui/non) : ").lower()

if fievre == "oui":
    print("\n⚠️ Symptôme notable détecté")
    douleurs = input("💢 Avez-vous des douleurs ? (oui/non) : ").lower()

    if douleurs == "oui":
        print("\n🚨 Recommandation :")
        print("- Consulter un médecin rapidement")
        print("- Boire beaucoup d'eau")
        print("- Prendre votre température toutes les 2 heures")
    else:
        print("\nℹ️ Conseil :")
        print("- Surveiller l'évolution de la fièvre")
        print("- Repos et hydratation")
        print("- Consulter si fièvre persiste plus de 48h")

else:
    toux = input("🤧 Avez-vous une toux ? (oui/non) : ").lower()

    if toux == "oui":
        print("\n💊 Recommandation :")
        print("- Repos complet")
        print("- Boissons chaudes")
        print("- Si toux persiste >5 jours, consulter")
    else:
        print("\n✅ État normal")
        print("- Aucun symptôme alarmant détecté")
        print("- Continuez vos bonnes habitudes")

print("\nPrenez soin de vous ! ❤️")