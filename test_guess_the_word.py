# Your Name
# CIS256 Term Year (e.g. Spring 2026)
# Exercise Assignment 4
# Testing the Game

import unittest
import guess_the_word

class TestTheGame(unittest.TestCase):
    def test_word_selection_from_list(self):
        expected_words = [
            "BENEFICIAL", "EXCELLENT", "BLACKBERRY", "FACETIOUS",
            "AREIOUS", "TRAGEDIOUSLY", "VIGOROUSLY", "NOCTURNAL",
            "TREBUCHET", "POWERFUL", "QUESTIONABLE", "PIZZARIA",
            "MONUMENTAL", "GALANTRY", "CAPRICIOUS", "VACILLATION"
        ]
        guess_the_word.build_game_word_instance()
        selected_word = "".join(guess_the_word.game_word.values())
        
        self.assertIn(selected_word, expected_words)




if __name__ == "__main__":
    unittest.main()