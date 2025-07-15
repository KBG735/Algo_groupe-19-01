nombre = int(input("🔢 Entrez un nombre pour sa table de multiplication : "))

print(f"\n✨ Table de multiplication de {nombre} ✨")
print("-------------------------")
for i in range(1, 13):
    resultat = nombre * i
    print(f"│ {nombre:2d} × {i:2d} = {resultat:3d} │")
print("-------------------------")

if nombre > 10:
    print("\n💡 Astuce : Essayez avec un nombre plus petit pour une table plus facile !")
elif nombre == 0:
    print("\n😂 La table de 0 est trop simple !")
else:
    print("\n🧠 Bravo pour votre pratique des mathématiques !")