from game_tools import *


def valid_word(word, language, word_length):
    """
    This function returns True when the word exists in the wordlist.
    :param word: (String): Word to evaluate.
    :param language: (String): Language of wordlist to check.
    :param word_length: (String): Length of wordlist to check.
    :return: Bool: If word in wordlist.
    """
    wordlist = get_vocabulary()
    if word in wordlist[language][word_length]:
        return True
    return False


def guess_word(language, word_length):
    """
    Asks for user input about the word that is desired to be guessed.
    :param language: (String): Language of wordlist to check.
    :param word_length: (String): Length of wordlist to check.
    :return: String: Guess that user typed in when valid_word()
    """
    while True:
        guess = input("Guess a word: ").upper()
        guess = guess.replace(" ", "")
        if valid_word(guess, language, word_length):
            return guess
        print("Not a valid word")


def evaluate_word(word, secret_word):
    """
    Checks correctness for every character in a word compared to secret_word.
    :param word: Word to be evaluated.
    :param secret_word: Actual word evaluation is based on.
    :return: List: Score for word represented in Strings red, yellow or empty for every character.
    """
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
    """
    Checks correctness for every character in a word compared to secret_word.
    :param word: Word to be evaluated.
    :param secret_word: Actual word evaluation is based on.
    :return: List: Score for word represented in integers 2, 1 or 0 for every character.
    """
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
    """
    Checks if every character in word_score is "red".
    :param word_score: Score for a word returned by evaluate_word()
    :return: Bool: If answer is correct.
    """
    for char in word_score:
        if char[1] != "red":
            return False

    return True


def yellow_letters(word_score):
    """
    Calculates all the yellow letters in word_score.
    :param word_score: Score for a word returned by evaluate_word()
    :return: List: Filled with the yellow characters in word_score
    """
    yellows = []
    for char in word_score:
        if char[1] == "yellow":
            yellows.append(char[0])
    return yellows


def filter_words_on_yellow(word_list, word_score):
    """
    From wordlist, removes every word that does not contain established yellow letters.
    :param word_list: (List): List of words.
    :param word_score: Score for a word returned by evaluate_word()
    :return: List: Updated version of word_list.
    """
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
    """
    Calculates impossible letters for every position of the word.
    :param word_score: Score for a word returned by evaluate_word()
    :param prev_bad_letters: (List): Output of calc_bad_letters() of previous round.
    :return: List: With lists on every index of word filled with impossible characters for the position.
    """
    # If prev_bad_letters doesn't exist yet because of first round. Creates it.
    if not prev_bad_letters:
        prev_bad_letters = [[] for _ in range(len(word_score))]
    new_bad_letters = prev_bad_letters

    for index, char in enumerate(word_score):
        # If character score equals empty string. Puts the corresponding character as bad letter in every position.
        if char[1] == "":
            for bad_letters in new_bad_letters:
                # If the bad letter was not already there or if the bad_letter is a yellow in the word, don't add it.
                if char[0] not in bad_letters and char[0] not in yellow_letters(word_score):
                    bad_letters.append(char[0])
        # If character score equals yellow. Puts the corresponding character as bad letter on that position.
        if char[1] == "yellow":
            if char[0] not in new_bad_letters[index]:
                new_bad_letters[index].append(char[0])

    # If character score equals red. Clears that position of all bad letters.
    for char, bad_letters in zip(word_score, new_bad_letters):
        if char[1] == "red":
            bad_letters.clear()

    return new_bad_letters


def reduce(possible_answers, bad_letters, word_score):
    """
    Reduces possible_answers list according to bad_letters and word_score.
    :param possible_answers: (List): Words that could be the correct answer.
    :param bad_letters: (List): Impossible characters for every position in word.
    :param word_score: Score for a word returned by evaluate_word()
    :return: List: Reduced version of possible_answers.
    """
    new_possible_answers = []
    # Filter out words that do not contain the established yellow letters of the guessed word.
    possible_answers = filter_words_on_yellow(possible_answers, word_score)

    for word in possible_answers:
        valid = True
        # Loop trough indexes of word, word_score and bad_letters at the same time.
        for char1, char2, bl in zip(word, word_score, bad_letters):
            # If character for guessed word is red (correct character),
            # but the character of the word that is checked is not the same. Not a valid word (possible answer).
            if char2[1] == "red" and char1 != char2[0]:
                valid = False
                break
            # If character of word that is checked appears in bad_letters for the position.
            # Not a valid word (possible answer).
            if char1 in bl:
                valid = False
                break

        if valid:
            new_possible_answers.append(word)

    return new_possible_answers
