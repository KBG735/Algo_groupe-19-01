from datetime import datetime

activite = input("Décrivez votre activité du jour : ")

with open("journal.txt", "a", encoding="utf-8") as f:
    now = datetime.now().strftime("%d/%m/%Y %H:%M")
    f.write(f"[{now}] {activite}\n")

print("Activité ajoutée avec succès dans 'journal.txt'.")