import math
import time
print("This is the Circle Assistant")
Loop = True
while Loop:
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
            