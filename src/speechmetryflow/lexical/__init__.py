from speechmetryflow.lexical.part_of_speech import POS
from speechmetryflow.lexical.utils import count_deictic_pronouns, count_indefinite_terms, compute_honore_r_stat, compute_brunet_index

def metrics(doc, tokens, stems, lang):
    pos = POS(doc, lang)
    metrics = pos.metrics
    metrics.update(count_deictic_pronouns(tokens, lang))
    metrics.update(count_indefinite_terms(tokens, lang))
    metrics['honore_r_stat'] = compute_honore_r_stat(stems)
    metrics['brunet_w_index'] = compute_brunet_index(stems)
    return metrics