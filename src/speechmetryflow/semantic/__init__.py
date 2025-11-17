from speechmetryflow.semantic.icu import compute_icu
from speechmetryflow.semantic.idea_density import compute_idea_density


def metrics(text, tokens, lang, task, n_tokens):
    metrics = compute_idea_density(tokens, [3, 10, 25, 40])

    icu_data = compute_icu(text, lang, task)

    # Total number of True ICU anf ICU efficacity
    if icu_data is None:
        n_icu_true = None
        icu_efficacity = None

    else:
        metrics.update(icu_data)
        n_icu_true = sum(icu_data.values())
        icu_efficacity = n_tokens / n_icu_true

    metrics['n_icu_true'] = n_icu_true
    metrics['icu_efficacity'] = icu_efficacity

    return metrics