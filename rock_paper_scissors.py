import random

while True:
    user_action = input("Enter a choice(rock, paper, scissors):")

    possible_action = ["rock","paper", "scissors"]

    computer_action= random.choice(possible_action)

    print(f"\nYou chose{user_action}, computer chose{computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!!")

    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors!! You win")
        else:
            print("paper covers rock!! You lose")

    elif user_action =="paper":
        if computer_action == "rock":
            print("paper covers rock you win")
        else:
            print("Scissors cut paper you lose")

    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cut paper you win")

        else:
            print("Rock smashes scissors you lose")

    play_again = input("Play again? (Yes/ No)")
    if play_again != "yes" or "Yes":
        break

