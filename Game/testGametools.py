import unittest
from Game.game_tools import *


class TestGametoolsFunctions(unittest.TestCase):
    def test_possible_feedback(self):
        # All possible forms of feedback for a 4-letter word. Impossible answers like (2, 2, 2, 1) excluded.
        expected_possible_feedback = [(0, 0, 0, 0), (0, 0, 0, 1), (0, 0, 0, 2), (0, 0, 1, 0), (0, 0, 1, 1), (0, 0, 1, 2),
                             (0, 0, 2, 0), (0, 0, 2, 1), (0, 0, 2, 2), (0, 1, 0, 0), (0, 1, 0, 1), (0, 1, 0, 2),
                             (0, 1, 1, 0), (0, 1, 1, 1), (0, 1, 1, 2), (0, 1, 2, 0), (0, 1, 2, 1), (0, 1, 2, 2),
                             (0, 2, 0, 0), (0, 2, 0, 1), (0, 2, 0, 2), (0, 2, 1, 0), (0, 2, 1, 1), (0, 2, 1, 2),
                             (0, 2, 2, 0), (0, 2, 2, 1), (0, 2, 2, 2), (1, 0, 0, 0), (1, 0, 0, 1), (1, 0, 0, 2),
                             (1, 0, 1, 0), (1, 0, 1, 1), (1, 0, 1, 2), (1, 0, 2, 0), (1, 0, 2, 1), (1, 0, 2, 2),
                             (1, 1, 0, 0), (1, 1, 0, 1), (1, 1, 0, 2), (1, 1, 1, 0), (1, 1, 1, 1), (1, 1, 1, 2),
                             (1, 1, 2, 0), (1, 1, 2, 1), (1, 1, 2, 2), (1, 2, 0, 0), (1, 2, 0, 1), (1, 2, 0, 2),
                             (1, 2, 1, 0), (1, 2, 1, 1), (1, 2, 1, 2), (1, 2, 2, 0), (1, 2, 2, 1), (2, 0, 0, 0),
                             (2, 0, 0, 1), (2, 0, 0, 2), (2, 0, 1, 0), (2, 0, 1, 1), (2, 0, 1, 2), (2, 0, 2, 0),
                             (2, 0, 2, 1), (2, 0, 2, 2), (2, 1, 0, 0), (2, 1, 0, 1), (2, 1, 0, 2), (2, 1, 1, 0),
                             (2, 1, 1, 1), (2, 1, 1, 2), (2, 1, 2, 0), (2, 1, 2, 1), (2, 2, 0, 0), (2, 2, 0, 1),
                             (2, 2, 0, 2), (2, 2, 1, 0), (2, 2, 1, 1), (2, 2, 2, 0), (2, 2, 2, 2)]

        # For word_length is 4.
        self.assertEqual(calc_possible_feedback(4), expected_possible_feedback)

    def test_calc_highest_info_word(self):
        language = "Nederlands"
        word_length = "5"
        word_entropies = get_word_bit_scores()[language][word_length]

        self.assertEqual(calc_highest_info_word(word_entropies), "SATER")

        language = "English"
        word_length = "5"
        word_entropies = get_word_bit_scores()[language][word_length]

        self.assertEqual(calc_highest_info_word(word_entropies), "RAISE")
