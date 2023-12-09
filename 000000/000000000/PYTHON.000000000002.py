import math
print("This is german!")
print("Willkommen zum Satz des Pythagoras Assistenten")
print("""Willst du a, b oder c als Ergebnis haben?
      """)
Result = "ERROR: option not found"

while True:
    option = input("Option: ").upper()
    if option == "A":
        c = float(input("Was ist der Wert von c: "))
        b = float(input("Was ist der Wert von b: "))
        a = math.sqrt((c**2) - (b**2))
        Result = a
    if option == "B":
        c = float(input("Was ist der Wert von c: "))
        a = float(input("Was ist der Wert von a: "))
        b = math.sqrt((c**2) - (a**2))
        Result = b
    if option == "C":
        a = float(input("Was ist der Wert von a: "))
        b = float(input("Was ist der Wert von b: "))
        c = math.sqrt((a**2) + (b**2))
        Result = c
    print(f"The Result is: {Result}")