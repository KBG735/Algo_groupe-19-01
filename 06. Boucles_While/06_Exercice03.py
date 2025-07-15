print("📊 CALCUL DE MOYENNE DES NOTES 📊")
print("---------------------------------")

notes = []  # Liste pour stocker toutes les notes

while True:
    try:
        note = float(input("\nEntrez une note (entre 0 et 20) ou -1 pour terminer : "))

        if note == -1:
            break

        if note < 0 or note > 20:
            print("⚠️ Note invalide! Entrez une valeur entre 0 et 20")
            continue

        notes.append(note)
        print(f"Note enregistrée: {note:.2f}/20")

    except ValueError:
        print("❌ Erreur: Veuillez entrer un nombre valide")

if notes:
    print("\n📝 Récapitulatif des notes:")
    for i, note in enumerate(notes, 1):
        print(f"Note {i}: {note:.2f}/20")

    moyenne = sum(notes) / len(notes)
    note_max = max(notes)
    note_min = min(notes)

    print("\n📊 Statistiques:")
    print(f"- Nombre de notes: {len(notes)}")
    print(f"- Meilleure note: {note_max:.2f}/20")
    print(f"- Moins bonne note: {note_min:.2f}/20")
    print(f"✨ Moyenne: {moyenne:.2f}/20")

    if moyenne >= 15:
        print("\n🎉 Excellent travail!")
    elif moyenne >= 10:
        print("\n👍 Bon résultat!")
    else:
        print("\n💪 Continuez vos efforts!")
else:
    print("\nℹ️ Aucune note valide n'a été saisie.")