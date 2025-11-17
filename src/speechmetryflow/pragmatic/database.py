

from speechmetryflow.pragmatic import assets


def compute_database(doc, lang, n_tokens, tag):
    """
    Compute the concreteness of words in a list from a concreteness database.

    Args:
        tokens (list): A list of words from which the average concreteness will be calculated.
        lang (str): language of the text.

    Returns:
        numpy.array: concreteness of the words.
    """
    tag2database = {
        'uncertainty_words': assets.uncertainty_words,
        'formulaic_expressions': assets.formulaic_expressions,
        'modal_expressions': assets.modal_expressions,
        'filler_expressions': assets.filler_expressions,
        'difficulty_words': assets.difficulty_words,
    }
    data = tag2database[tag].get(lang)
    if data is None:
        return {
            f'n_{tag}': None,
            f'prop_{tag}': None,
        }
    
    text = doc.text.lower()
    count = sum(text.count(expression) for expression in data)
    return {
            f'n_{tag}': count,
            f'prop_{tag}': count / n_tokens if n_tokens else None,
        }

def compute_concreteness(tokens, lang):
    """
    Compute the concreteness of words in a list from a concreteness database.

    Args:
        tokens (list): A list of words from which the average concreteness will be calculated.
        lang (str): language of the text.

    Returns:
        numpy.array: concreteness of the words.
    """
    return compute_database(tokens, lang, 'concreteness')

def compute_familiarity(tokens, lang):
    """
    Compute the familiarity of words in a list from a familiarity database.

    Args:
        tokens (list): A list of words from which the average familiarity will be calculated.
        lang (str): language of the text.

    Returns:
        numpy.array: familiarity of the words.
    """
    return compute_database(tokens, lang, 'familiarity')

def compute_imageability(tokens, lang):
    """
    Compute the imageability of words in a list from a imageability database.

    Args:
        tokens (list): A list of words from which the average imageability will be calculated.
        lang (str): language of the text.

    Returns:
        numpy.array: imageability of the words.
    """
    return compute_database(tokens, lang, 'imageability')

def compute_frequency(tokens, lang):
    """
    Compute the frequency of words in a list from a frequency database.

    Args:
        tokens (list): A list of words from which the average frequency will be calculated.
        lang (str): language of the text.

    Returns:
        numpy.array: frequency of the words.
    """
    return compute_database(tokens, lang, 'frequency')

def compute_valence(tokens, lang):
    """
    Compute the valence of words in a list from a valence database.

    Args:
        tokens (list): A list of words from which the average valence will be calculated.
        lang (str): language of the text.

    Returns:
        numpy.array: valence of the words.
    """
    return compute_database(tokens, lang, 'valence')


TAG2FUNC = {
    'concreteness': compute_concreteness,
    'familiarity': compute_familiarity,
    'imageability': compute_imageability,
    'frequency': compute_frequency,
    'valence': compute_valence,
}