# Version optimisée avec compréhension de liste
carres = [i**2 for i in range(1, 21)]

print("🔢 Carrés des nombres de 1 à 20 :")
print(carres)

print("\n🚀 Carrés supérieurs à 100 :")
grands_carres = [x for x in carres if x > 100]
print(grands_carres if grands_carres else "Aucun carré > 100")

# Bonus : Statistiques
print(f"\n📊 Statistiques :")
print(f"- Nombre total : {len(carres)}")
print(f"- Plus grand carré : {max(carres)}")
print(f"- Somme des carrés : {sum(carres)}")