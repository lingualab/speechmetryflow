
import numpy as np
from collections import Counter

from speechmetryflow.syntactic.assets import dep_mapping


class Dependency:

    def __init__(self, doc):
        self.doc = doc
        self.dependencies = [token.dep_ for token in doc]
        self.counts = self._counts()
        self.len_doc = len(doc)
        self.distances = [abs(token.i - token.head.i) for token in self.doc]
        self.lefts = [token.n_lefts for token in self.doc]
        self.rights = [token.n_rights for token in self.doc]
        self.metrics = {}
        self._compute_metrics()

    def _counts(self):
        counts = Counter(dep_mapping.keys())
        counts.subtract(dep_mapping.keys())
        counts.update(self.dependencies)
        return counts
    
    def _compute_metrics(self):
        self.counter()
        self.proportions()

        # average and maximum lengths of dependencies
        self.metrics['dep_mean_distance'] = np.mean(self.distances)
        self.metrics['dep_max_distance'] = max(self.distances)

        # number of left-dependencies and right-dependencies for each word.
        self.metrics['dep_total_n_lefts'] = sum(self.lefts)
        self.metrics['dep_total_n_rights'] = sum(self.rights)
        self.metrics['dep_mean_n_lefts'] = np.mean(self.lefts)
        self.metrics['dep_mean_n_rights'] = np.mean(self.rights)

    def counter(self):
        for tag, count in self.counts.items():
            self.metrics[f'dep_count_{tag}'] = count

    def proportions(self):
        for tag, count in self.counts.items():
            self.metrics[f'dep_prop_{tag}'] = count / self.len_doc if self.len_doc > 0 else None

    