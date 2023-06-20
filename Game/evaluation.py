from game_tools import *


def valid_word(word, language, word_length):
    wordlist = get_vocabulary()
    if word in wordlist[language][word_length]:
        return True
    return False


def guess_word(language, word_length):
    while True:
        guess = input("Guess a word: ").upper()
        guess = guess.replace(" ", "")
        if valid_word(guess, language, word_length):
            return guess
        print("Not a valid word")


def evaluate_word(word, secret_word):
    feedback = [[word[i], ""] for i in range(len(word))]
    used_positions = []

    for count, char in enumerate(word):
        if word[count] == secret_word[count]:
            feedback[count][1] = "red"
            used_positions.append(count)

    secret_word_copy = []
    for char in secret_word:
        secret_word_copy.append(char)

    for position in used_positions:
        secret_word_copy.remove(word[position])

    for count, char in enumerate(word):
        if count not in used_positions:
            if word[count] in secret_word_copy:
                feedback[count][1] = "yellow"
                secret_word_copy.remove(word[count])

    return feedback


def evaluate_word_pattern(word, secret_word):
    feedback = [0 for i in range(len(word))]
    used_positions = []

    for count, char in enumerate(word):
        if word[count] == secret_word[count]:
            feedback[count] = 2
            used_positions.append(count)

    secret_word_copy = []
    for char in secret_word:
        secret_word_copy.append(char)

    for position in used_positions:
        secret_word_copy.remove(word[position])

    for count, char in enumerate(word):
        if count not in used_positions:
            if word[count] in secret_word_copy:
                feedback[count] = 1
                secret_word_copy.remove(word[count])

    return tuple(feedback)



def winning_answer(word_score):
    for char in word_score:
        if char[1] != "red":
            return False

    return True


def yellow_letters(word_score):
    yellows = []
    for char in word_score:
        if char[1] == "yellow":
            yellows.append(char[0])
    return yellows


def filter_words_on_yellow(word_list, word_score):
    filtered_wordlist = []
    for word in word_list:
        yellows = yellow_letters(word_score)
        for char in word:
            if char in yellows:
                yellows.remove(char)
        if not yellows:
            filtered_wordlist.append(word)

    return filtered_wordlist


def calc_bad_letters(word_score, prev_bad_letters):
    if not prev_bad_letters:
        prev_bad_letters = [[] for _ in range(len(word_score))]
    new_bad_letters = prev_bad_letters

    for index, char in enumerate(word_score):
        if char[1] == "":
            for bad_letters in new_bad_letters:
                if char[0] not in bad_letters and char[0] not in yellow_letters(word_score):
                    bad_letters.append(char[0])
        if char[1] == "yellow":
            if char[0] not in new_bad_letters[index]:
                new_bad_letters[index].append(char[0])

    for char, bad_letters in zip(word_score, new_bad_letters):
        if char[1] == "red":
            bad_letters.clear()

    return new_bad_letters


def reduce(possible_answers, bad_letters, score):
    new_possible_answers = []
    possible_answers = filter_words_on_yellow(possible_answers, score)

    for word in possible_answers:
        valid = True
        for char1, char2, bl in zip(word, score, bad_letters):
            if char2[1] == "red" and char1 != char2[0]:
                valid = False
                break
            if char1 in bl:
                valid = False
                break
        if valid:
            new_possible_answers.append(word)

    return new_possible_answers

# print(evaluate_word("palen", "nalpo"))
# print(evaluate_word_pattern("palen", "nalpo"))