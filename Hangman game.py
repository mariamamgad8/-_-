# Hangman in Python
import random
from tkinter import W

hangman_art = {                0: ("   ",
                                   "   ",
                                   "   "),
                               1: (" o ",
                                   "   ",
                                   "   "),
                               2: (" o ",
                                   " | ",
                                   "   "),
                               3: (" o ",
                                   "/| ",
                                   "   "),
                               4: (" o ",
                                   "/|\\",
                                   "   "),
                               5: (" o ",
                                   "/|\\",
                                   "/  "),
                               6: (" o ",
                                   "/|\\",
                                   "/ \\")}

words = ("Orange","Black","Red","White","Green","Grey","Violet","Yellow","Purple","Pink","Mustard","Bronze","Brown","Silver","Mint","Mocha","Lavender","Turquoise")

def display_man(wrong_guesses):
    print("*************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("*************")

def display_hint(hint):
    print(" ".join(hint))


def main():
    
    print("Let's play Hangman!")
    answer = random.choice(words).upper()
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = []
    guessed_words = []
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a guess: ").upper()

        if len(guess) == 1 and guess.isalpha():
             if guess in guessed_letters :
                 print(f"{guess} is already guessed")
       
             elif guess in answer:
                 print("Good job,", guess, "is in the word!")
                 for i in range(len(answer)):
                    if answer[i] == guess:
                      hint[i] = guess
                 guessed_letters.append(guess)
                   
             else:
                print(guess, "is not in the word.")
                wrong_guesses += 1
                guessed_letters.append(guess)
                

              
        elif len(guess) == len(answer) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
                
                
            elif guess != answer:
                print(guess, "is not the word.")
                wrong_guesses += 1
                guessed_words.append(guess)
                
            else:
                is_running= False
                print("Congrats, you guessed the word! You win!")
                  
                
        else :
            print("Not a valid guess.")
            
        if "_" not in hint:
            display_man(wrong_guesses)
            print("Congrats, you guessed the word " + answer.upper()+" !")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            print("Sorry, you ran out of tries. The word was " + answer.upper())
            is_running = False
            

    while input("Play Again? (Y/N) ").upper() == "Y":
             return main()
              
main()
