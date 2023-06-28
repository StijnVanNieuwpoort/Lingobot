import unittest
from Game.evaluation import *


class TestEvaluationFunctions(unittest.TestCase):

    def test_valid_word(self):
        language = "Nederlands"
        word_length = "5"

        # Test word_length too long.
        self.assertEqual(valid_word("VERYLONGWORD", language, word_length), False)
        # Test word_length too short.
        self.assertEqual(valid_word("WORD", language, word_length), False)

        # Test word that doesn't exist.
        self.assertEqual(valid_word("ABCDE", language, word_length), False)
        # Test word that does exist.
        self.assertEqual(valid_word("WOORD", language, word_length), True)

    def test_evaluate_word(self):
        # Test evaluate_word gives correct score with varied score.
        word = "WORD"
        secret_word = "DIRT"
        expected_score = [["W", ""], ["O", ""], ["R", "red"], ["D", "yellow"]]

        # Should equal expected_score
        self.assertEqual(evaluate_word(word, secret_word), expected_score)

        # Test evaluate_word gives correct score with confusing yellows.
        word = "BEER"
        secret_word = "MORE"
        expected_score = [["B", ""], ["E", "yellow"], ["E", ""], ["R", "yellow"]]

        # The second E in "BEER" should not get a yellow score, because there is only 1 E in "MORE".
        self.assertEqual(evaluate_word(word, secret_word), expected_score)

        # Test if evaluate_word correctly ignores characters with a red score in checking for yellows.
        word = "WERE"
        secret_word = "BEAT"
        expected_score = [["W", ""], ["E", "red"], ["R", ""], ["E", ""]]

        # The second E in "WERE" should not get a yellow score, because the first E already got a red score,
        # and there is only 1 E in "BEAT"
        self.assertEqual(evaluate_word(word, secret_word), expected_score)

    def test_winning_answer(self):
        # Test winning_answer when word is the correct answer.
        word = "WORD"
        secret_word = "WORD"
        score = evaluate_word(word, secret_word)

        self.assertEqual(winning_answer(score), True)

        # Test winning_answer when word is not the correct answer.
        word = "WORD"
        secret_word = "BIRD"
        score = evaluate_word(word, secret_word)

        self.assertEqual(winning_answer(score), False)

    def test_yellow_letters(self):
        word = "BEER"
        secret_word = "MORE"
        score = evaluate_word(word, secret_word)
        expected_outcome = ["E", "R"]

        self.assertEqual(yellow_letters(score), expected_outcome)

    def test_filter_words_on_yellow(self):
        word = "BEER"
        secret_word = "MORE"
        score = evaluate_word(word, secret_word)
        wordlist = ["RATE", "ROLL", "MEAL", "MOON", "FOOL"]
        expected_outcome = ["RATE"]

        # "RATE" should be the only word that the function returns because it is the only words that contain both,
        #  The yellow E and the yellow R.
        self.assertEqual(filter_words_on_yellow(wordlist, score), expected_outcome)

    def test_calculate_bad_letters(self):
        # Test bad letters when prev_bad_letters is empty and gray letters.
        word = "WORD"
        secret_word = "MAKE"
        score = evaluate_word(word, secret_word)
        expected_outcome = [["W", "O", "R", "D"], ["W", "O", "R", "D"], ["W", "O", "R", "D"], ["W", "O", "R", "D"]]

        # Giving an empty list as argument. All letters in "WORD" are bad letters.
        self.assertEqual(calc_bad_letters(score, []), expected_outcome)

        word = "CORD"
        secret_word = "MAKE"
        score = evaluate_word(word, secret_word)
        prev_bad_letters = expected_outcome
        expected_outcome = [["W", "O", "R", "D", "C"], ["W", "O", "R", "D", "C"], ["W", "O", "R", "D", "C"], ["W", "O", "R", "D", "C"]]

        # Giving a filled list as argument. Bad letters in "WORD" already in prev_bad_letters. Only C from "CORD" added.
        self.assertEqual(calc_bad_letters(score, prev_bad_letters), expected_outcome)

        # Test red letter removes bad_letters from position.
        word = "MORD"
        secret_word = "MAKE"
        score = evaluate_word(word, secret_word)
        prev_bad_letters = expected_outcome
        expected_outcome = [[], ["W", "O", "R", "D", "C"], ["W", "O", "R", "D", "C"], ["W", "O", "R", "D", "C"]]

        # Because the M in "MORD" is correct, the list on the first index of the return value is empty.
        self.assertEqual(calc_bad_letters(score, prev_bad_letters), expected_outcome)

        # Test yellow letters correctly updates bad_letters.
        word = "WORD"
        secret_word = "DATE"
        score = evaluate_word(word, secret_word)
        expected_outcome = [["W", "O", "R"], ["W", "O", "R"], ["W", "O", "R"], ["W", "O", "R", "D"]]

        # D is only a bad letter in the last position, because a yellow letter indicates that the character in question.
        # Is present on another position in the word.
        self.assertEqual(calc_bad_letters(score, []), expected_outcome)
