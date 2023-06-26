from evaluation import *
from scipy.stats import entropy
from collections import defaultdict
import math

possible_answers = get_vocabulary()["Nederlands"]["5"]


def generate_possible_outcomes(wordlist):
    outcomes = {}
    for word in wordlist:
        outcomes[word] = {c: [] for c in calc_possible_feedback(len(word))}

    for word1 in wordlist:
        for word2 in wordlist:
            outcome = evaluate_word_pattern(word1, word2)
            outcomes[word1][outcome].append(word2)

    return outcomes


def calculate_entropies(words, possible_words, all_outcomes, all_patterns):
    entropies = {}
    for word in words:
        counts = []
        for pattern in all_patterns:
            matches = set(all_outcomes[word][str(pattern)])
            matches = matches.intersection(possible_words)
            counts.append(len(matches))

        # Calculate entropy manually
        total_count = sum(counts)
        probabilities = [count / total_count for count in counts if count > 0]
        entropies[word] = -sum(p * math.log2(p) for p in probabilities) if probabilities else 0.0

    return entropies


# outcomes = generate_possible_outcomes(possible_answers)
# print(outcomes)
# outcomes =
# print(calculate_entropies(possible_answers, possible_answers, outcomes, calc_possible_feedback(5)))
# print(generate_possible_outcomes(possible_answers))

# def calculate_entropies(words, possible_words, outcomes_dict, all_patterns):
#     entropies = {}
#     for word in words:
#         counts = []
#         for pattern in all_patterns:
#             matches = set(outcomes_dict[word][pattern])
#             matches = matches.intersection(possible_words)
#             counts.append(len(matches))
#         entropies[word] = entropy(counts)
#     return entropies

# outcomes = get_word_outcomes()["Nederlands"]["5"]
# print(calculate_entropies(possible_answers, possible_answers, outcomes, calc_possible_feedback(5)))