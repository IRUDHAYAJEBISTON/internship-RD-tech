import random

def get_user_choice():
    choice = input("Choose Rock, Paper, or Scissors: ").strip().lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid input. Try again.")
        choice = input("Choose Rock, Paper, or Scissors: ").strip().lower()
    return choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def display_result(user, computer, winner):
    print(f"\nYou chose: {user.capitalize()}")
    print(f"Computer chose: {computer.capitalize()}")
    if winner == "tie":
        print("It's a tie!\n")
    elif winner == "user":
        print("You win this round!\n")
    else:
        print("Computer wins this round!\n")

def play_game():
    user_score = 0
    computer_score = 0

    print("🎮 Welcome to Rock-Paper-Scissors Game!")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)

        display_result(user_choice, computer_choice, winner)

        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        print(f"Score => You: {user_score} | Computer: {computer_score}\n")

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("\nThanks for playing! Final Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            break

# Run the game
play_game()
