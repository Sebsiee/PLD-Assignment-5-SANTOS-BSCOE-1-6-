def introduction():
    print("Welcome!")

def lifeStage():
    while True:
        try:
            agePerson = int(input("How old are you? "))
        except ValueError:
            print("Enter a Number.")
            continue
        if agePerson >= 0 and agePerson <= 12:
            print("You're a Kid. How Cute!")
        elif agePerson >= 13 and agePerson <= 17:
            print("You're a Teen. How Cool!")
        elif agePerson == 18:
            print("You're a Debutant. How Nice!")   
        elif agePerson >= 19:
            print("You're an Adult. How Resoponsible!")
        break

introduction()
lifeStage()