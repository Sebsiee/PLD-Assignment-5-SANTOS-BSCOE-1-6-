def introduction():
    print("Welcome to my Program 2 - Lowest Number!")

def lowestNumber():
    while True:
        try:
            firstInput = int(input("Input 1st Number: "))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        else:
            break

    while True:
        try:
            secondInput = int(input("Input 2nd Number: "))
        except ValueError:  
            print("Sorry, I didn't understand that.")
            continue
        else:
            break

    while True:
        try:
            thirdInput = int(input("Input 3rd Number: "))
        except ValueError:  
            print("Sorry, I didn't understand that.")
            continue
        else:
            break
        
    print(f"Your three numbers are: {firstInput}, {secondInput}, {thirdInput}")
    if firstInput < secondInput and thirdInput:
        print("The lowest number is: ", firstInput)
    elif secondInput < firstInput and thirdInput:
        print("The lowest number is: ", secondInput)
    elif thirdInput < firstInput and secondInput:
        print("The lowest number is: ", thirdInput)
    elif firstInput == secondInput == thirdInput:
        print("You entered 3 identical numbers so there's no lowest nor highest number!")

def goodbye():
    print()
    print("Thank you for using my program!")

introduction()
lowestNumber()
goodbye()