import os
import random

def clear_screen():
    if os.name == 'nt':
        os.system('cls')

def display_menu():
    clear_screen()
    print("Welcome to Rock, Paper, Scissors Game!")
    print("1. Play Game")
    print("2. Instructions")
    print("3. Quit")

def display_instructions():
    clear_screen()
    print("Instructions:")
    print("- You will play against the computer.")
    print("- Enter your choice: 'rock', 'paper', or 'scissor'.")
    print("- The computer will randomly select its choice.")
    print("- The winner is determined by the rules: Rock beats Scissor, Scissor beats Paper, Paper beats Rock.")

def play_game():
    options = ("rock", "paper", "scissor")
    player_score = 0
    computer_score = 0

    while True:
        clear_screen()
        computer = random.choice(options)
        player = input("Enter your choice (rock, paper, scissor) or 'q' to quit: ").lower()

        if player == 'q':
            break

        if player not in options:
            print("Invalid choice. Please enter 'rock', 'paper', 'scissor' or 'q' to quit.")
            input("Press Enter to continue...")
            continue

        print(f"Player: {player}")
        print(f"Computer: {computer}")

        if player == computer:
            print("It's a tie!")
        elif (player == "rock" and computer == "scissor") or \
             (player == "scissor" and computer == "paper") or \
             (player == "paper" and computer == "rock"):
            print("You Win!")
            player_score += 1
        else:
            print("Computer Wins!")
            computer_score += 1

        print(f"Player Score: {player_score}  Computer Score: {computer_score}")
        input("Press Enter to continue...")

    print("Thanks for playing!")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            play_game()
        elif choice == '2':
            display_instructions()
            input("Press Enter to continue...")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
