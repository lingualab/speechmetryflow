from speechmetryflow.speech_production.assets import filled_pauses


def count_silent_pauses(text, lang=None, pause_marker=None):
    """
    Counts the total number of occurrences of "<pause_marker>" in the text, according to the specified language.

    Args:
    text (str): The text to be analysed.
    lang (str): The language of the text ('en' or 'fr').
    pause_marker (str): Overwrite the specific language pause_marker

    Returns:
    int: The number of occurrences of silent pauses.
    """
    if pause_marker is None:
        pause_markers = {"en": "[break]", "fr": "[pause]"}
        pause_marker = pause_markers.get(lang)

    if pause_marker is None:
        return

    return text.count(pause_marker)


def count_filled_pauses(text, lang):
    """
    Counts the total number of occurrences of specified words in the text, according to language.

    Args:
    text (str): The text to be analysed.
    language (str): The language of the text ('en' or 'fr').

    Returns:
    int: The number of occurrences of filled pauses.
    """
    pauses = filled_pauses.get(lang)

    if pauses is None:
        return

    return sum(text.count(pause) for pause in pauses)
