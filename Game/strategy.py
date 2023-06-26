from entropy import *


def deploy_strategy(strategy, possible_answers, bad_letters, score, language, word_length):
    if strategy == "simple":
        return simple(possible_answers)
    if strategy == "information":
        return information(possible_answers, language, word_length)
    return 0


def simple(possible_answers):
    return possible_answers[0]


def information(possible_answers, language, word_length):
    if len(possible_answers) < 3:
        return possible_answers[0]

    # Checks if outcomes has already been cached so it doesn't have to load it again.
    if not hasattr(information, 'outcomes'):
        information.outcomes = get_word_outcomes()[language][word_length]

    all_feedback = calc_possible_feedback(int(word_length))
    all_words = get_vocabulary()[language][word_length]
    entropies = calculate_entropies(all_words, possible_answers, information.outcomes, all_feedback)

    return calc_highest_info_word(entropies)