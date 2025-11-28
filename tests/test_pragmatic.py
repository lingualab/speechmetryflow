import pytest

import speechmetryflow as smf


@pytest.mark.parametrize("tag,n_tokens", [("north", 113), ("phebus", 313)])
def test_pragmatic(request, tag, n_tokens):
    text, expected, lang = request.getfixturevalue(f"data_{tag}")
    expected = expected.get("pragmatic")

    nlp = request.getfixturevalue(f"nlp_{lang}")
    doc = nlp(text)

    metrics = smf.pragmatic.metrics(doc, lang, n_tokens)

    # assert metrics == expected
    assert metrics.keys() == expected.keys()
    for key, expected_value in expected.items():
        assert metrics[key] == pytest.approx(expected_value, rel=1e-2), key
