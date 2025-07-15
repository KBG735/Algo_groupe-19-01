usd = float(input("💵 Montant en USD : "))

eur = usd * 0.93
cfa = usd * 610
gbp = usd * 0.79

print(f"\n🌍 Conversion de {usd:.2f} USD :")
print(f"🇪🇺 EUR : {eur:.2f}€")
print(f"🇧🇯 CFA : {cfa:.0f} FCFA")
print(f"🇬🇧 GBP : £{gbp:.2f}")
print("\n💱 Conversion terminée !")