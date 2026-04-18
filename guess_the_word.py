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
    if "_" in guess_word.values() and wrong_guesses < 6:
        guess_letter = input("Enter a letter: ").upper()
        if guess_letter in guessed_letters:
            print("You already guessed this letter.  Try again")
        else:
            guessed_letters.append(guess_letter)
    
    if wrong_guesses < 6:
        if guess_letter not in game_word.values():
            print("wrong letter")
            wrong_guesses += 1
    else:
        print("You lose")
        break
    if guess_letter in game_word:
        for key in game_word:
            if key.values() == guess_letter:
                guess_word[key] = key.values()
                for v in guess_word.values():
                    gword = gword + str(v)
                    print(gword)

    






print(game_word)




