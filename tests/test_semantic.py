import pytest

import speechmetryflow as smf


@pytest.mark.parametrize("tag,n_tokens", [("north", 113), ("phebus", 313)])
@pytest.mark.parametrize("task", ["cookie", "picnic"])
def test_semantic(request, tag, n_tokens, task):
    text, expected, lang = request.getfixturevalue(f"data_{tag}")
    expected = expected.get(f"semantic_{task}")

    nlp = request.getfixturevalue(f"nlp_{lang}")
    doc = nlp(text)

    tokens_filtered = [token for token in doc if not token.is_punct]

    metrics = smf.semantic.metrics(
        text,
        tokens_filtered,
        lang,
        task,
        n_tokens,
    )

    # assert metrics == expected
    assert metrics.keys() == expected.keys()
    for key, expected_value in expected.items():
        assert metrics[key] == pytest.approx(expected_value, rel=1e-2), key
