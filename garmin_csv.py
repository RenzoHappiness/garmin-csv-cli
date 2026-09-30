import csv 
from pathlib import Path 

path = Path("data/sample/activities.csv")


def load_activities(path: Path) -> list[dict[str, str]]:
    with open(path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)
        return rows
    
def total_distance(rows:list[dict[str,str]]) -> float:
    total = 0.0
    for row in rows:
        total += float(row['Distanz km'])
    return total

def main() -> None:
    rows = load_activities(path)
    distance = total_distance(rows)
    print(f"{len(rows)} activities, {distance:.1f} km")
main()