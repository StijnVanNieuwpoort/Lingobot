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
    all_feedback = calc_possible_feedback(int(word_length))
    all_words = get_vocabulary()[language][word_length]
    outcomes = generate_possible_outcomes(possible_answers)
    entropies = calculate_entropies(possible_answers, possible_answers, outcomes, all_feedback)
    return calc_highest_info_word(entropies)