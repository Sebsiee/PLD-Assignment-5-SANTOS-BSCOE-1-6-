def introduction():
    print("Welcome!")

def lowestNumber():
    while True:
        try:
            firstInput = int(input("Input 1st Number: "))
            secondInput = int(input("Input 2nd Number: "))
            thirdInput = int(input("Input 3rd Number: "))
            break
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
    print(f"Your three numbers are: {firstInput}, {secondInput}, {thirdInput}")
    if firstInput < secondInput and thirdInput:
        print("The lowest number is: ", firstInput)
    elif secondInput < firstInput and thirdInput:
        print("The lowest number is: ", secondInput)
    elif thirdInput < firstInput and secondInput:
        print("The lowest number is: ", thirdInput)

introduction()
lowestNumber()