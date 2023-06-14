import json
import re

vocabulary = {
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


def is_valid_word(word):
    pattern = re.compile(r'^[a-zA-Z]+$')  # Regex pattern to match only alphabetic characters
    return bool(pattern.match(word))

def fill_wordlist_nederlands(wordlist):
    # basiswoorden-gekeurd
    with open("Nederlandse Woorden/basiswoorden-gekeurd.txt", "r") as file:
        for word in file:
            wordlength = len(word.rstrip("\n"))
            if is_valid_word(word) and wordlength in wordlist["Nederlands"]:
                wordlist["Nederlands"][wordlength].append(word.rstrip("\n").upper())

    # Officiele-Lingowoorden-Nederlands
    with open("Nederlandse Woorden/Officiele-Lingowoorden-Nederlands.txt", "r") as file:
        for word in file:
            wordlength = len(word.rstrip("\n"))
            if is_valid_word(word) and wordlength in wordlist["Nederlands"]:
                if word.rstrip("\n").upper() not in wordlist["Nederlands"][wordlength]:
                    wordlist["Nederlands"][wordlength].append(word.rstrip("\n").upper())


def export_wordlist_to_json(file, wordlist):
    with open(file, "w") as jsonfile:
        json.dump(wordlist, jsonfile)

fill_wordlist_nederlands(vocabulary)
export_wordlist_to_json("wordlist.json", vocabulary)