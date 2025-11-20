""""""

import re
from nltk.stem import SnowballStemmer


def general_cleaning(raw_text: str) -> str:
    """
    Cleans up text by performing several cleaning operations

    Args:
    raw_text (str): The text to be cleaned up

    Returns:
    str: Cleaned up text
    """
    # Removes content between square brackets ([...])
    text = re.sub(r"\[.*?\]", "", raw_text)

    # Removes punctuation, keeping letters, apostrophes, spaces, periods, and question marks
    text = re.sub(r"[^\w\’ \.\?]", "", text)

    # Removes periods following a space
    text = re.sub(r"\s\.", "", text)

    # Replaces two consecutive spaces with a single space
    text = re.sub(r"\s\s+", " ", text)

    return text


def compute_stemming(tokens, lang):
    """
    Stemming with Snowball
    https://snowballstem.org/

    Args:
        tokens list(str): text to compute.
        lang (str): language of the text.

    Returns:
        list(str): stems from SnowballStemmer.
    """
    if lang == "en":
        stemmer = SnowballStemmer("english")

    elif lang == "fr":
        stemmer = SnowballStemmer("french")

    else:
        return

    return list(map(stemmer.stem, tokens))
