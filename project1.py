#Projekt 1: Hangman
#Skapa en version av det klassiska spelet Hangman.

#Datorn väljer ett slumpmässigt ord från en fördefinierad lista av ord.

#Spelet visar hur många bokstäver ordet består av, men inte vilka bokstäver som är rätt.

#Spelaren ska gissa en bokstav i taget, och datorn ger feedback om bokstaven finns i ordet eller inte.

#Spelet fortsätter tills spelaren har gissat hela ordet eller har gjort tillräckligt många felaktiga gissningar.


#SOLUTION
#STEP1: choose the words and create a list of words where the computer can randomly select from the game
#improt random
#randomly select the word from the existing list 
import random
words=["python", "AI", "hangman", "developer", "computer", "computer science"]
word_to_guess=random.choice(words)


#STEP2 DISPLAY UNDERSCORES FOR TEH WORD
#before the playes guesses, display the words as a series of unerscores prepreseting each letter in the word list

word_display= ["_" for _ in word_to_guess] #display as ['_', '_', '_', '']

#STEP3: TRACK GUESSES AND INCORRECT ATTEMPTS

max_incorrect_guesses=6
incorrect_guesses=0
correct_guesses=set()
guessed_letters=set() #to keep tack of all gueseed letters


#STEP 4 GAME LOOP
while incorrect_guesses < max_incorrect_guesses and "_" in word_display:
    print("word:", "".join(word_display))
    guess=input("guess a letter").lower()
    
#Ensure the input is a single letter and hasnot been guessed before being
    if len(guess) !=1 or not guess.isalpha():
        print("pls enter a valid single letter.")
        continue
    if guess in guessed_letters:
        print("You've already guessed that letter. Try agian.")
        continue
    
#check if the guess is correct or incorrect
if guess in word_to_guess:
    #update display for correct guesses
    for index, letter in enumerate(word_to_guess):
        if letter==guess:
            word_display[index] = guess
        correct_guesses.add(guess)
else:
    #handle the incorrect guess
    incorrect_guesses+=1
    print(f"Incorrect guess! You have {max_incorrect_guesses -incorrect_guesses} guesses left.")

#STEP5: END THE GAME

if "_" not in word_display:
    print("Congratulation! You' ve guessed the word:", word_to_guess)
else:
    print("Sorry, you' ve runt out of guesses. The word was:", word_to_guess)
        
        


