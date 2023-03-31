import random

def get_user_choice():
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def play_round():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    if user_choice == computer_choice:
        print("It's a tie!")
        return "tie"
    elif user_choice == "rock" and computer_choice == "scissors" or \
         user_choice == "paper" and computer_choice == "rock" or \
         user_choice == "scissors" and computer_choice == "paper":
        print("You win!")
        return "user"
    else:
        print("Computer wins!")
        return "computer"

def play_game():
    num_rounds = 0
    num_user_wins = 0
    num_computer_wins = 0
    while True:
        print(f"\nRound {num_rounds + 1}")
        result = play_round()
        if result == "user":
            num_user_wins += 1
        elif result == "computer":
            num_computer_wins += 1
        num_rounds += 1
        print(f"\nScore: You {num_user_wins}, Computer {num_computer_wins}")
        play_again = input("\nDo you want to play another round? (y/n) ").lower()
        if play_again != "y":
            break

play_game()
