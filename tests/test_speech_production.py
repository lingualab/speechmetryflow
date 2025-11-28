import pytest

import speechmetryflow as smf


@pytest.mark.parametrize("tag", ["north", "phebus"])
@pytest.mark.parametrize("task", ["cookie", "picnic"])
def test_speech_production(request, tag, task):
    text, expected, lang = request.getfixturevalue(f"data_{tag}")
    expected = expected.get(f"speech_production_{task}")

    nlp = request.getfixturevalue(f"nlp_{lang}")
    doc = nlp(text)

    tokens_filtered = [token for token in doc if not token.is_punct]
    texts_filtered = [token.text for token in tokens_filtered]
    lemmas_filtered = [token.lemma_ for token in tokens_filtered]

    metrics = smf.speech_production.metrics(
        text, texts_filtered, lemmas_filtered, lang=lang, task=task
    )

    # assert metrics == expected
    assert metrics.keys() == expected.keys()
    for key, expected_value in expected.items():
        assert metrics[key] == pytest.approx(expected_value, rel=1e-2), key
