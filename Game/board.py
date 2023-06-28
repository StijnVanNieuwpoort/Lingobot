# Prints first letter of the word on turn 1.
def show_turn_zero(secret_word):
    print('\033[31m' + secret_word[0])


def show_board(words_played, secret_word, first_letter):
    """
    Prints the board in the console.
    :param words_played: (List): Words that have been played in earlier turn(s).
    :param secret_word: Word that has to be guessed.
    :param first_letter: (Bool): Play with first letter known.
    """
    if not words_played:
        if first_letter:
            show_turn_zero(secret_word)

    for char in words_played[-1]:
        if char[1] == "red":
            print('\033[31m' + char[0], end=" ")
        elif char[1] == "yellow":
            print('\033[33m' + char[0], end=" ")
        else:
            print(char[0], end=" ")
    print("")
