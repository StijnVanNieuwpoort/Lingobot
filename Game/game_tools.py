import json
import os
import random
import itertools
import jsonlines
from ast import literal_eval


def get_vocabulary():
    # Get the current directory
    current_directory = os.getcwd()

    # Construct the path to the wordlist.json file
    json_path = os.path.join(current_directory, '..', 'vocabulary', 'wordlist.json')

    # Read the JSON data from the file
    with open(json_path, 'r') as file:
        data = json.load(file)

    return data


def get_word_outcomes():
    # Get the current directory
    current_directory = os.getcwd()

    # Construct the path to the wordlist.json file
    json_path = os.path.join(current_directory, '..', 'Game', 'word-outcomes.json')

    # Read the JSON data from the file
    with open(json_path, 'r') as file:
        data = json.load(file)

    return data


def get_word_bit_scores():
    # Get the current directory
    current_directory = os.getcwd()

    # Construct the path to the wordlist.json file
    json_path = os.path.join(current_directory, '..', 'Game', 'word-entropies.json')

    # Read the JSON data from the file
    with open(json_path, 'r') as file:
        data = json.load(file)

    return data


def random_word(language, word_length):
    wordlist = get_vocabulary()
    secret_word = random.choice(wordlist[language][word_length])

    return secret_word


def calc_possible_feedback(word_length):
    # Creates every possible feedback combination
    combinations = list(itertools.product([0, 1, 2], repeat=word_length))

    # Removes feedback combinations that are impossible like (1, 2, 2, 2).
    # If everything except one letter is in the right spot. That one letter cannot be somewhere else in the word.
    for combination in combinations:
        red_letters = 0
        yellow_letters = 0
        for feedback in combination:
            if feedback == 2:
                red_letters += 1
            if feedback == 1:
                yellow_letters += 1
        if red_letters == word_length - 1 and yellow_letters == 1:
            combinations.remove(combination)

    return combinations


def calc_highest_info_word(word_bit_scores):
    highest_bit = max(word_bit_scores.values())
    return list(word_bit_scores.keys())[list(word_bit_scores.values()).index(highest_bit)]


def first_turn_best_word(language, word_length):
    best_words = []
    if language == "Nederlands":
        best_words = ["AI", "AIO", "ROES", "SATER", "SINTER"]
    if language == "English":
        best_words = ["RAISE"]

    for word in best_words:
        if len(word) == int(word_length):
            return word

    return 0


# print(calc_highest_info_word(get_word_bit_scores()["Nederlands"]["5"]))
# print(first_turn_best_word("Nederlands", "5"))
# print(calc_highest_info_word(get_word_bit_scores()["English"]["5"]))
# print(first_turn_best_word("English", "5"))