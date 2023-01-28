import random

def play_game():
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    if user_choice not in options:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        return
    print("Computer chose: " + computer_choice)
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win!")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win!")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!")
    else:
        print("You lose.")

play_game()
