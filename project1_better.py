import random 
 
class Hangmangame:
    def __init__(self, word_list, max_attempts=6):
         self.word_to_guess=random.choice(word_list) #stores a randomly chosen word 
         self.word_display=["_"] * len(self.word_to_guess) #is a list of underscores (_), representing each letter in
         self.max_attempts=max_attempts #stores the maximum number of incorrect guesses allowed.
         self.incorrect_guess=False
         self.guesssed_letters=set() # is a set that keeps track of all the letters the player has guessed so far. Using a set helps ensure that there are no duplicate guesses.
         
    def play(self): #game loop and handles all the game logic.
        
        while self.incorrect_guess<self.max_attempts and "_" in self.word_display: #The game continues as long as the player has not all allowed incorrect guesses
            print("Word:", "". join(self.word_display))
            guess =input("guess a letter:").lower() #The player is prompted to guess a letter
            
            if len(self.word_to_guess) != 1 or not guess.isalpha() or guess in self.guessed_letters:
                print("Repeated guess. Try agian!.")
                continue
            #len(guess) != 1: Ensures the input is exactly one character.
            #not guess.isalpha(): Checks that the input is a letter (not a number or symbol).
            #guess in self.guessed_letters: Checks if the letter has already been guessed.
            
            
            self.guesssed_letters.add(guess)
            if guess in self.word_to_guess:
                for i, letter in enumerate(self.word_to_guess): #iterates through each letter and its index in
                    if letter==guess:
                        self.word_display[i]=guess
            else: 
                self.incorrect_guess +=1
                
                print(f" Incorrect! {self.max_attempts -self.incorrect_guess}")
                
        if "_" not in self.word_display:
             print(f"Sorry, you rant out of guesses. The word was: {self.word_to_guess}")
        else:
            print(f"Congartulations! You 've guessed the word: {self.word_to_guess} ")
                
                
                
                        
         
word_list = ["pyhton ", "developer","admin", "AI", "computer"]
game=Hangmangame(word_list)
game.play()

