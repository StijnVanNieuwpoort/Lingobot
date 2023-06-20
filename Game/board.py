def show_turn_zero(secret_word):
    print('\033[31m' + secret_word[0])


def show_board(words_played, secret_word, first_letter):
    if not words_played:
        if first_letter:
            show_turn_zero(secret_word)

    for word in words_played:
        for char in word:
            if char[1] == "red":
                print('\033[31m' + char[0], end=" ")
            elif char[1] == "yellow":
                print('\033[33m' + char[0], end=" ")
            else:
                print(char[0], end=" ")
        print("")