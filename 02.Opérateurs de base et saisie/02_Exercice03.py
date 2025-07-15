montant_ht = float(input("💰 Montant HT (€) : "))
taux_tva = float(input("📊 Taux de TVA (%) : "))

taux_coef = taux_tva / 100
montant_ttc = montant_ht * (1 + taux_coef)

print(f"\n🧾 Facture :")
print(f"➖ HT : {montant_ht:.2f}€")
print(f"➕ TVA ({taux_tva}%) : {montant_ht * taux_coef:.2f}€")
print(f"✅ TTC : {montant_ttc:.2f}€")
print("\n💳 Prêt à régler !")