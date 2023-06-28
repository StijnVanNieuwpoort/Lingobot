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
    # show_board(words_played, word_to_guess, first_letter)

    for turn in range(turns):
        if turn == 0:
            guess = first_turn_best_word(language, word_length)
        else:
            guess = deploy_strategy(strategy, possible_answers, bad_letters, score, language, word_length)
        score = evaluate_word(guess, word_to_guess)
        bad_letters = calc_bad_letters(score, bad_letters)
        possible_answers = reduce(possible_answers, bad_letters, score)
        words_played.append(score)
        print(f"{turn + 1}:", end=" ")
        show_board(words_played, word_to_guess, first_letter)
        if winning_answer(score):
            print("You win")
            return True

    print(word_to_guess)
    print("You lose")

    return False

game("English", "5", 6, False, "simple")
