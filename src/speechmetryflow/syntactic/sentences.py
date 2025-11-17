
from typing import Iterable, Dict, Any, Union
import spacy

from speechmetryflow.syntactic.assets import coordinating_conjunctions


class Sentences:

    def __init__(self, doc, lang):
        self.doc = doc
        self.lang = lang
        self.len_doc = len(doc)
        self.metrics = {}
        self._compute_metrics()

    def _compute_metrics(self):
        # average sentence length in the text
        self.metrics['mean_length_sentence'] = self.len_doc / len(list(self.doc.sents))

        # Count type of sentences
        incomplete = 0
        prepositional = 0
        verbal = 0
        conjunctions = 0
        for sentence in self.doc.sents:
            incomplete += is_incomplete(sentence)
            prepositional += is_prepositional(sentence)
            verbal += is_verbal(sentence)
            conjunctions += is_conjunctions(sentence, self.lang)
        self.metrics['n_incomplete_sentences'] = incomplete
        self.metrics['n_prepositional_sentences'] = prepositional
        self.metrics['n_verbal_sentences'] = verbal

        if self.lang in coordinating_conjunctions.keys():
            self.metrics['n_conjunctions_sentences'] = conjunctions
            self.metrics['prop_conjunctions_sentences'] = conjunctions / self.len_doc
        else:
            self.metrics['n_conjunctions_sentences'] = None
            self.metrics['prop_conjunctions_sentences'] = None


def is_incomplete(sentence: Iterable[spacy.tokens.Token]) -> bool:
    """
    Determine whether a sentence is syntactically incomplete.

    A sentence is considered incomplete if it lacks either a subject
    (a token with dependency label 'nsubj' or 'csubj') or a main verb
    (a token with part-of-speech tag 'VERB').

    Parameters
    ----------
    sentence : Iterable[spacy.tokens.Token]
        A sequence of SpaCy token objects representing the sentence.

    Returns
    -------
    bool
        True if the sentence is incomplete (missing subject or verb),
        False otherwise.
    """
    sent_pos = [token.pos_ for token in sentence]
    sent_dep = [token.dep_ for token in sentence]
    has_subject = 'nsubj' in sent_dep or 'csubj' in sent_dep
    has_verb = 'VERB' in sent_pos
    return not (has_verb and has_subject)

def is_prepositional(sentence: Iterable[spacy.tokens.Token]) -> bool:
    """
    Determine whether a sentence is headed by or centered around
    a prepositional structure.

    The function checks if the sentence contains at least one preposition
    (token with part-of-speech tag 'ADP') that governs an object
    (dependency label 'pobj' or 'dobj'). This helps identify sentences
    whose main syntactic relation is prepositional.

    Parameters
    ----------
    sentence : Iterable[spacy.tokens.Token]
        A sequence of spacy token objects representing the sentence.

    Returns
    -------
    bool
        True if the sentence contains a prepositional structure
        (a preposition with an object), False otherwise.
    """
    for token in sentence:
        if token.pos_ == 'ADP':  # 'ADP' is the POS tag for prepositions in spacy
            # Check if the preposition has an object as a dependent
            return any(child.dep_ in ["pobj", "dobj"] for child in token.children)
    return False

def is_verbal(sentence: Iterable[spacy.tokens.Token]) -> bool:
    """
    Determine whether a sentence contains a verb.

    The function checks if any token in the sentence has a part-of-speech
    tag of 'VERB', indicating the presence of a verbal predicate or
    verbal structure.

    Parameters
    ----------
    sentence : Iterable[spacy.tokens.Token]
        A sequence of SpaCy token objects representing the sentence.

    Returns
    -------
    bool
        True if the sentence contains at least one verb, False otherwise.
    """
    return any(token.pos_ == 'VERB' for token in sentence)

def is_conjunctions(sentence: Iterable[spacy.tokens.Token], lang: str) -> bool:
    """
    Determine whether a sentence contains any coordinating conjunctions.

    Parameters
    ----------
    sentence : Iterable[spacy.tokens.Token]
        A sequence of SpaCy token objects representing the sentence.
    lang : str
        The ISO language code of the sentence (e.g., 'en' for English, 'fr' for French).

    Returns
    -------
    bool
        True if the sentence contains at least one coordinating conjunction,
        False otherwise.
    """
    conjunctions = coordinating_conjunctions.get(lang, set())
    return any(token.lower_ in conjunctions for token in sentence)

def nominal_sentences_stats(doc) -> Dict[str, Any]:
    """
    Compute statistics about nominal sentences (noun chunks).

    Returns
    -------
        - "n_nominal_sentences": int  
        Number of nominal sentences (noun chunks)
        - "mean_length_nominal_sentence": float  
        Average number of tokens per nominal sentence
        - "prop_nominal_sentences": float  
        Proportion of nominal sentences relative to the document length
    """
    nominal_sentences = [chunk for chunk in doc.noun_chunks]
    n_nominal_sentences = len(nominal_sentences)
    length_nominal_sentences = sum(len(chunk) for chunk in nominal_sentences)
    mean_length_nominal_sentence = length_nominal_sentences / n_nominal_sentences
    return {
        "n_nominal_sentences": n_nominal_sentences,
        "mean_length_nominal_sentence": mean_length_nominal_sentence,
        "prop_nominal_sentences": n_nominal_sentences / len(doc)
    }

def clauses_per_sentence(doc: spacy.tokens.Doc) -> Union[float, None]:
    """
    Compute the average number of clauses per sentence in a SpaCy document.

    A clause is identified by the presence of specific dependency relations:
    - 'csubj' (clausal subject)
    - 'ccomp' (clausal complement)
    - 'xcomp' (open clausal complement)

    The function counts all tokens with these dependencies and divides by the
    total number of sentences in the document.

    Parameters
    ----------
    doc : spacy.tokens.Doc
        A SpaCy Doc object representing the processed text.

    Returns
    -------
    float or None
        The mean number of clauses per sentence.
        Returns None if the document contains no sentences.
    """
    # Count tokens whose dependency label indicates a clause
    n_clauses = sum(1 for token in doc if token.dep_ in ["csubj", "ccomp", "xcomp"])
    n_sents = len(list(doc.sents))
    return n_clauses / n_sents if n_sents else None