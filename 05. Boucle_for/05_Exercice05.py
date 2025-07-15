print("🔤 Compteur de voyelles\n")

mots = input("Entrez du texte : ").split()
voyelles = {'a','e','i','o','u','y','A','E','I','O','U','Y'}

# Version optimale avec compréhension de liste
total_voyelles = sum(1 for mot in mots for lettre in mot if lettre in voyelles)

# Analyse détaillée
stats_mots = {mot: sum(1 for lettre in mot if lettre in voyelles) for mot in mots}

print(f"\n📊 Résultats :")
print(f"- Nombre total de voyelles : {total_voyelles}")
print(f"- Nombre de mots analysés : {len(mots)}")
print("\n🔍 Détail par mot :")
for mot, count in stats_mots.items():
    print(f"  '{mot}': {count} voyelle{'s' if count > 1 else ''}")

if total_voyelles == 0:
    print("\n❌ Aucune voyelle trouvée !")
elif total_voyelles > 10:
    print("\n🎉 Beaucoup de voyelles !")