import random
import json
import os
import re


def get_vocabulary():
    # Get the current directory
    current_directory = os.getcwd()

    # Construct the path to the wordlist.json file
    json_path = os.path.join(current_directory, '..', 'vocabulary', 'wordlist.json')

    # Read the JSON data from the file
    with open(json_path, 'r') as file:
        data = json.load(file)

    return data


def random_word(language, word_length):
    wordlist = get_vocabulary()
    random_word = random.choice(wordlist[language][word_length])

    return random_word


def print_board(words_played, current_turn):
    return 0


def guess_word():
    guess = input("Guess a word: ")
    guess = guess.replace(" ", "")

    return guess


def evaluate_word(word, secret_word: str):
    feedback = {}
    for char in range(len(word)):
        feedback[char] = {word[char]: ""}

    used_letters = []

    for char in range(len(word)):
        if word[char] == secret_word[char]:
            feedback[char][word[char]] = "red"
            used_letters.append(word[char])

    secret_word_copy = secret_word

    for char in used_letters:
        secret_word_copy = secret_word_copy.replace(char, "")

    for char in range(len(word)):
        if word[char] not in used_letters:
            if word[char] in secret_word_copy:
                feedback[char][word[char]] = "yellow"
                secret_word_copy = secret_word_copy.replace(word[char], "")

    return feedback


def winning_answer(word_score: dict):
    return True


def game(language, word_length):
    word_to_guess = random_word(language, word_length)
    words_played = []

    for turn in range(0, 5):
        guess = guess_word()
        score = evaluate_word(guess, word_to_guess)
        words_played.append(score)
        # showBoard()

    return 0


woord = evaluate_word("ballon", "vriend")
for x in woord:
    print(woord[x].values())

# game("Nederlands", "5")
