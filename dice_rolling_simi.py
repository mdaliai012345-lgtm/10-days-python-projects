import random    # import random for random choice
while True:      # create a infinite loop for asking the user input 
    user = input("Roll the Dice? (y/n) : ").lower()

    if user == "y":                   # give condition for loop
        Dice = random.choice([1,2,3,4,5,6])
        print(Dice)
    elif user == "n":
        print("OVER")
        break
    else:
        print("Plese enter y or n : ")