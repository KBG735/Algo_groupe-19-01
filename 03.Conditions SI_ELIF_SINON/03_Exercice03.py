panier = float(input("🛒 Montant du panier (€) : "))

if panier >= 100:
    frais = 0
    message = "🎉 Livraison OFFERTE !"
elif panier >= 50:
    frais = 5
    message = "🚚 Frais réduits"
else:
    frais = 10
    message = "📦 Frais standard"

total = panier + frais

print(f"\n💳 Facture :")
print(f"- Sous-total : {panier:.2f}€")
print(f"- Livraison : {frais}€ ({message})")
print(f"💶 TOTAL : {total:.2f}€")
print("\nMerci pour votre commande ! ❤️")