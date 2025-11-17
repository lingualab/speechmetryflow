''''''

import importlib_resources
import json

from speechmetryflow.speech_production.assets import target_words

class Fragment:

    def __init__(self, lang, task):
        self.lang = lang
        self.task = task
        self.valid_words = self._load_valid_words()
        self.target_words = target_words.get(lang)

    def _load_valid_words(self):
        if self.lang == 'en':
            from nltk.corpus import words
            return set(words.words())
        
        elif self.lang == 'fr':
            resources = importlib_resources.files(__name__) / 'assets'
            with (resources / 'words_fr.json').open('r', encoding='utf-8') as file:
                return set(json.load(file))
            
        else:
            print(f'language "{self.lang}" not currently recognized for fragment counting')
            return None
        
    def counter(self, tokens, verbose=False):
        """
        Identifies and counts word fragments in a list of tokens

        Args:
        tokens (list): The list of tokens
        verbose (bool): If true, displays fragments found.

        Returns:
        int: The number of word fragments
        """
        if self.valid_words is None:
            return
        
        # Fragments identification
        fragments = [token for token in tokens if token.lower() not in self.valid_words]

        if verbose:
            print(fragments)

        return len(fragments)
        
    def context(self, tokens):
        """
        Identifies and counts word fragments in a list of tokens

        Args:
        tokens (list): The list of tokens
        verbose (bool): If true, displays fragments found.

        Returns:
        int: The number of word fragments
        """
        if self.task != 'cookie':
            return
        
        if self.target_words is None:
            return
        
        context_counter = 0
        # Browse two consecutives tokens
        for comb in zip(tokens, tokens[1:]):
            context_counter += comb in self.target_words            
        return context_counter
