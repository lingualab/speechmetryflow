import pytest

import speechmetryflow as smf
from speechmetryflow.utils import compute_stemming


@pytest.mark.parametrize("tag", ["north", "phebus"])
def test_lexical(request, tag):
    text, expected, lang = request.getfixturevalue(f"data_{tag}")
    expected = expected.get("lexical")

    nlp = request.getfixturevalue(f"nlp_{lang}")
    doc = nlp(text)

    tokens_filtered = [token for token in doc if not token.is_punct]
    texts_filtered = [token.text for token in tokens_filtered]
    stems_filtered = compute_stemming(texts_filtered, lang)

    metrics = smf.lexical.metrics(doc, texts_filtered, stems_filtered, lang)

    # assert metrics == expected
    assert metrics.keys() == expected.keys()
    for key, expected_value in expected.items():
        assert metrics[key] == pytest.approx(expected_value, rel=1e-2), key
