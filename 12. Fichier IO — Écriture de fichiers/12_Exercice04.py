notes = [float(x) for x in input("Entrez des notes séparées par des espaces : ").split() if x.replace('.', '').isdigit()]
moyenne = sum(notes) / len(notes) if notes else 0

with open("statistiques.txt", "w", encoding="utf-8") as f:
    f.write(f"Notes : {notes}\n")
    f.write(f"Moyenne : {moyenne:.2f}\n")
    f.write(f"Note max : {max(notes) if notes else 'N/A'}\n")
    f.write(f"Note min : {min(notes) if notes else 'N/A'}\n")

print("Statistiques sauvegardées dans 'statistiques.txt'.")