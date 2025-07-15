a = float(input("🔢 Premier nombre : "))
b = float(input("🔢 Deuxième nombre : "))

somme = a + b
difference = a - b
produit = a * b
quotient = a / b if b != 0 else "∞"
division_entiere = a // b if b != 0 else "∞"
reste = a % b if b != 0 else "∞"

print(f"\n🧮 Résultats :")
print(f"➕ Somme : {somme}")
print(f"➖ Différence : {difference}")
print(f"✖️ Produit : {produit}")
print(f"➗ Quotient : {quotient}")
print(f"⏏️ Division entière : {division_entiere}")
print(f"🔍 Reste : {reste}")
print("\n✨ Opérations terminées !")