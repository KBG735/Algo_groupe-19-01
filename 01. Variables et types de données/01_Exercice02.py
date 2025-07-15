nom_produit = "casque Bluetooth"
prix = 150.0
stock = 35
remise = 0.15

prix_final = prix * (1 - remise)

print("\n🛒 FICHE PRODUIT 🛒")
print(f"🔹 Nom : {nom_produit}")
print(f"💰 Prix initial : {prix} €")
print(f"🎁 Remise : {remise * 100}%")
print(f"💶 Prix final : {prix_final:.2f} €")
print(f"📦 Stock : {stock} unités")
print("\n⚡ Équipez-vous dès maintenant !")