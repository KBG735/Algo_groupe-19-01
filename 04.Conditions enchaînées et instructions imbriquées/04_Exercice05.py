print("🍽️ Système de commande de repas\n")

plat = input("Choisissez un plat (viande/poisson/végétarien) : ").lower()

if plat == "viande":
    cuisson = input("🔥 Cuisson (saignant/à point/bien cuit) : ").lower()
    print(f"\n✅ Commande : Viande {cuisson}")
    print("🥩 Accompagnement : Frites fraîches et légumes grillés")
elif plat == "poisson":
    sauce = input("🍋 Sauce (citron/beurre blanc) : ").lower()
    print(f"\n✅ Commande : Poisson sauce {sauce}")
    print("🐟 Accompagnement : Riz basmati et asperges")
elif plat == "végétarien":
    choix = input("🥗 Préférez-vous salade ou pâtes ? ").lower()
    if choix == "salade":
        print("\n✅ Commande : Grande salade composée")
        print("🥑 Ingrédients : Avocat, noix, chèvre, tomates cerises")
    else:
        print("\n✅ Commande : Pâtes végétariennes")
        print("🍝 Sauce au choix : Pesto ou tomate fraîche")
else:
    print("\n❌ Option non disponible")
    print("Veuillez choisir parmi : viande/poisson/végétarien")

print("\nBon appétit ! 😊")