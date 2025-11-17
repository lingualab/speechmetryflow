''''''

from typing import Dict

from collections import Counter


def metrics(text: str) -> Dict:
    disfluency_counter = Counter(text)
    return {
        "UCSF_disfluency_single_repetition": disfluency_counter["="],
        "UCSF_disfluency_multiple_repetitions": disfluency_counter["@"],
        "UCSF_disfluency_repeated_phrase": disfluency_counter["&"],
        "UCSF_disfluency_restart_rephrase": disfluency_counter["#"],
        "UCSF_disfluency_partial_word_false_start": disfluency_counter["%"],
        "UCSF_disfluency_spoonerism": disfluency_counter["$"],
    }


def cleaning(text: str) -> str:
    for char in "=@&#%$":
        text = text.replace(char, "")
    return text