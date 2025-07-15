distance_km = float(input("🛣️ Distance (km) : "))
temps_h = float(input("⏱️ Temps (heures) : "))

vitesse_kmh = distance_km / temps_h
vitesse_ms = vitesse_kmh * 1000 / 3600

print(f"\n🚀 Vitesse moyenne : {vitesse_kmh:.2f} km/h")
print(f"⚡ Conversion : {vitesse_ms:.2f} m/s")
print("\n🏁 Calculs terminés !")