import random
options = ("Rock", "Paper", "Scissors")

running = True

while running:
    comp = random.choice(options)
    user = None

    while user not in options :
        user = input("Enter a choice(Rock, Paper, Scissors) : ")

    print("Player : " + user)
    print("Computer : " + comp)
    if user == comp:
        print("It's a tie!")
    elif user == "Rock" and comp == "Scissors":
        print("You win!")
    elif user == "Paper" and comp == "Rock":
        print("You win!")
    elif user == "Scissor" and comp == "Paper":
        print("You win!")
    else:
        print("Oops, Better luck next time!")

    x = input("Play again? (y/n) : ").lower()

    if x != "y" :
        running = False
print("Thanks for playing! ")



    
