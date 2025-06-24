import random

def get_user_choice():
    while True:
        choice = input("Rock, Paper, or Scissors? ").strip().lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        print("Hmm... that wasn't a valid choice. Try again.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player, computer):
    if player == computer:
        return "tie"
    if (player == "rock" and computer == "scissors") or \
       (player == "scissors" and computer == "paper") or \
       (player == "paper" and computer == "rock"):
        return "player"
    return "computer"

def show_round_result(player, computer, winner):
    print(f"\nYou picked: {player.capitalize()}")
    print(f"Computer picked: {computer.capitalize()}")

    if winner == "tie":
        print("It's a tie!")
    elif winner == "player":
        print("Nice! You win this round.")
    else:
        print("Oops, computer wins this one.")

def play_game():
    player_score = 0
    computer_score = 0

    print("Let's play Rock-Paper-Scissors!\n")

    while True:
        player = get_user_choice()
        computer = get_computer_choice()
        winner = determine_winner(player, computer)

        show_round_result(player, computer, winner)

        if winner == "player":
            player_score += 1
        elif winner == "computer":
            computer_score += 1

        print(f"Current Score — You: {player_score}, Computer: {computer_score}\n")

        again = input("Play again? (yes/no): ").strip().lower()
        if again not in ['yes', 'y']:
            print("\nThanks for playing!")
            print(f"Final Score — You: {player_score}, Computer: {computer_score}")
            break

play_game()
