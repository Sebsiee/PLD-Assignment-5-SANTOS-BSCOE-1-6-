def introduction():
    print("Welcome!")

def lowestNumber():
    firstInput = int(input("Input 1st Number: "))
    secondInput = int(input("Input 2nd Number: "))
    thirdInput = int(input("Input 3rd Number: "))
    if firstInput < secondInput and thirdInput:
        print("The lowest number is ", firstInput)
    if secondInput < firstInput and thirdInput:
        print("The lowest number is ", secondInput)
    if thirdInput < firstInput and secondInput:
        print("The lowest number is ", thirdInput)

introduction()
lowestNumber()