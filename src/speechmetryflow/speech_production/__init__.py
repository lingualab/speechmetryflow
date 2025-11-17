from speechmetryflow.speech_production import fluency
from speechmetryflow.speech_production.fragment import Fragment

from collections import Counter


def compute_counts(words):
    '''
    Compute various count statistics for a list of words.

    Parameters
    ----------
    words (list of str): The list of words to analyze.

    Returns
    -------
    n (int): Total number of words in the list.
    n_different (int): Number of distinct words (vocabulary size).
    n_unique (int): Number of words that occur exactly once.
    n_repetition (int): Number of distinct words that occur more than once 

    Examples
    --------
    >>> compute_counts(["cat", "dog", "cat", "mouse"])
    (4, 3, 2, 1)
    '''
    n = len(words)
    counter = Counter(words)
    n_different = len(counter)
    n_unique = len([word for word, count in counter.items() if count == 1])
    n_repetition = n_different - n_unique
    return n, n_different, n_unique, n_repetition

def metrics(raw_text, tokens, lemmas, lang, task):
    fragment = Fragment(lang, task)

    n_tokens, n_different_tokens, n_unique_tokens, n_repetition_tokens = compute_counts(tokens)
    n_lemmas, n_different_lemmas, n_unique_lemmas, n_repetition_lemmas = compute_counts(lemmas)

    return {
        'n_tokens': n_tokens,
        'n_different_tokens': n_different_tokens,
        'n_unique_tokens': n_unique_tokens,
        'n_repetition_tokens': n_repetition_tokens,
        'n_lemmas': n_lemmas,
        'n_different_lemmas': n_different_lemmas,
        'n_unique_lemmas': n_unique_lemmas,
        'n_repetition_lemmas': n_repetition_lemmas,
        'n_fragments': fragment.counter(tokens),
        'n_fragments_context': fragment.context(tokens),
        'n_silent_pauses': fluency.count_silent_pauses(raw_text, lang),
        'n_filled_pauses': fluency.count_filled_pauses(raw_text, lang),
        'n_ucsf_silent_pauses': fluency.count_silent_pauses(raw_text, pause_marker='...'),
        'n_ucsf_filled_pauses': fluency.count_filled_pauses(raw_text, 'ucsf'),
    }
