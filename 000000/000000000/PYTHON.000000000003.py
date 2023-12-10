import numpy
print("this is double assistant")
while True:
    print("""Choose the Number of the Assistan you want to use.
        1. Circle Assistant
        2. Satz des Pythagoras Assistant
    """)
    Number = input("Number: ")
    if Number == "1":
        import math
        import time
        print("This is the Circle Assistant")
        Loop = True
        
        print("""Please select one of the following options with the keywords below in the []
            1. get the circle circumference [circumference]
            2. get the circle volume [volume]
        """
        )
        option = input("Keyword: ")
        if option.upper() == "Circumference".upper():
                radius = int(input("What is the circle radius?: "))
                circumference = math.pi * radius * 2
                print(f"The circumference is {circumference}.")
        elif option.upper() == "volume".upper():
            radius = int(input("What is the circle radius?: "))
            volume = math.pi * (radius**2)
            print(f"the volume is {volume}.")
        else:
            for i in range(0, 1000):
                print()
            print(f"ERROR: Unknown option! You put in \"{option}\".")
            time.sleep(1)
        for i in range(0, 1000):
                print()
    if Number == "2":
        import math
        print("This is german!")
        print("Willkommen zum Satz des Pythagoras Assistenten")
        print("""Willst du a, b oder c als Ergebnis haben?
            """)
        Result = "ERROR: option not found"
        option = input("Option: ").upper()
        if option == "A":
            c = float(input("Was ist der Wert von c: "))
            b = float(input("Was ist der Wert von b: "))
            x = c**2 - b**2
            a = numpy.sqrt(x)
            Result = a
        elif option == "B":
            c = float(input("Was ist der Wert von c: "))
            a = float(input("Was ist der Wert von a: "))
            x = c**2 - a**2
            b = numpy.sqrt(x)
            Result = b
        elif option == "C":
            a = float(input("Was ist der Wert von a: "))
            b = float(input("Was ist der Wert von b: "))
            x = a**2 + b**2
            c = numpy.sqrt(x)
            Result = c
        else:
            print("Error: Invalid option")
        print(f"The Result is: {Result}")
                
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    