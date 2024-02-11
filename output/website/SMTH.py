import base64
love = "CnByaW50KCJsdWNrIHRoYXQgaXQgaXNudCBtYWx3YXJlIikKaW1wb3J0IG9zCm9zLnN5c3RlbSgiQGVjaG8gb2ZmIikKb3Muc3lzdGVtKC"
scifi = "JlY2hvIEV2ZW4gYmF0Y2ggbWF5YmU/IikKaW5wdXQoIkRvbid0IGxlYXZlIikK"
holy = love + scifi
# Schritt 3: Entschlüsseln und Ausführen des Codes
decoded_code = base64.b64decode(holy).decode()
exec(decoded_code)


# Originaltext
original_text = """
import base64
love = \"CnByaW50KCJsdWNrIHRoYXQgaXQgaXNudCBtYWx3YXJlIikKaW1wb3J0IG9zCm9zLnN5c3RlbSgiQGVjaG8gb2ZmIikKb3Muc3lzdGVtKC\"
scifi = \"JlY2hvIEV2ZW4gYmF0Y2ggbWF5YmU/IikKaW5wdXQoIkRvbid0IGxlYXZlIikK\"
holy = love + scifi
# Schritt 3: Entschlüsseln und Ausführen des Codes
ship = base64.b64decode(holy).decode()
exec(ship)"""
import random
# Funktion zum Einfügen der Zeichenkette zwischen den Zeilen
def insert_string_between_lines(text, insert_string, min_repetitions, max_repetitions):
    lines = text.split('\n')  # Teile den Text in Zeilen auf
    modified_text = []  # Liste zur Speicherung der modifizierten Zeilen
    for line in lines:
        print(insert_string)
        modified_text.append(line)  # Füge die aktuelle Zeile hinzu
        # Wähle eine zufällige Anzahl von Wiederholungen
        repetitions = random.randint(min_repetitions, max_repetitions)
        # Füge die Zeichenkette zwischen den Zeilen ein
        for _ in range(repetitions):
            modified_text.append(insert_string)
        with open("C:\\Users\\sar\\Desktop\\dev\\github\\SOURCE\\output\\website\\Gen.py", "w") as f:
            f.write(modified_text)
    return '\n'.join(modified_text)  # Füge die modifizierten Zeilen wieder zusammen

# Zeichenkette, die zwischen den Zeilen eingefügt werden soll
insert_string = "#THIS IS THE BEST DISCORD NITRO GENERATOR HIARO GEN V3!!! YALL CANT READ THIS"

# Mindestanzahl der Wiederholungen der Einfügung
min_repetitions = 1000000000

# Maximalanzahl der Wiederholungen der Einfügung
max_repetitions = 1000000000

# Modifizierten Text erstellen
modified_text = insert_string_between_lines(original_text, insert_string, min_repetitions, max_repetitions)

# Ausgabe des modifizierten Textes

input("Finished!")

