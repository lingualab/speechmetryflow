# Speech production

## Definitions

### Lemmatization

A lemma in the context of linguistics is the basic or reference canonical form of a word. In other words, it's the form in which a word is listed in a dictionary or used to represent all the inflectional variants of a word. The idea is to group together the different forms of a word (such as future past tenses, plurals etc.) in a single standardized form.

Lemmas are not punctuation markers or filled pauses (such as "hmm" or "uh"), which are usually omitted in lexical analysis because they carry no specific lexical meaning.

Examples:

- "dog", "dogs" is "dog".
- "best", "better" is "good"

1. **Process**: Lemmatization involves a complete morphological analysis of words to deduce their canonical form or lemma. Lemmatization takes into account the context of the word, its gender, number and tense, to determine its basic form.
2. **Example**: Taking your example, the word "find" is reduced to its basic form "find". Unlike stemming, the result of lemmatization is always a valid, recognizable word.
3. **Usage**: Lemmatization is often used in situations where precision is crucial, such as in natural language understanding systems or linguistic applications where context understanding and semantic precision are important.

### Phoneme

A phoneme is a basic unit of sound in a language that distinguishes one word from another. It is the smallest unit of sound that can change the meaning of a word. Phonemes are abstract concepts used to analyze how sounds function in a particular language. They are not the sounds themselves, but rather categories of sounds that can be pronounced in different ways by different speakers, yet still be perceived as the same sound.

In French, the sounds /p/ and /b/ are distinct phonemes, differentiating words like "patte" and "batte". The phoneme /k/ is present in the words "café" and "quai", although the sound is produced differently in each word (with a different letter).

In English, the /t/ and /d/ phonemes differentiate the words "tap" and "dap" (a made-up word that sounds different thanks to the different initial phoneme).

### Tokenization

Breakdown of text into several parts called *tokens*.

Example: "You will find the document in question attached" gives "You", "will find", "in", "part", "attached", "the", "document", "in", "question".

### Stemming

1. **Process**: Stemming consists in cutting off the ends (suffixes and sometimes prefixes) of words to achieve a simplified form. This process is generally heuristic, and takes no account of the context or complete morphology of words. It is based on simple, fixed rules for truncating words.
2. **Example**: In your example, "trouverez" becomes "trouv". Here the suffix "-erez" is removed to arrive at the root "trouv". This root is not necessarily a valid word in itself.
3. **Usage**: Stemming is often used in search and filter systems where precision is not critical, but speed and simplicity of the process are important.

### Lemmatization

This involves performing the same task as stemming, but using a vocabulary and a fine-grained analysis of word construction. Lemmatization** removes only inflexible endings and thus **isolates the canonical form of the word** known as the lemma.

### Semantic similarity

Semantic similarity measures how close two words or concepts are in meaning. In the context of word embeddings, this is often expressed by the proximity of their vectors in vector space.

### Word Embedding

Word Embedding is an encoding method that aims to represent the words or phrases of a text by vectors of real numbers described in a Vector Space Model.

In simple terms, each word of the vocabulary V under study will be represented by a vector of size m. The principle of Word Embedding is to project each of these words into a vector space of fixed size N (N being different from m). In other words, whatever the size of the vocabulary, we need to be able to project a word into its own space.

### Embedding templates

CBOW (Continuous Bag-of-Words): In this model, the target word is predicted from surrounding words. It takes into account the context represented by neighboring words to predict the target word.

Skip-Gram: Inverse of CBOW, this model predicts the context of a given word. It is effective for representing rare words or phrases.

### Dependency tree

In a dependency grammar, a sentence is represented as a tree. Each word in the sentence is a node in this tree. The links (or arcs) between these words represent syntactic relationships.

## Variables

### Sample length

Total number of words in the sample. This is the total number of lemmas that are not punctuation markers, including filled pauses (e.g. hmmm).

### Word fragments

Production of only part of a word's phonemes without sound replacements or articulation errors. May or may not be followed by full word production. A word fragment is a portion of a word that contains one or more phonemes of that word, but not all its phonemes. In other words, it's a part of a word, not the complete word.

- Fragments Identification**: In the speech or text sample you are looking for occurrences where only part of a word is spoken or written. This can be the beginning of a word, the end or even the middle, as long as it's not the whole word.
- Fragments Count**: You then count the total number of these fragments in the sample. Each occurrence of a word fragment is counted as a separate unit.
- Exclude Pronunciation Errors and Sound Substitutions**: It's important to note that word fragments should not be confused with pronunciation errors or sound substitutions. These are specific occurrences where missing phonemes are not replaced by other sounds or errors.
- **Example** : "I her kitchkitchen" An example of this would be in a speech sample where someone starts to say a word but stops before finishing it like starting to say "incomprehens..." instead of "incomprehensible". Each time this happens it would count as a word fragment.

### Fluency

#### Silent pauses

Segments of the sample in which no sound is produced after the participant has started speaking. This is the total number of times "[pause]" appears in the sample. Could indicate: lexical access difficulties syntactic difficulties speech planning difficulties (Boschi et al. 2017).

#### Filled pauses

Pause in speech marked by "uhm" or a variant of this sound ("hmmm" "hum" "er" "ah" etc.). Total number of occurrences of the words "uhm" "hmmm" "hum" "uh" "er" and "ah" in the sample. Could indicate: lexical access difficulties syntactic difficulties discourse planning difficulties (Boschi et al. 2017).

#### Word, word group or idea repetitions

Words or content information that are present more than once in the sample (repetitions directly glued on top of each other or further apart in the sample). Total number of words, groups of words (combinations of 2 to 6 words) or content information present more than once in the sample. Could indicate: lexico-semantic deficits discourse planning difficulties (Boschi et al. 2017).

### Variable names

{{ read_csv("speech-production.csv") }}