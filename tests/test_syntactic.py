import pytest

import speechmetryflow as smf


@pytest.mark.parametrize("tag", ["north", "phebus"])
def test_syntactic(request, tag):
    text, expected, lang = request.getfixturevalue(f"data_{tag}")
    expected = expected.get("syntactic")

    nlp = request.getfixturevalue(f"nlp_{lang}")
    doc = nlp(text)

    metrics = smf.syntactic.metrics(doc, lang)

    # assert metrics == expected
    assert metrics.keys() == expected.keys()
    for key, expected_value in expected.items():
        assert metrics[key] == pytest.approx(expected_value, rel=1e-2), key
