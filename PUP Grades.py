def introduction():
    print("Welcome!")

def gradePUP():
    gradeInput = int(input("Input Your Grade: "))
    if gradeInput >= 97 and gradeInput <= 100:
        print("Grade Mark: 1.0")
        print("Description: Excellent")
    elif gradeInput >= 94 and gradeInput <= 96:
        print("Grade Mark: 1.25")
        print("Description: Excellent")
    elif gradeInput >= 91 and gradeInput <= 93:
        print("Grade Mark: 1.5")
        print("Description: Very Good")
    elif gradeInput >= 88 and gradeInput <= 90:
        print("Grade Mark: 1.75")
        print("Description: Very Good")
    elif gradeInput >= 85 and gradeInput <= 87:
        print("Grade Mark: 2.0")
        print("Description: Good")
    elif gradeInput >= 82 and gradeInput <= 84:
        print("Grade Mark: 2.25")
        print("Description: Good")
    elif gradeInput >= 79 and gradeInput <= 81:
        print("Grade Mark: 2.5")
        print("Description: Satisfactory")
    elif gradeInput >= 76 and gradeInput <= 78:
        print("Grade Mark: 2.75")
        print("Description: Satisfactory")
    elif gradeInput == 75:
        print("Grade Mark: 3.0")
        print("Description: Passing")
    elif gradeInput >= 65 and gradeInput <= 74:
        print("Grade Mark: 5.0")
        print("Description: Failure")
    else:
        print("It seems you haven't input your percentage grade, Are you one of the following?")
        print("Incomplete, Withdrawn, Dropped")  
        inWiDro = str(input("Y or N = "))
        if inWiDro == "Y":
            print("Type the letter of your category:")
            print(" I = Incomplete, W = Withdrawn, D = Dropped")
            categoryLetter = str(input("= "))
            if categoryLetter == "I":
                print("Grade: Inc.")
            elif categoryLetter == "W":
                print("Grade: W")
            elif categoryLetter == "D":
                print("Grade: D")

        if inWiDro == "N":
            print("Input your grade again.")

introduction()
gradePUP()