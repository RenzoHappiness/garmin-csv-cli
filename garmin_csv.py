import csv 
from pathlib import Path 
datei_pfad = Path("data/sample/activities.csv")

with open(datei_pfad, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    zeilen_liste = list(reader)
    anzahl = len(zeilen_liste)
    print(anzahl)


