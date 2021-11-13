def introduction():
    print("Welcome to my Program 1 - PUP Grades!")

def gradePUP():
    while True:
        try:
            inputGrade = float(input("Input Your Grade: "))
            roundedoffGrade = round(inputGrade)
            print("")
            print("Your grade is:", round(inputGrade))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if roundedoffGrade >= 101:
            print("That was above the limit of grades.")
            continue
        if roundedoffGrade >= 97 and roundedoffGrade <= 100:
            print("Grade Mark: 1.0")
            print("Description: Excellent")
        elif roundedoffGrade >= 94 and roundedoffGrade <= 96:
            print("Grade Mark: 1.25")
            print("Description: Excellent")
        elif roundedoffGrade >= 91 and roundedoffGrade <= 93:
            print("Grade Mark: 1.5")
            print("Description: Very Good")
        elif roundedoffGrade >= 88 and roundedoffGrade <= 90:
            print("Grade Mark: 1.75")
            print("Description: Very Good")
        elif roundedoffGrade >= 85 and roundedoffGrade <= 87:
            print("Grade Mark: 2.0")
            print("Description: Good")
        elif roundedoffGrade >= 82 and roundedoffGrade <= 84:
            print("Grade Mark: 2.25")
            print("Description: Good")
        elif roundedoffGrade >= 79 and roundedoffGrade <= 81:
            print("Grade Mark: 2.5")
            print("Description: Satisfactory")
        elif roundedoffGrade >= 76 and roundedoffGrade <= 78:
            print("Grade Mark: 2.75")
            print("Description: Satisfactory")
        elif roundedoffGrade == 75:
            print("Grade Mark: 3.0")
            print("Description: Passing")
        elif roundedoffGrade >= 65 and roundedoffGrade <= 74:
            print("Grade Mark: 5.0")
            print("Description: Failure")
        else:
            print("Are you one of the following?")
            print("Incomplete / Withdrawn / Dropped")  
            while True:
                inWiDro = str(input("Y or N: "))
                if inWiDro == "Y" or "y":
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
                
                elif inWiDro == "N" or "n":
                    print("You should enter your grades again.")
                    gradePUP()
                    break

                else:
                    print("Sorry, I didn't understand that.")
                    continue
        break

def goodbye():
    print()
    print("Thank you for using my program!")

introduction()
gradePUP()
goodbye()