print("🔢 Calcul de la somme des nombres pairs\n")

entree = input("Entrez des nombres séparés par des espaces : ")
nombres = [int(x) for x in entree.split()]

somme_pairs = sum(n for n in nombres if n % 2 == 0)

print(f"\n📊 Résultats :")
print(f"- Nombres saisis : {len(nombres)}")
print(f"- Nombre de pairs : {sum(1 for n in nombres if n % 2 == 0)}")
print(f"💰 Somme des pairs : {somme_pairs}")

if somme_pairs == 0:
    print("\nℹ️ Aucun nombre pair trouvé")
elif somme_pairs > 100:
    print("\n🎉 Total impressionnant !")
else:
    print("\n🧮 Calcul terminé avec succès")