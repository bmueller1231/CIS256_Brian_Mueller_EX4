# Brian Mueller
# CIS256 Spring 2026
# Part 2 - Writing the Game (Hangman)

import random

def build_game_word_instance(word):
    word_index = 0
    for i in word:
        if word_index != len(word):
            game_word[word_index] = i.upper()
            word_index += 1


word = input("Enter a word: ")

game_word = {}
guess_word  = {}
guessed_letters = []


build_game_word_instance(word)

print(game_word)


