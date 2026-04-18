# Your Name
# CIS256 Term Year (e.g. Spring 2026)
# Exercise Assignment 4
# Testing the Game

import unittest
import guess_the_word

class TestTheGame(unittest.TestCase):

    def setUp(self):
        '''Rest for each test'''

        guess_the_word.reset_game()
    
    def test_word_selection_from_list(self):
        """Test that the word comes from a list of values"""
        
        expected_words =    ["BENEFICIAL", "EXCELLENT", "BLACKBERRY", "FACETIOUS",
                            "AREIOUS", "TRAGEDIOUSLY", "VIGOROUSLY", "NOCTURNAL",
                            "TREBUCHET", "POWERFUL", "QUESTIONABLE", "PIZZARIA",
                            "MONUMENTAL", "GALANTRY", "CAPRICIOUS", "VACILLATION"]
        
        # Build the word
        guess_the_word.build_game_word_instance()
        selected_word = "".join(guess_the_word.game_word.values())
        
        # Check the word set up came from the list
        self.assertIn(selected_word, expected_words)

    def test_correct_guess(self):
        '''Test that the letter entered processes as a correct letter'''

        # Manually set the word to ensure we know the correct letters
        guess_the_word.game_word = {0: "W", 1: "O", 2: "R", 3: "D", 4: "E", 5: "D"}
        guess_the_word.guess_word = {0: "_", 1: "_", 2: "_", 3: "_", 4: "_", 5: "_"}
        
        # Run the check fo rthe letter in the word
        guess_the_word.word_check("D")

        # Check that the letter was added correctly to the correct guesses dicitonary
        # including multiple replacments at once
        self.assertEqual(guess_the_word.guess_word[3], "D")
        self.assertEqual(guess_the_word.guess_word[5], "D")
        
        # Check that wrong_guesses did not increment
        self.assertEqual(guess_the_word.wrong_guesses, 0)

    def test_incorrect_guess(self):
        '''Test that the letter entered processes as an incorrect letter'''

        # Manually set the word to ensure we know the correct letters
        guess_the_word.game_word = {0: "W", 1: "O", 2: "R", 3: "D"}
        guess_the_word.guess_word = {0: "_", 1: "_", 2: "_", 3: "_"}
        
        # Get the starting wrong guesses value
        wrong_word_start = guess_the_word.wrong_guesses
        check_letter = "C"

        # Run the check fo rthe letter in the word
        guess_the_word.word_check(check_letter)
        
        # Check that the letter was not added to the dictionary
        self.assertNotIn(check_letter, guess_the_word.guess_word)

        # Check that wrong_guesses did increment
        self.assertEqual(guess_the_word.wrong_guesses, wrong_word_start + 1)

    def test_letter_validation(self):
        '''Test that a number fails validation'''

        validation = guess_the_word.letter_validation("1")
        self.assertNotEqual(validation,"continue")

if __name__ == "__main__":
    unittest.main()