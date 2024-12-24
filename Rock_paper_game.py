import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == "rock":
        return "You win!" if computer_choice == "scissors" else "You lose!"
    elif user_choice == "paper":
        return "You win!" if computer_choice == "rock" else "You lose!"
    elif user_choice == "scissors":
        return "You win!" if computer_choice == "paper" else "You lose!"

# Main game function
def play_game():
    print("Welcome to Rock, Paper, Scissors!")

    # List of possible choices
    choices = ["rock", "paper", "scissors"]

    # Ask for the user's choice
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    
    # Check if the user's choice is valid
    if user_choice not in choices:
        print("Invalid choice. Please choose either rock, paper, or scissors.")
        return

    # Get the computer's choice randomly
    computer_choice = random.choice(choices)
    print(f"The computer chose: {computer_choice}")

    # Determine and print the winner
    result = determine_winner(user_choice, computer_choice)
    print(result)

# Loop to allow multiple rounds
def main():
    while True:
        play_game()

        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

# Start the game
if __name__ == "__main__":
    main()
