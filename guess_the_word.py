# Brian Mueller
# CIS256 Spring 2026
# Part 2 - Writing the Game (Hangman)

import random

def build_game_word_instance():
    if len(game_word) == 0:
        word_list = ["beneficial",
                    "excellent",
                    "blackberry",
                    "facetious",
                    "areious",
                    "tragediously"]
        
        word = random.choice(word_list)
        word_index = 0
        
        for i in word:
            if word_index != len(word):
                game_word[word_index] = i.upper()
                guess_word[word_index] = "_"
                word_index += 1
    else:
        print("This game already has a word")
    



game_word = {}
guess_word  = {}
guessed_letters = []
wrong_guesses = 0

build_game_word_instance()

while True:
    
    if "_" not in guess_word.values():
        print(f"You win")
        break

    if wrong_guesses >= 6:
        print(f"You lose.  The word was {''.join(game_word.values())}")
        break
        
    guess_letter = input("Enter a letter: ").upper()
    
    if guess_letter in guessed_letters:
        print("You already guessed this letter.  Try again")
        continue

    if len(guess_letter) != 1:
        print("Please enter a single letter.")
        continue
    
    if not guess_letter.isalpha():
        print("Please enter a letter")

    guessed_letters.append(guess_letter)


    if guess_letter in game_word:
        for index, letter in game_word.items():
            if letter == guess_letter:
                guess_word[index] = guess_letter
                
                print("".join(guess_word.values()))
                print("".join(game_word.values()))
    else:
        print("wrong letter")
        wrong_guesses += 1

print(game_word)




