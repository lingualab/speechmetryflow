# Database Caractéristiques syntaxiques

## Traductions des étiquettes de dépendance en français
dep_mapping = {
    'nsubj': 'Sujet_nominal',
    'csubj': 'Sujets_Clausaux',
    'ROOT': 'Racine',
    'det': 'Determinant',
    'amod': 'Modificateur_adjectival',
    'compound': 'Compose',
    'dobj': 'Objet_direct',
    'prep': 'Preposition',
    'pobj': 'Objet_de_preposition',
    'punct': 'Ponctuation',
    'expl': 'Element_expletif',
    'attr': 'Attribut',
    'acl': 'Clause_adjectivale',
    'advcl': 'Clause_adverbiale',
    'aux': 'Auxiliaire',
    'xcomp': 'Complement_ouvert',
    'ccomp': 'Complements_Clausaux_Non_Controles',
    'conj': 'Conjonction',
    'cc': 'Conjonction_de_coordination',
    'neg': 'Negation',
    'dative': 'Datif',
}

translation_dict = {
    'csubj': 'Sujets_Clausaux',
    'xcomp': 'Complements_Clausaux_Controles',
    'ccomp': 'Complements_Clausaux_Non_Controles',
    'advcl': 'Modificateurs_Clauses_Adverbiaux',
    'acl': 'Modificateurs_Clauses_Adnominaux'
}

## Dictionnaire des conjonctions de coordination par langue
coordinating_conjunctions = {
    'en': {"and", "but", "for", "nor", "or", "yet", "so"},
    'fr': {"et", "mais", "ou", "donc", "or", "ni", "car"}
}