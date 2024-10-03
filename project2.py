import random

def get_difficulty_level():
    """Asks the user to choose a difficulty level."""
    print("Choose a difficulty level: Easy (3), Medium (5), Hard (7)")
    while True:
        try:
            level = input("Enter difficulty level (easy, medium, hard): ").lower()
            if level == 'easy':
                return 3
            elif level == 'medium':
                return 5
            elif level == 'hard':
                return 7
            else:
                print("Invalid input, please choose easy, medium, or hard.")
        except ValueError:
            print("Please enter a valid difficulty level.")

def generate_random_sequence(length):
    """Generates a random sequence of numbers or letters."""
    sequence = []
    for _ in range(length):
        choice = random.choice('abcdefghijklmnopqrstuvwxyz1234567890')
        sequence.append(choice)
    return sequence

def shuffle_sequence(sequence):
    """Shuffles the given sequence."""
    shuffled = sequence[:]
    random.shuffle(shuffled)
    return shuffled

def play_memory_game():
    """Main function to play the Memory game."""
    # Step 1: Choose difficulty
    length = get_difficulty_level()

    # Step 2: Generate a random sequence
    original_sequence = generate_random_sequence(length)
    print("Memorize this sequence: ", " ".join(original_sequence))

    input("\nPress Enter when you're ready to continue...")

    # Step 4: Shuffle the sequence and show the player
    shuffled_sequence = shuffle_sequence(original_sequence)
    print("\nShuffled sequence: ", " ".join(shuffled_sequence))

    # Step 5: Get player's guess for the original order
    while True:
        player_guess = input("\nEnter the original sequence (separate characters with space): ").split()

        # Step 6: Check if the player guessed correctly
        if player_guess == original_sequence:
            print("Congratulations! You guessed the correct sequence.")
            break
        else:
            print("Incorrect! Try again.")
            print("\nShuffled sequence: ", " ".join(shuffled_sequence))

# Run the Memory game
play_memory_game()
 