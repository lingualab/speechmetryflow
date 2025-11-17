import math

from speechmetryflow.lexical.assets import deictic_pronouns, indefinite_terms
from speechmetryflow.speech_production import compute_counts


def count_deictic_pronouns(tokens, lang):
    """
    Counts deictic pronouns in a text in English or French.

    Args:
    - tokens list[(str)]: The text to be analysed.
    - lang (str): The language of the text ("fr", "en").

    Returns:
    - dict: A dictionary with the counts of spatial, personal, temporal pronouns and the total.
    """
    deictic_pronouns_data = deictic_pronouns.get(lang)

    if deictic_pronouns_data is None:
        return {
            "n_deictic_pronouns_spatial": None,
            "n_deictic_pronouns_personal": None,
            "n_deictic_pronouns_temporal": None,
            "n_deictic_pronouns_total": None,
            "prop_deictic_pronouns_spatial": None,
            "prop_deictic_pronouns_personal": None,
            "prop_deictic_pronouns_temporal": None,
            "prop_deictic_pronouns_total": None,
            }
    
    len_text = len(tokens)
    n_spatial = sum(token in deictic_pronouns_data["spatial"] for token in tokens)
    n_personal = sum(token in deictic_pronouns_data["personal"] for token in tokens)
    n_temporal = sum(token in deictic_pronouns_data["temporal"] for token in tokens)
    n_total = n_spatial + n_personal + n_temporal
    
    return {
            "n_deictic_pronouns_spatial": n_spatial,
            "n_deictic_pronouns_personal": n_personal,
            "n_deictic_pronouns_temporal": n_temporal,
            "n_deictic_pronouns_total": n_total,
            "prop_deictic_pronouns_spatial": n_spatial / len_text if len_text > 0 else None,
            "prop_deictic_pronouns_personal": n_personal / len_text if len_text > 0 else None,
            "prop_deictic_pronouns_temporal": n_temporal / len_text if len_text > 0 else None,
            "prop_deictic_pronouns_total": n_total / len_text if len_text > 0 else None,
            }

def count_indefinite_terms(tokens, lang):
    """
    Counts the number of indefinite terms in a text based on the language.

    Args:
    - tokens list[(str)]: The text to be analysed.
    - lang (str): The language of the text ("fr", "en").

    Returns:
        int: The number of indefinite terms found in the text.
    """
    indefinite_terms_data = indefinite_terms.get(lang)

    if indefinite_terms_data is None:
        return
    
    len_text = len(tokens)
    num = sum(token in indefinite_terms_data for token in tokens)
    return {
        'n_indefinite_terms': num,
        'prop_indefinite_terms': num / len_text if len_text > 0 else None,
    }

def compute_honore_r_stat(stems):
    """
    Compute Honore's R statistic.
    100*log(N)/(1-(n_unique/n_different))

    Args:
        stems list(str): list of stems to compute.

    Returns:
        float: value of Honore's R statistic.
    """
    if stems is None:
        return
    
    N, n_different, n_unique, _ = compute_counts(stems)
    return (100 * math.log(N)) / (1 - (n_unique / n_different))

def compute_brunet_index(stems):
    """
    Compute the Brunet index
    A measure of lexical diversity linking the length of the sample to the number of different words used in it.
    Lower values of W correspond to richer texts.
    Stemming is done on words and only the stems are considered.

    Formula: W = N ^ (V ^ (-0.165))
        W (float): Brunet's index.
        N (int): total number of stems.
        V (int): number of different stems.

    Args:
        stems list(str): list of stems to compute.

    Returns:
        float: value of Brunet index.
    """
    if stems is None:
        return
    
    N, n_different, _, _ = compute_counts(stems)

    return math.pow(N, math.pow(n_different, -0.165))