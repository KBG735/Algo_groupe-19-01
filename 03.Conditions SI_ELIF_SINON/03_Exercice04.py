temp = float(input("🌡️ Température (°C) : "))

print("\n☀️ Avis météo :")
if temp >= 35:
    print("🔥 Canicule !")
    print("💧 Restez hydraté et à l'ombre")
elif temp >= 25:
    print("☀️ Chaud")
    print("🕶️ Protégez-vous du soleil")
elif temp >= 15:
    print("🌤️ Agréable")
    print("😊 Profitez-en !")
else:
    print("❄️ Frais")
    print("🧣 Couvrez-vous bien")

print("\nPrenez soin de vous ! 💙")