# Your Name
# CIS256 Term Year (e.g. Spring 2026)
# Exercise Assignment 4
# Testing the Game

import unittest
import guess_the_word

class TestTheGame(unittest.TestCase):

    def setUp(self):
        guess_the_word.reset_game()
    
    def test_word_selection_from_list(self):
        '''Test that the word comes from a list of values'''
        
        expected_words = [
            "BENEFICIAL", "EXCELLENT", "BLACKBERRY", "FACETIOUS",
            "AREIOUS", "TRAGEDIOUSLY", "VIGOROUSLY", "NOCTURNAL",
            "TREBUCHET", "POWERFUL", "QUESTIONABLE", "PIZZARIA",
            "MONUMENTAL", "GALANTRY", "CAPRICIOUS", "VACILLATION"]
        
        guess_the_word.build_game_word_instance()
        selected_word = "".join(guess_the_word.game_word.values())
        
        self.assertIn(selected_word, expected_words)

    def test_guess(self):

        # Manually set the word to ensure we know the correct letters
        guess_the_word.game_word = {0: 'W', 1: 'O', 2: 'R', 3: 'D'}
        guess_the_word.guess_word = {0: '_', 1: '_', 2: '_', 3: '_'}
        
        guess_the_word.word_check('W')
        
        # Check that the letter was added correctly to the correct guesses dicitonary
        self.assertEqual(guess_the_word.guess_word[0], 'W')
        
        # Check that wrong_guesses did not increment
        self.assertEqual(guess_the_word.wrong_guesses, 0)



if __name__ == "__main__":
    unittest.main()