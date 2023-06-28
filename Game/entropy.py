from evaluation import *
from scipy.stats import entropy
from collections import defaultdict
import math


def generate_possible_outcomes(wordlist):
    """
    For every word in wordlist. Keeps track of all words in wordlist that match the possible score if they were to be compared.
    :param wordlist: (List): List of words.
    :return: Dict: For every word, for every score, a list of corresponding words.
    """
    # Creates a dictionary with roughly this structure: {"WORD": {(0, 0, 2, 2): ["BIRD", "CARD"], (0, 2, 2, 2): ["FORD", "LORD"]....
    outcomes = {}
    for word in wordlist:
        outcomes[word] = {c: [] for c in calc_possible_feedback(len(word))}

    for word1 in wordlist:
        for word2 in wordlist:
            outcome = evaluate_word_pattern(word1, word2)
            outcomes[word1][outcome].append(word2)

    return outcomes


def calculate_entropies(words, possible_words, all_outcomes, all_feedback):
    """
    Calculates the entropy value of every word by counting it's occurrence in all_outcomes.
    :param words: (List): All words.
    :param possible_words: (List): All possible words/answers
    :param all_outcomes: Output of generate_possible_outcomes().
    :param all_feedback: All possible feedback.
    :return: List: All words with their current entropy score represented in bits.
    """
    entropies = {}
    for word in words:
        counts = []
        for pattern in all_feedback:
            matches = set(all_outcomes[word][str(pattern)])
            matches = matches.intersection(possible_words)
            counts.append(len(matches))

        # Calculate entropy manually
        total_count = sum(counts)
        probabilities = [count / total_count for count in counts if count > 0]
        entropies[word] = -sum(p * math.log2(p) for p in probabilities) if probabilities else 0.0

    return entropies
