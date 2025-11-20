from speechmetryflow.semantic.assets import ICU_references


def compute_icu(text, lang, task):
    """
    Analyses the text to detect the presence of ICUs (Information Content Unique)
    associated with specific subjects, places, objects, and actions.

    Args:
        text (str): The text to be analysed.
        language (str): The language of the text ("fr" or "en").
        task (str): Image used to generate the text ("cookie" or "picnic").

    Returns:
        dict: A dictionary containing information about the presence of ICUs. Each ICU is associated with a key
        and the corresponding value is True if the ICU is found in the text, otherwise False.
    """
    ICU_dict = ICU_references.get(f"{task}_{lang}")

    if ICU_dict is None:
        return

    # Initialising the results dictionary
    icu_data = {f"icu_{icu}": False for icu in ICU_dict.keys()}

    # Verification of the presence of each ICU in the text
    for icu, words in ICU_dict.items():
        for word in words:
            if word in text:
                icu_data[f"icu_{icu}"] = True
                break  # Move to the next ICU as soon as a match is found

    return icu_data
