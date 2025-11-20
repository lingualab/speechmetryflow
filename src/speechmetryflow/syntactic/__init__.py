from typing import Dict, Union
import spacy


from speechmetryflow.syntactic.dependency import Dependency
from speechmetryflow.syntactic.sentences import (
    Sentences,
    nominal_sentences_stats,
    clauses_per_sentence,
)


def count_verb_tenses(doc: spacy.tokens.Doc, lang: str) -> Dict[str, float | None]:
    """
    Count the number and proportion of verbs in different tenses within a document.

    This function analyzes verb tenses for English texts based on part-of-speech
    tags provided by SpaCy. For non-English languages, it returns `None` values
    for all tense-related fields.

    The following English verb tags are used:
    - Present tense: VBP, VBZ, VBG
    - Past tense: VBD, VBN

    Parameters
    ----------
    doc : spacy.tokens.Doc
        A SpaCy Doc object representing the processed text.
    lang : str
        The ISO language code of the document (e.g., 'en' for English).

    Returns
    -------
    dict
        A dictionary containing the following keys:
        - "n_present_verb": int or None
          Number of verbs in the present tense.
        - "prop_present_verb": float or None
          Proportion of present-tense verbs relative to document length.
        - "n_past_verb": int or None
          Number of verbs in the past tense.
        - "prop_past_verb": float or None
          Proportion of past-tense verbs relative to document length.
    """
    if lang != "en":
        empty_results = {}
        for tense in ["present", "past"]:
            empty_results[f"n_{tense}_verb"] = None
            empty_results[f"prop_{tense}_verb"] = None
        return empty_results

    verbs = [token for token in doc if token.pos_ == "VERB"]

    tenses = {
        "present": 0,
        "past": 0,
    }

    for verb in verbs:
        if verb.tag_ in [
            "VBP",
            "VBZ",
            "VBG",
        ]:  # Typical tags for the present tense in English
            tenses["present"] += 1
        elif verb.tag_ in ["VBD", "VBN"]:  # Typical tags for the past tense in English
            tenses["past"] += 1
        # Note: the future tense in English is often marked by auxiliary verbs and does not have a specific tag.

    results = {}
    for tense, count in tenses.items():
        results[f"n_{tense}_verb"] = count
        results[f"prop_{tense}_verb"] = count / len(doc)

    return results


def nouns_with_determiners_proportion(doc: spacy.tokens.Doc) -> Union[float, None]:
    """
    Compute the proportion of nouns in a document that have determiners.

    The function identifies all tokens with the part-of-speech tag "NOUN"
    and checks how many of them have at least one dependent token with
    the dependency label "det" (determiner). It then returns the ratio
    of such nouns to the total number of nouns in the document.

    Parameters
    ----------
    doc : spacy.tokens.Doc
        A SpaCy Doc object representing the processed text.

    Returns
    -------
    float or None
        The proportion of nouns that have determiners.
        Returns None if the document contains no nouns.
    """
    nouns = [token for token in doc if token.pos_ == "NOUN"]
    n_nouns = len(nouns)

    determiners = 0
    for noun in nouns:
        if any(child.dep_ == "det" for child in noun.children):
            determiners += 1

    return determiners / n_nouns if n_nouns else None


def metrics(doc, lang):
    dependency = Dependency(doc)
    metrics = dependency.metrics
    metrics.update(Sentences(doc, lang).metrics)
    metrics.update(nominal_sentences_stats(doc))
    metrics.update(count_verb_tenses(doc, lang))
    metrics["clauses_per_sentence"] = clauses_per_sentence(doc)
    metrics["nouns_with_determiners_proportion"] = nouns_with_determiners_proportion(
        doc
    )
    return metrics
