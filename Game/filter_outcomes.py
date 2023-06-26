import json
from entropy import *

outcomes_dict = {
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


# Saves the outcomes for all the words in dictonary. Converts tuples to strings because tuples cannot be saved in a
# json file
def fill_outcomes_dict_nederlands():
    for i in range(4, 6):
        wordlist = wordlist_nederlands[str(i)]
        outcomes = generate_possible_outcomes(wordlist)
        converted_outcomes = {word: {str(key): value for key, value in inner_dict.items()} for word, inner_dict in outcomes.items()}
        outcomes_dict["Nederlands"][i] = converted_outcomes


def fill_outcomes_dict_english():
    for i in range(5, 6):
        wordlist = wordlist_english[str(i)]
        outcomes = generate_possible_outcomes(wordlist)
        converted_outcomes = {word: {str(key): value for key, value in inner_dict.items()} for word, inner_dict in outcomes.items()}
        outcomes_dict["English"][i] = converted_outcomes


# Exports outcomes_dict to 'word-entropies.json'
def export_outcomes_to_json(file, all_outcomes):
    with open(file, "w") as jsonfile:
        json.dump(all_outcomes, jsonfile)


# fill_outcomes_dict_nederlands()
# fill_outcomes_dict_english()
export_outcomes_to_json('word-outcomes.json', outcomes_dict)
