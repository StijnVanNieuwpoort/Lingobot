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


def fill_bits_dict_nederlands():
    for i in range(2, 7):
        wordlist = wordlist_nederlands[str(i)]
        all_feedback = calc_possible_feedback(i)
        patterns = generate_possible_outcomes(wordlist)
        entropies = calculate_entropies(wordlist, wordlist, patterns, all_feedback)
        bits_dict["Nederlands"][i] = entropies


def export_bits_to_json(file, all_bits):
    with open(file, "w") as jsonfile:
        json.dump(bits_dict, jsonfile)


fill_bits_dict_nederlands()
export_bits_to_json("word-outcomes.json", bits_dict)