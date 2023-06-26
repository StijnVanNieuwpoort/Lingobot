import json
from entropy import *

bits_dict = {
    "Nederlands": {
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
        10: [],
        11: [],
        12: []
    },
    "English": {
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
        10: [],
        11: [],
        12: []
    }
}


wordlist_nederlands = get_vocabulary()["Nederlands"]
wordlist_english = get_vocabulary()["English"]


def fill_bits_dict_nederlands():
    for i in range(2, 7):
        outcomes = get_word_outcomes()["Nederlands"][str(i)]
        wordlist = wordlist_nederlands[str(i)]
        all_feedbacks = calc_possible_feedback(i)
        entropies = calculate_entropies(wordlist, wordlist, outcomes, all_feedbacks)
        bits_dict["Nederlands"][i] = entropies


def fill_bits_dict_english():
    for i in range(5, 6):
        outcomes = get_word_outcomes()["English"][str(i)]
        wordlist = wordlist_english[str(i)]
        all_feedbacks = calc_possible_feedback(i)
        entropies = calculate_entropies(wordlist, wordlist, outcomes, all_feedbacks)
        bits_dict["English"][i] = entropies


def export_bits_to_json(file, all_bits):
    with open(file, "w") as jsonfile:
        json.dump(all_bits, jsonfile)


fill_bits_dict_nederlands()
fill_bits_dict_english()
export_bits_to_json("word-entropies.json", bits_dict)