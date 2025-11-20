import warnings
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
from collections import Counter

from speechmetryflow.lexical.assets import pos_mapping
from speechmetryflow.lexical.database import TAG2FUNC


class POS:
    def __init__(self, doc, lang):
        self.doc = doc
        self.lang = lang
        self.mapping = pos_mapping
        self.pos = [token.pos_ for token in self.doc]
        self.text = np.array([token.text for token in self.doc])
        self.counts = self._counts()
        self.len_text = len(doc)
        self.metrics = {}
        self._compute_metrics()

    def _counts(self):
        counts = Counter(pos_mapping.keys())
        counts.subtract(pos_mapping.keys())
        counts.update(self.pos)
        return counts

    def _compute_metrics(self):
        self.counter()
        self.proportions()
        self.count_open_class_words()
        self.count_closed_class_words()
        self.count_verb_inflection()
        self.count_verb_gerondif()
        self.compute_ratios()
        for window_shape in [10, 25, 40]:
            self.compute_mattr(window_shape)
        self.compute_database("concreteness")
        self.compute_database("familiarity")
        self.compute_database("imageability")
        self.compute_database("frequency")
        self.compute_database("valence")

    def proportions(self):
        for tag, count in self.counts.items():
            self.metrics[f"pos_prop_{tag}"] = (
                count / self.len_text if self.len_text > 0 else None
            )

    def counter(self):
        for tag, count in self.counts.items():
            self.metrics[f"pos_count_{tag}"] = count

    def count_open_class_words(self):
        open_classes = ["NOUN", "VERB", "ADJ", "ADV"]
        num = sum(self.counts[pos] for pos in open_classes)
        self.metrics["pos_count_open_words"] = num
        self.metrics["pos_prop_open_words"] = (
            num / self.len_text if self.len_text > 0 else None
        )

    def count_closed_class_words(self):
        closed_classes = ["CONJ", "PRON", "DET", "ADP"]
        num = sum(self.counts[pos] for pos in closed_classes)
        self.metrics["pos_count_closed_words"] = num
        self.metrics["pos_prop_closed_words"] = (
            num / self.len_text if self.len_text > 0 else None
        )

    def count_verb_inflection(self):
        """Verb inflection is the modification of a verb's form to express grammatical features such as tense."""
        num = sum(
            1 for token in self.doc if token.pos_ == "VERB" and token.tag_ != "VB"
        )
        self.metrics["pos_count_verb_inflection"] = num
        self.metrics["pos_prop_verb_inflection"] = (
            num / self.len_text if self.len_text > 0 else None
        )

    def count_verb_gerondif(self):
        """
        The gérondif is a French verb form expressing an action occurring in relation to another action.
        Example: Il écoute de la musique en travaillant.
        """
        num = sum(1 for token in self.doc if token.tag_ != "VBG")
        self.metrics["pos_count_verb_gerondif"] = num
        self.metrics["pos_prop_verb_gerondif"] = (
            num / self.len_text if self.len_text > 0 else None
        )

    def compute_ratios(self):
        """
        Computing the following ratios:
        - PRON / (NOUN + PRON)
        - NOUN / (NOUN + PRON)
        - NOUN / (NOUN + VERB)
        - VERB / (NOUN + VERB)
        - VERB_INFLECTION / VERB
        - VERB_GERONDIF / VERB
        """
        n_verb = self.counts["VERB"]
        n_noun = self.counts["NOUN"]
        n_pron = self.counts["PRON"]
        n_inflection = self.metrics["pos_count_verb_inflection"]
        n_gerondif = self.metrics["pos_count_verb_gerondif"]
        # Calcul des ratios
        self.metrics["PRON/(NOUN+PRON)"] = (
            n_pron / (n_noun + n_pron) if (n_noun + n_pron) > 0 else None
        )
        self.metrics["NOUN/(NOUN+PRON)"] = (
            n_noun / (n_noun + n_pron) if (n_noun + n_pron) > 0 else None
        )
        self.metrics["NOUN/(NOUN+VERB)"] = (
            n_noun / (n_noun + n_verb) if (n_noun + n_verb) > 0 else None
        )
        self.metrics["VERB/(NOUN+VERB)"] = (
            n_verb / (n_noun + n_verb) if (n_noun + n_verb) > 0 else None
        )
        self.metrics["VERB_INFLECTION/VERB"] = (
            n_inflection / n_verb if n_verb > 0 else None
        )
        self.metrics["VERB_GERONDIF/VERB"] = n_gerondif / n_verb if n_verb > 0 else None

    def compute_mattr(self, window_shape):
        """
        Compute the MATTR (Moving-Average Type-Token Ratio) using a window of specified size.

        Args:
            window_shape (int): The size of the text window to use.

        Returns:
            float: MATTR value.
        """
        try:
            windows = sliding_window_view(self.pos, window_shape=window_shape)
        except ValueError:
            # if window_shape is larger than input array shape
            return

        # Compute the TTR (Type-Token Ratio) for each window
        ttr_values = [len(set(window)) / window_shape for window in windows]

        self.metrics[f"pos_mattr_{window_shape}"] = np.mean(ttr_values)

    def compute_database(self, tag):
        """"""
        scores = TAG2FUNC[tag](self.text, self.lang)

        if scores is None:
            for pos_type in ["NOUN", "VERB", "ADJ"]:
                self.metrics[f"{tag}_mean_{pos_type}"] = None
            self.metrics[f"{tag}_mean_all_tokens"] = None
            return

        warnings.filterwarnings("error")
        for pos_type in ["NOUN", "VERB", "ADJ"]:
            pos_positions = np.nonzero(np.array(self.pos) == pos_type)[0]
            sub_scores = scores[pos_positions]
            try:
                score = np.nanmean(sub_scores)
            except RuntimeWarning:
                score = 0.0
            self.metrics[f"{tag}_mean_{pos_type}"] = score

        # For all tokens
        try:
            score = np.nanmean(scores)
        except RuntimeWarning:
            score = 0.0
        self.metrics[f"{tag}_mean_all_tokens"] = score

        warnings.resetwarnings()
