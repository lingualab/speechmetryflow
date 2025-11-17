import numpy as np

from transformers import AutoTokenizer, AutoModelWithLMHead, pipeline

from speechmetryflow.semantic.idea_density import compute_idea_density
from speechmetryflow.pragmatic.database import compute_database


def coherence_locale(doc):
    similarities = []
    for sent in doc.sents:
        tokens = [token for token in sent]
        similarity, = compute_idea_density(tokens, [len(tokens)]).values()
        similarities.append(similarity)
    return np.nanmean(similarities)


def compute_emotion(text):
    tokenizer = AutoTokenizer.from_pretrained("mrm8488/t5-base-finetuned-emotion")
    model = AutoModelWithLMHead.from_pretrained("mrm8488/t5-base-finetuned-emotion")
    input_ids = tokenizer.encode(text + '</s>', return_tensors='pt')
    output = model.generate(input_ids=input_ids, max_length=2)
    dec = [tokenizer.decode(ids) for ids in output]
    label = dec[0]
    # Supprimer le token <pad> de la sortie
    return label.replace("<pad>", "").strip()

def compute_sentiment(text):
    """
    Analyses the sentiment of a text using the mrm8488/t5-base-finetuned-emotion model.
    :param text: Text to be analysed.
    :return: Sentiment label.
    """
    model_path = "cardiffnlp/twitter-xlm-roberta-base-sentiment"
    # Creation of the sentiment analysis pipeline
    sentiment_task = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path, max_length=512, truncation=True)
    # Sentiment analysis
    result = sentiment_task(text)
    # Sentiment label retrieval
    label = result[0]['label']
    return label


def metrics(doc, lang, n_tokens):
    metrics = compute_database(doc, lang, n_tokens, 'uncertainty_words')
    metrics.update(compute_database(doc, lang, n_tokens, 'formulaic_expressions'))
    metrics.update(compute_database(doc, lang, n_tokens, 'modal_expressions'))
    metrics.update(compute_database(doc, lang, n_tokens, 'filler_expressions'))
    metrics.update(compute_database(doc, lang, n_tokens, 'difficulty_words'))
    metrics['coherence_locale'] = coherence_locale(doc)
    metrics['emotion'] = compute_emotion(doc.text)
    metrics['sentiment'] = compute_sentiment(doc.text)
    return metrics