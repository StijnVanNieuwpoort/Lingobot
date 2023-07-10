import unittest
from Game.entropy import *


class TestEntropyFunctions(unittest.TestCase):

    def test_entropy_validation(self):
        """
        With the entropy calculation in entropy.py, the entropy value for every word is calculated, based on the list
        of possible answers at that point. Because this list is always the same on turn 1 because no word
        has been played at that point in the game. It can be assumed that the best first word to play,
        is the word with the highest entropy value (bit score) when the list of possible answers has not been
        reduced yet.

        In the scientific article: Kooi, B. (2005). Yet another mastermind strategy. ICGA Journal, 28(1), 13-20.
        Under section 2.5: "The Entropy Strategy". When translating the given formula to Python code in the context of
        Lingo/Wordle (entropy.py, line 46). The entropy value (bit score) can be calculated for every word.

        When using the same word-database as the official Wordle game which contains 2309 english 5-letter words.
        This implementation of the strategy determines "raise" with a rounded score of 5.88,
        to be the highest information word on the first turn.

        Esteemed mathematician and youtuber that goes under the alias: "3Blue 1Brown". Has already tested this before.
        Link to youtube video: https://www.youtube.com/watch?v=fRed0Xmc2Wg&t=505s
        Where this implementation of the algorithm only assumes the 2309 provided words can be correct.
        3Blue 1Brown's implementation assumes all 5-letter words in the english dictionary could be correct.
        His top 3 best words are: "soare" with a score of 5.89, "roate" with a score of 5.88 and finally "raise" with a rounded score of 5.88.
        We can see that "raise" is the third best word to play according to 3Blue 1Brown's implementation.
        However, because he uses all words, instead of only valid-words. "soare" and "roate" are note included,
        in the 2309 Worlde approved words. Which means that when using the a naive implementation where the algorithm
        only has knowledge on these 2309 words. "raise" is the best first turn word when looking one step ahead.
        """

        language = "English"
        word_length = "5"

        # When no words have been played yet (so list of possible answers is not reduced yet), "raise" is the word
        # that gives the highest bit-score.
        word_bit_scores = get_word_bit_scores()[language][word_length]
        highest_info_word = calc_highest_info_word(word_bit_scores)
        self.assertEqual(highest_info_word, "RAISE")

        # Just like in 3Blue 1Brown's example. "raise" gives a rounded bit-score of 5.88.
        highest_bit_score = calc_rounded_bit_score_of_word("RAISE", word_bit_scores, 2)
        self.assertEqual(highest_bit_score, 5.88)


