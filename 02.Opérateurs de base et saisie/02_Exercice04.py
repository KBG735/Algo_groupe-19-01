note1 = float(input("📝 Note 1 : "))
note2 = float(input("📝 Note 2 : "))
note3 = float(input("📝 Note 3 : "))

moyenne = (note1 + note2 + note3) / 3

print(f"\n📊 Moyenne : {moyenne:.2f}/20")
if moyenne >= 10:
    print("✅ Admis ! Félicitations 🎉")
else:
    print("❌ Non admis - Courage pour la prochaine fois 💪")
print("\n🔍 Résultat officiel")