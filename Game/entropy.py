from evaluation import *
from scipy.stats import entropy

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


def calculate_entropies(words, possible_words, outcomes_dict, all_patterns):
    entropies = {}
    for word in words:
        counts = []
        for pattern in all_patterns:
            matches = set(outcomes_dict[word][pattern])
            matches = matches.intersection(possible_words)
            counts.append(len(matches))
        entropies[word] = entropy(counts)
    return entropies


# patterns = generate_pattern_dict(possible_answers)
# # print(patterns)
# print(calculate_entropies(possible_answers, possible_answers, patterns, calc_possible_feedback(5)))