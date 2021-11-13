def introduction():
    print("Welcome!")

def gradePUP():
    while True:
        try:
            gradeInput = int(input("Input Your Grade: "))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if gradeInput >= 101:
            print("That was above the limit of grades.")
            continue
        if gradeInput >= 97 and gradeInput <= 100:
            print("Grade Mark: 1.0")
            print("Description: Excellent")
            break
        elif gradeInput >= 94 and gradeInput <= 96:
            print("Grade Mark: 1.25")
            print("Description: Excellent")
            break
        elif gradeInput >= 91 and gradeInput <= 93:
            print("Grade Mark: 1.5")
            print("Description: Very Good")
            break
        elif gradeInput >= 88 and gradeInput <= 90:
            print("Grade Mark: 1.75")
            print("Description: Very Good")
            break
        elif gradeInput >= 85 and gradeInput <= 87:
            print("Grade Mark: 2.0")
            print("Description: Good")
            break
        elif gradeInput >= 82 and gradeInput <= 84:
            print("Grade Mark: 2.25")
            print("Description: Good")
            break
        elif gradeInput >= 79 and gradeInput <= 81:
            print("Grade Mark: 2.5")
            print("Description: Satisfactory")
            break
        elif gradeInput >= 76 and gradeInput <= 78:
            print("Grade Mark: 2.75")
            print("Description: Satisfactory")
            break
        elif gradeInput == 75:
            print("Grade Mark: 3.0")
            print("Description: Passing")
            break
        elif gradeInput >= 65 and gradeInput <= 74:
            print("Grade Mark: 5.0")
            print("Description: Failure")
            break
        else:
            print("It seems you haven't input your percentage grade, Are you one of the following?")
            print("Incomplete, Withdrawn, Dropped")  
            while True:
                inWiDro = str(input("Y or N = "))
                if inWiDro == "Y":
                    while True:
                        print("Type the number of your category:")
                        print("1 = Incomplete, 2 = Withdrawn, 3 = Dropped")
                        categoryLetter = str(input("Input Number: "))
                        if categoryLetter == "1":
                            print("Grade: Inc.")
                            break
                        elif categoryLetter == "2":
                            print("Grade: W")
                            break
                        elif categoryLetter == "3":
                            print("Grade: D")
                            break
                        else:
                            print("Sorry, I didn't understand that.")
                            continue
                    break
                
                elif inWiDro == "N":
                    print("You should enter your grades again.")
                    gradePUP()
                    break

                else:
                    print("Sorry, I didn't understand that.")
                    continue
        break
    

introduction()
gradePUP()