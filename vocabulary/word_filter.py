import json
import re

wordlist = {
    "Nederlands": {
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
        10: []
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
        10: []
    }
}


def is_valid_word(word):
    pattern = re.compile(r'^[a-zA-Z]+$')  # Regex pattern to match only alphabetic characters
    return bool(pattern.match(word))

with open("Nederlandse Woorden/basiswoorden-gekeurd.txt", "r") as file:
    for word in file:
        wordlength = len(word.rstrip("\n"))
        if is_valid_word(word) and wordlength in wordlist["Nederlands"]:
            wordlist["Nederlands"][wordlength].append(word.rstrip("\n").upper())


with open("wordlist.json", "w") as jsonfile:
    json.dump(wordlist, jsonfile)