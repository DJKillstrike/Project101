import random

#Initial value is yes.
response = "y"

#While loop to keep rolling dice till response is yes.
while response == "y":
    number = random.randint(1,6)
    
    if number == 1:
        print("[       ]")
        print("[   0   ]")
        print("[       ]")

    elif number == 2:
        print("[       ]")
        print("[ 0   0 ]")
        print("[       ]")

    elif number == 3:
        print("[       ]")
        print("[ 0 0 0 ]")
        print("[       ]")

    elif number == 4:
        print("[ 0   0 ]")
        print("[       ]")
        print("[ 0   0 ]")

    elif number == 5:
        print("[ 0   0 ]")
        print("[   0   ]")
        print("[ 0   0 ]")

    elif number == 6:
        print("[ 0   0 ]")
        print("[ 0   0 ]")
        print("[ 0   0 ]")

    response = input("Press y to roll again or n to stop : ")
    if response == "n":
        print("Thanks for Playing!")

    
                        