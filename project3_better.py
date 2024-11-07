import random 

class RockScissorBagGame:
    def __init__(self):
        self.choices =["rock","scissors","bag"]

    def get_choices(self, prompt):
        return random.choice(self.choices) if prompt =="computer" else self.validate_choice()#get a valid choice from the playe
    #getting a choice from either the computer or the player. och prompt is computer
    
    
    #loop continues to prompt the player until a valid choice
    def validate_choice(self):
        while (choice:=input("Choose rock, scissors, or bag:").lower()) not in self.choices: #assign and check choice in one line. The input is converted to lowercase for consistency.
            print("Invalid choice. Pls try agian.")
        return choice
    
    #determines the winner of the game
    def who_is_thewinner(self, player, computer):
        if player==computer: return "IT'S A TIE! TRY AGIAN."
        outcomes={"rock": "scissors", "scissors": "bag", "bag": "rock"}
        return " CONGRAT! YOU WIN!" if outcomes[player] ==computer else "You lose! Computer wins!"
    
    def play(self):
        while True:
            player =self.get_choices("player")
            computer =self.get_choices("computer")
            print(f"\n you chose:{player}\n Computer chose:{computer}")
            result =self.who_is_thewinner(player,computer) #called to decide the outcome, and the result is printed.
            print(result)
            if "tie" not in result:break
RockScissorBagGame().play()