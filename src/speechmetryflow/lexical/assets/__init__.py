# Correspondence between English and French POS labels
pos_mapping = {
    'ADJ': 'Adjectif',
    'ADP': 'Preposition',
    'ADV': 'Adverbe',
    'AUX': 'Auxiliaire',
    'CONJ': 'Conjonction',
    'CCONJ': 'Conjonction_de_coordination',
    'DET': 'Determinant',
    'INTJ': 'Interjection',
    'NOUN': 'Nom',
    'NUM': 'Numeral',
    'PART': 'Particule',
    'PRON': 'Pronom',
    'PROPN': 'Nom propre',
    'PUNCT': 'Ponctuation',
    'SCONJ': 'Conjonction_de_subordination',
    'SYM': 'Symbole',
    'VERB': 'Verbe',
    'X': 'Autre',
}

# Dictionary of deictic pronouns for each language
deictic_pronouns = {
    "en": {
        "spatial": {"here", "there", "this", "these", "that", "those"},
        "personal": {"i", "you", "he", "she", "it", "we", "they"},
        "temporal": {"now", "then", "soon", "tomorrow"}
    },
    "fr": {
        "spatial": {"ce", "cet", "cette", "ces", "celui-ci", "celle-ci", "ceux-ci", "celles-ci", "celui-là", "celle-là", "ceux-là", "celles-là", "y", "en"},
        "personal": {"je", "tu", "il", "elle", "nous", "vous", "ils", "elles"},
        "temporal": {"y", "en"}
    }
}

# List of undefined terms in English and French
indefinite_terms = {
    "en": [
        "thing", "stuff", "anything", "nothing", "anyone", "one", "either", "neither", "everyone", 
        "no one", "someone", "anybody", "everybody", "nobody", "somebody", "another", "the other", 
        "each", "little", "less", "much", "both", "few", "fewer", "many", "other", "others", "several",
        ],
    "fr": [
        "truc", "chose", "peu", "beaucoup", "quelques", "plusieurs", "quelqu'un", "tout le monde", 
        "personne", "chacun", "n'importe qui", "autre", "l'autre", "chaque", "ni l'un ni l'autre", 
        "les deux", "d'autres",
        ],
}