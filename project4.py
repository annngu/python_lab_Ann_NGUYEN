#Step-by-Step Breakdown for the Blackjack Game:
#Step 1: Define a Deck of Cards
#A standard deck of cards has 52 cards, with values 2-10, J, Q, K (all worth 10), and Ace (worth 1 or 11 depending on the situation).
#Step 2: Shuffle the Deck
#Shuffle the deck at the beginning of each round.
#Step 3: Deal Initial Cards
#Deal two cards to the player and two cards to the computer (one card face-up for the computer).
#Step 4: Player’s Turn
#The player can choose to:
#Hit (draw another card) until they either go over 21 or decide to stand.
#Stand (stop drawing cards and lock in their current total).
#Step 5: Computer’s Turn
#The computer must draw cards (hit) until its total is 17 or more. It must stop drawing once it reaches 17 or higher.
#Step 6: Determine the Winner
#If either the player or computer goes over 21, they lose.
#If both are under 21, the player with the higher total wins.



###SOLUTION 

import random

# Step 1: Define the deck of cards
def create_deck():
    """Creates a standard deck of 52 cards."""
    deck = []
    # Add cards 2 to 10 for each suit
    for i in range(2, 11):
        deck += [str(i)] * 4  # 4 suits for each value
    # Add face cards (J, Q, K worth 10 points)
    deck += ['J', 'Q', 'K'] * 4
    # Add Aces (worth 1 or 11 points)
    deck += ['A'] * 4
    return deck

def shuffle_deck(deck):
    """Shuffles the deck."""
    random.shuffle(deck)

# Step 2: Assign values to cards
def card_value(card):
    """Returns the point value of a card."""
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 11  # Aces are worth 11 initially, we will adjust if necessary later
    else:
        return int(card)

def calculate_hand_total(hand):
    """Calculates the total points in a hand, adjusting for Aces."""
    total = sum(card_value(card) for card in hand)
    # Adjust for Aces if necessary
    ace_count = hand.count('A')
    while total > 21 and ace_count:
        total -= 10  # Convert Ace from 11 to 1
        ace_count -= 1
    return total

# Step 3: Deal initial cards
def deal_card(deck):
    """Deals one card from the deck."""
    return deck.pop()

def initial_deal(deck):
    """Deals two cards to both the player and the computer."""
    player_hand = [deal_card(deck), deal_card(deck)]
    computer_hand = [deal_card(deck), deal_card(deck)]
    return player_hand, computer_hand

# Step 4: Player's turn (Hit or Stand)
def player_turn(deck, player_hand):
    """Handles the player's turn."""
    while True:
        print(f"Your hand: {player_hand} (total: {calculate_hand_total(player_hand)})")
        choice = input("Do you want to hit or stand? (hit/stand): ").lower()
        if choice == 'hit':
            player_hand.append(deal_card(deck))
            if calculate_hand_total(player_hand) > 21:
                print(f"Your hand: {player_hand} (total: {calculate_hand_total(player_hand)})")
                print("You went over 21! You lose.")
                return False
        elif choice == 'stand':
            break
        else:
            print("Invalid input. Please enter 'hit' or 'stand'.")
    return True

# Step 5: Computer's turn
def computer_turn(deck, computer_hand):
    """Handles the computer's turn."""
    while calculate_hand_total(computer_hand) < 17:
        computer_hand.append(deal_card(deck))
    return calculate_hand_total(computer_hand)

# Step 6: Determine the winner
def determine_winner(player_hand, computer_hand):
    """Determines the winner of the game."""
    player_total = calculate_hand_total(player_hand)
    computer_total = calculate_hand_total(computer_hand)

    print(f"\nYour final hand: {player_hand} (total: {player_total})")
    print(f"Computer's final hand: {computer_hand} (total: {computer_total})")

    if computer_total > 21:
        print("The computer went over 21. You win!")
    elif player_total > computer_total:
        print("You win!")
    elif player_total < computer_total:
        print("The computer wins!")
    else:
        print("It's a tie!")

# Main game function
def play_blackjack():
    """Main function to play the game."""
    deck = create_deck()
    shuffle_deck(deck)

    # Step 3: Deal initial cards
    player_hand, computer_hand = initial_deal(deck)
    
    print(f"Computer shows: {computer_hand[0]}")
    print(f"Your hand: {player_hand} (total: {calculate_hand_total(player_hand)})")

    # Step 4: Player's turn
    if player_turn(deck, player_hand):
        # Step 5: Computer's turn
        computer_total = computer_turn(deck, computer_hand)
        
        # Step 6: Determine winner
        determine_winner(player_hand, computer_hand)

# Start the game
play_blackjack()
