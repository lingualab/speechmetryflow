""""""

from typing import Dict

import click
import json
import spacy

from textdescriptives.utils import _download_spacy_model
from textdescriptives.extractors import extract_dict
from pathlib import Path

import speechmetryflow as smf
from speechmetryflow.utils import compute_stemming


@click.command()
@click.option('--lang', '-l', default='en')
@click.option('--task', '-t')
@click.option('--output', '-o', type=click.Path(dir_okay=False))
@click.option('--clobber', is_flag=True)
@click.argument('text_path', type=click.Path(exists=True, dir_okay=False))
def extract(
    text_path: Path,
    lang: str = None,
    task: str = None,
    output: Path = None,
    clobber: bool = False,
) -> Dict:
    # Read input text_path
    text_path = Path(text_path)
    with text_path.open('r') as txt:
        raw_text = ' '.join(txt.read().split('\n'))

    # Output
    if output is None:
        output = Path(f'{text_path.stem}_metrics-speechmetryflow.json')
    else:
        output = Path(output)

    # Check if output file already exists
    if output.exists() and not clobber:
        raise FileExistsError(f'File {output} already exists, use --clobber to overwrite.')
    
    # Disfluency metrics from UCSF
    ucsf_disfluency_metrics = smf.ucsf_disfluency.metrics(raw_text)
    text = smf.ucsf_disfluency.cleaning(raw_text)

    # General cleaning
    text = smf.utils.general_cleaning(text)

    # TextDescriptives pipeline
    spacy_model = _download_spacy_model(lang, 'lg')
    nlp = spacy.load(spacy_model)
    nlp.add_pipe('textdescriptives/all')
    doc = nlp(text)

    tokens_filtered = [token for token in doc if not token.is_punct]
    texts_filtered = [token.text for token in tokens_filtered]
    lemmas_filtered = [token.lemma_ for token in tokens_filtered]
    stems_filtered = compute_stemming(texts_filtered, lang)

    # metrics containers
    smf_metrics = {
        "filename": text_path.name,
        "participant_id": text_path.name.split('_')[0],
        "language": lang,
        "spacy_model" : spacy_model,
    }
    smf_metrics.update(ucsf_disfluency_metrics)

    td_metrics = {
        "filename": text_path.name,
        "participant_id": text_path.name.split('_')[0],
        "language": lang,
        "spacy_model" : spacy_model,
    }
    td_metrics.update(extract_dict(doc)[0])

    # speech_production
    speech_production_metrics = smf.speech_production.metrics(raw_text, texts_filtered, lemmas_filtered, lang, task)
    smf_metrics.update(speech_production_metrics)

    # lexical
    lexical_metrics = smf.lexical.metrics(doc, texts_filtered, stems_filtered, lang)
    smf_metrics.update(lexical_metrics)

    # semantic
    semantic_metrics = smf.semantic.metrics(raw_text, tokens_filtered, lang, task, speech_production_metrics['n_tokens'])
    smf_metrics.update(semantic_metrics)

    # syntactic
    syntactic_metrics = smf.syntactic.metrics(doc, lang)
    smf_metrics.update(syntactic_metrics)

    # pragmatic
    pragmatic_metrics = smf.pragmatic.metrics(doc, lang, speech_production_metrics['n_tokens'])
    smf_metrics.update(pragmatic_metrics)

    # write output
    with output.open('w', encoding="utf-8") as f:
        json.dump(smf_metrics, f, indent=4)
    
    output_td = Path(f'{text_path.stem}_metrics-textdescriptives.json')
    with output_td.open('w', encoding="utf-8") as f:
        json.dump(td_metrics, f, indent=4)


@click.command()
def download():
    import nltk
    nltk.download('words')

    _download_spacy_model('en', 'lg')
    _download_spacy_model('fr', 'lg')

    from transformers import AutoTokenizer, AutoModelWithLMHead, pipeline
    AutoTokenizer.from_pretrained('mrm8488/t5-base-finetuned-emotion', legacy=False)
    AutoModelWithLMHead.from_pretrained('mrm8488/t5-base-finetuned-emotion')
    model_path = 'cardiffnlp/twitter-xlm-roberta-base-sentiment'
    pipeline('sentiment-analysis', model=model_path, tokenizer=model_path)