import pandas as pd
import numpy as np
import importlib_resources


def load_database(tag, lang):
    assets_folder = importlib_resources.files(__name__) / "assets"

    if lang == "en":
        tag2df = {
            "concreteness": pd.read_csv(
                assets_folder / "concreteness.tsv",
                sep="\t",
                usecols=["Word", "Conc.M"],
                index_col="Word",
            ).squeeze(),
            "familiarity": pd.read_csv(
                assets_folder / "familiarity_imageability.tsv",
                sep="\t",
                usecols=["Words", "FAM_M"],
                index_col="Words",
            ).squeeze(),
            "imageability": pd.read_csv(
                assets_folder / "familiarity_imageability.tsv",
                sep="\t",
                usecols=["Words", "IMAG_M"],
                index_col="Words",
            ).squeeze(),
            "frequency": pd.read_csv(
                assets_folder / "frequency.tsv",
                sep="\t",
                usecols=["Word", "SUBTLWF"],
                index_col="Word",
            ).squeeze(),
            "valence": pd.read_csv(
                assets_folder / "valence.tsv",
                sep="\t",
                usecols=["Word", "V.Mean.Sum"],
                index_col="Word",
            ).squeeze(),
        }

    else:
        return

    return tag2df.get(tag)


def compute_database(tokens, lang, tag):
    """
    Compute the concreteness of words in a list from a concreteness database.

    Args:
        tokens (list): A list of words from which the average concreteness will be calculated.
        lang (str): language of the text.

    Returns:
        numpy.array: concreteness of the words.
    """
    data = load_database(tag, lang)
    if data is None:
        return

    return np.array(list(map(data.get, tokens))).astype(float)


def compute_concreteness(tokens, lang):
    """
    Compute the concreteness of words in a list from a concreteness database.

    Args:
        tokens (list): A list of words from which the average concreteness will be calculated.
        lang (str): language of the text.

    Returns:
        numpy.array: concreteness of the words.
    """
    return compute_database(tokens, lang, "concreteness")


def compute_familiarity(tokens, lang):
    """
    Compute the familiarity of words in a list from a familiarity database.

    Args:
        tokens (list): A list of words from which the average familiarity will be calculated.
        lang (str): language of the text.

    Returns:
        numpy.array: familiarity of the words.
    """
    return compute_database(tokens, lang, "familiarity")


def compute_imageability(tokens, lang):
    """
    Compute the imageability of words in a list from a imageability database.

    Args:
        tokens (list): A list of words from which the average imageability will be calculated.
        lang (str): language of the text.

    Returns:
        numpy.array: imageability of the words.
    """
    return compute_database(tokens, lang, "imageability")


def compute_frequency(tokens, lang):
    """
    Compute the frequency of words in a list from a frequency database.

    Args:
        tokens (list): A list of words from which the average frequency will be calculated.
        lang (str): language of the text.

    Returns:
        numpy.array: frequency of the words.
    """
    return compute_database(tokens, lang, "frequency")


def compute_valence(tokens, lang):
    """
    Compute the valence of words in a list from a valence database.

    Args:
        tokens (list): A list of words from which the average valence will be calculated.
        lang (str): language of the text.

    Returns:
        numpy.array: valence of the words.
    """
    return compute_database(tokens, lang, "valence")


TAG2FUNC = {
    "concreteness": compute_concreteness,
    "familiarity": compute_familiarity,
    "imageability": compute_imageability,
    "frequency": compute_frequency,
    "valence": compute_valence,
}
