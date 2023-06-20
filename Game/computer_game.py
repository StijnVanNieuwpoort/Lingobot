from strategy import *
from board import *
import colorama
colorama.init(autoreset=True)


def game(language, word_length, turns, first_letter, strategy):
    word_to_guess = random_word(language, word_length)
    print(word_to_guess)
    words_played = []
    possible_answers = get_vocabulary()[language][word_length]
    bad_letters = []
    score = []
    show_board(words_played, word_to_guess, first_letter)

    for turn in range(turns):
        print(turn + 1)
        if turn == 0:
            guess = first_turn_best_word(language, word_length)
        else:
            guess = deploy_strategy(strategy, possible_answers, bad_letters, score, language, word_length)
        score = evaluate_word(guess, word_to_guess)
        bad_letters = calc_bad_letters(score, bad_letters)
        possible_answers = reduce(possible_answers, bad_letters, score)
        words_played.append(score)
        show_board(words_played, word_to_guess, first_letter)
        if winning_answer(score):
            print("You win")
            return True

    print(word_to_guess)
    print("You lose")

    return False

game("Nederlands", "6", 6, False, "information")


# SATER, FAXEN

# S A T E R
# K E L E N
# D O Z E N
# M I X E N
# H Y F E N
# HUWEN

# S A T E R
# K E R E N
# B U R E N
# D U R E N
# H U R E N
# ZUREN

# S A T E R
# T O R U S
# B O R S T
# D O R S T
# H O R S T
# K O R S T
# VORST