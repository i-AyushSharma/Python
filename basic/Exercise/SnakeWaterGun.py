import random
choice = ["Snake", "Water", "Gun"]
computer = random.choice(choice)
a = print(computer)

user = input("Choose between Snake/Water/Gun : ")
a = user.lower()
if a == "snake":
    if computer == "Snake":
        print("TIE")
    elif computer == "Water":
        print("YOU WON!!")
    else:
        print("YOU LOSE!!")
elif a == "water":
    if computer == "Snake":
        print("YOU LOSE!!")
    elif computer == "Water":
        print("TIE")
    else:
        print("YOU WON!!")
elif a == "gun":
    match computer:
        case "Snake":
            print("YOU WON!!")
        case "Gun":
            print("TIE")
        case "Water":
            print("YOU LOSE!!")
    
else:
    print("Invalid Input")
print(f"Opponent's Choice : {computer}")


