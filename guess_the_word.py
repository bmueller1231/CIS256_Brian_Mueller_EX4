# Brian Mueller
# CIS256 Spring 2026
# Exercise Assignment 4
# Writing the Game (Hangman)

import random

def build_game_word_instance():
    '''Build the game word and dictionaries that will be used'''
    if len(game_word) == 0:
        word_list = ["beneficial", "excellent", "blackberry", "facetious",
                    "areious", "tragediously", "vigorously", "nocturnal",
                    "trebuchet", "powerful", "questionable", "pizzaria",
                    "monumental", "galantry", "capricious", "vacillation"]
        
        word = random.choice(word_list)
        word_index = 0
        
        for i in word:
            if word_index != len(word):
                game_word[word_index] = i.upper()
                guess_word[word_index] = "_"
                word_index += 1
        print(f"The word for this game is {len(game_word)} letters long.")
        print(" ".join(guess_word.values()))
    else:
        print("This game already has a word")

def letter_validation(guess_letter):
    '''Validation that the user has entered a single letter'''
    if guess_letter in guessed_letters:
        print("You already guessed this letter.  Try again\n")
        return "continue"

    if len(guess_letter) != 1:
        print("Please enter a single letter.")
        return "continue"
    
    if not guess_letter.isalpha():
        print("Please enter a letter")

def word_check(guess_letter):
    '''Checking to see if letter is in the word'''
    if guess_letter in game_word.values():
        for index, letter in game_word.items():
            if letter == guess_letter:
                guess_word[index] = guess_letter
        print(f"\nLetter {guess_letter} is in the word")       
        print(" ".join(guess_word.values()))
    else:
        global wrong_guesses 
        wrong_guesses += 1
        print(f"\nLetter {guess_letter} is not in the word")
        print("".join(guess_word.values()))

def end_game(wrong_guesses):
    '''How to determine if the game is finished'''
    if "_" not in guess_word.values():
        print(f"You win!")
        print(f"The word was {''.join(game_word.values())}\n")
        return True
    
    if wrong_guesses >= 6:
        print(f"You lose!")  
        print(f"The word was {''.join(game_word.values())}\n")
        return True
    
    return False

def reset_game():
    '''Resets all game data for a fresh start.'''
    global wrong_guesses, guessed_letters, game_word, guess_word
    game_word.clear()
    guess_word.clear()
    guessed_letters = []
    wrong_guesses = 0

def play_again():
    '''Do you want to play a game?'''
    while True:
        allowed = ("yes", "no", "y", "n")
        yn = input("Would you like to play again?").lower()
        if yn in allowed:
            if yn == "yes" or yn == "y":
                return True
            if yn == "no" or yn =="n":
                return False
        else:
            print("Please answer yes or no.")

def main():
    '''Main program to keep the game going as long as the user would like'''
    while True:
        reset_game()
        build_game_word_instance()

        while True:
            if end_game(wrong_guesses):
                break
                
            guess_letter = input("Enter a letter: ").upper()
            
            if letter_validation(guess_letter) == "continue":
                continue

            guessed_letters.append(guess_letter)

            word_check(guess_letter)
            output_letters = ", ".join(guessed_letters)
            print(f"You have guessed letters: {output_letters}")
            print(f"You have {6 - wrong_guesses} wrong gesses reamaining.\n")

        if not play_again():
            print("Goodbye")
            break

# Global variables
game_word = {}
guess_word  = {}
guessed_letters = []
wrong_guesses = 0

# Start of the program
if __name__ == "__main__":
    main()
