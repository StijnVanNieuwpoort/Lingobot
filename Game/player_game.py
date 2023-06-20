import colorama
from board import *
from evaluation import *
from game_tools import *
colorama.init(autoreset=True)


def game(language, word_length, first_letter):
    word_to_guess = random_word(language, word_length)
    words_played = []
    show_board(words_played, word_to_guess, first_letter)

    for turn in range(0, 5):
        guess = guess_word(language, word_length)
        score = evaluate_word(guess, word_to_guess)
        words_played.append(score)
        show_board(words_played, word_to_guess, first_letter)
        if winning_answer(score):
            print("You win")
            return True

    print(word_to_guess)
    print("You lose")

    return False


game("Nederlands", "5", True)
