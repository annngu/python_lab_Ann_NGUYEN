#Step-by-Step Breakdown for the Rock-Scissors-Bag Game:
#Step 1: Define Possible Choices
#Both the player and the computer can choose between "rock", "scissors", or "bag".
#Step 2: Computer Makes a Random Choice
#Use Python's random module to make the computer randomly select one of the three choices.
#Step 3: Player Makes a Choice
#Ask the player to input their choice: "rock", "scissors", or "bag". Ensure the input is valid.
#Step 4: Determine the Winner
#Define the game rules:
#Rock beats Scissors.
#Scissors beat Bag.
#Bag beats Rock.
#If both players choose the same option, it's a tie.
#Step 5: Display the Results
#Display the choices of both the player and the computer and determine who wins.
#Step 6: Continue Until Win or Loss
#The game should continue until the player wins or loses (ignoring ties).


#ROCK SCISSORS - BAG GAME:

#SOLUTION


import random

def get_computer_choice():
    """Randomly chooses rock, scissors, or bag for the computer."""
    choices = ['rock', 'scissors', 'bag']
    return random.choice(choices)

def get_player_choice():
    """Gets the player's choice and validates it."""
    while True:
        choice = input("Choose rock, scissors, or bag: ").lower()
        if choice in ['rock', 'scissors', 'bag']:
            return choice
        else:
            print("Invalid choice. Please try again.")

def determine_winner(player, computer):
    """Determines the winner based on the game rules."""
    if player == computer:
        return "tie"
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'scissors' and computer == 'bag') or \
         (player == 'bag' and computer == 'rock'):
        return "player"
    else:
        return "computer"

def play_game():
    """Main function to play the Rock-Scissors-Bag game."""
    
    while True:
        # Step 2: Computer makes a random choice
        computer_choice = get_computer_choice()
        
        # Step 3: Player makes a choice
        player_choice = get_player_choice()
        
        # Step 5: Show choices
        print(f"\nYou chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        
        # Step 4: Determine the winner
        winner = determine_winner(player_choice, computer_choice)
        
        # Step 6: Show result and end the game if no tie
        if winner == "tie":
            print("It's a tie! Try again.\n")
        elif winner == "player":
            print("Congratulations! You win!\n")
            break
        else:
            print("You lose! The computer wins.\n")
            break

# Run the game
play_game()
