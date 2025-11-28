import pytest
import json
import importlib_resources

import spacy
from textdescriptives.utils import _download_spacy_model


def nlp(lang):
    spacy_model = _download_spacy_model(lang, "lg")
    nlp = spacy.load(spacy_model)
    nlp.add_pipe("textdescriptives/all")
    return nlp

def get_data(filename_stem, lang):
    assets_folder = importlib_resources.files(__name__) / "assets"

    filename_txt = assets_folder / f"{filename_stem}.txt"
    with filename_txt.open("r") as txt:
        text = " ".join(txt.read().split("\n"))

    filename_json = assets_folder / f"{filename_stem}.json"
    with filename_json.open("r") as f:
        expected = json.load(f)

    return text, expected, lang

@pytest.fixture()
def nlp_en():
    return nlp("en")

@pytest.fixture()
def nlp_fr():
    return nlp("fr")

@pytest.fixture()
def data_north():
    return get_data("the_north_wind_and_the_sun", "en")

@pytest.fixture()
def data_phebus():
    return get_data("phébus-et-borée", "fr")
