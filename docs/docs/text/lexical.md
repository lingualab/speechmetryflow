# Lexical features

## Parts-of-Speech

Grammatical class of a word. Parts-of-Speech (POS) categorization refers to the classification of words according to their grammatical function in a sentence. This includes determining the class to which each word belongs, such as nouns pronouns verbs adverbs adjectives prepositions determiners and conjunctions.

Number of occurrences of each grammatical class (nouns pronouns verbs adverbs adjectives prepositions determiners conjunctions) in the sample. Calculated in 2 ways: as an absolute number and in relation to the total number of words in the sample.

## Open and closed class words

Open-class words" and "closed-class words" are two main categories in the classification of words according to their role in the language. Total number of open-class words (nouns verbs adjectives adverbs) and closed-class words (conjunctions pronouns determiners prepositions) in the sample.

### Open Class Words

These words are the main content of the speech. They are called "open" because new words can be regularly added to these categories.

These words include :

- Nouns: Represent people places objects ideas (e.g. apple freedom).
- Verbs: Designate actions, states and occurrences (e.g.: run, be).
- Adjectives: Qualify or quantify nouns (e.g.: fast big).
- Adverbs: Modify verbs, adjectives or other adverbs (e.g.: quickly very).

### Closed Class Words

These words have a grammatical function rather than conveying concrete content. They form a relatively fixed and limited set of terms.

These words include :
- Conjunctions: connect words with phrases or clauses (e.g. and but).
- Pronouns: Replace nouns (e.g.: she the one).
- Determiners: Specify nouns (e.g.: the one).
- Prepositions: Link a noun to another element of the sentence (e.g. in on).

### Example

Here are the general steps for counting words in open and closed classes in Python using NLTK :

- Download Necessary Resources: Use `nltk.download('punkt')` and `nltk.download('averaged_perceptron_tagger')`.
- Tokenize text and apply POS tagging: Use word_tokenize to divide text into words and pos_tag to apply POS tagging to each word.
- Word Count: Count occurrences of words belonging to open (nouns verbs adjectives adverbs) and closed (conjunctions pronouns determiners prepositions) classes and calculate these numbers in absolute terms.

## Ratio of different Parts-of-Speech and word types

Ratio of words of different grammatical classes or word types to the total number of words in the sample or to the total number of words of one or more other grammatical class(es). 

Total number of occurrences of a grammatical class in the sample divided by the total number of words in the sample or by the number of occurrences of one or more other grammatical class(es).

The following ratios will be calculated: 

- Pronouns/Nouns + Pronouns 
- Nouns/Noms + Pronouns 
- Nouns/Noms + Verbs
- Verbs/Nouns + Verbs
- Verbs with inflections/Total number of verbs
- Number of open class words/Total number of words
- Number of closed words/Total number of words
- Gerunds/Total number of verbs
- Gerunds/Total number of words

## Light verbs

A light verb is a linguistic term for a verb that, taken on its own, has a limited or generic semantic content, but when combined with other words (such as nouns, adjectives or prepositions) helps create a verbal expression with a richer or more specific meaning. These often common and versatile verbs like "to do" "to put" "to take" acquire a more nuanced and specific meaning in the context of their combination with other linguistic elements. 

Number of occurrences of the following verbs (infinitive or conjugated) in the sample: be, have, come, go, give, take, make, do, get, move, put.

Calculated in two ways:
- in absolute numbers
- in relation to the total number of verbs in the sample

## Deictic pronouns

Pronouns used to refer directly to personal temporal or local characteristics of the image to be described. The specific meaning of these pronouns depends on the context in which they are used (Crystal 2011).

Total number of occurrences of words in the following four categories in the sample:

- Spatial deixis: this, that, here, there.
- Personal deixis: he, she, her, herself, him, himself.
- Temporal deixis: then, now, soon, recently.
- Deictic pronouns: sum of deictic pronouns from the three preceding categories.

Calculated in 2 ways:
- in absolute number
- in relation to the total number of words in the sample

## Indefinite terms

In a linguistic context, "indefinite terms" are words used to refer to objects, people or quantities in a vague or non-specific way, without designating a precise element. They are often used to talk about things in a general way or to indicate an indeterminate quantity.

Examples:

- General objects or things: thing, stuff.
- Quantitative indefinites: little, much, few, many, several.
- Person indefinites: anyone, everyone, no one, someone, everybody, nobody.
- Other Indefinites: another, the other, each, either, neither, both, other, others.

- General objects or things: thing, thing.
- Quantitative Indefinites: little, much, some, many.
- Person indefinites: someone, everyone, nobody, everyone, anyone.
- Other Indefinites: other, the other, each, neither, both, others.

Total number of occurrences of the following terms in the sample, calculated in 2 ways:

- as an absolute number
- in relation to the total number of words in the sample

## Moving Average Type-Token Ratio (MATTR)

The Moving-Average Type-Token Ratio (MATTR) is a linguistic measure that calculates the moving average for all segments of a given length in a text. For a 50-word segment, for example, the Type-Token Ratio (TTR) is calculated for words 1-50 2-51 3-52 etc., and the resulting TTR measurements are averaged to produce the final MATTR value. This approach provides a more stable and representative measure of the lexical diversity of a text, as it minimizes the impact of text length on TTR.

Calculated by moving a window of size `x` across the text. For each window, a Type-Token Ratio is obtained by dividing the number of unique words by the total number of words in the window. To obtain the overall MATTR of a sample, the TTR of each window is averaged. The length of each window is determined by calculating the average number of words in all DS samples.

Three window groups will therefore be obtained so that each window contains 10 25 and 40 words (Covington & McFall 2010).

A higher MATTR indicates greater lexical diversity (Covington & McFall 2010).

[https://pypi.org/project/taaled/#:~:text=The Moving15](https://pypi.org/project/taaled/#:~:text=The%20Moving15)

## Honoré's R statistic

Honoré's R statistic is a measure of lexical diversity that takes into account sample length, the number of different words used and the number of words mentioned only once.

It is calculated according to the formula: `R=100×log(N)/(1-(V1/V))`.

- N is the total number of words in the sample.
- V is the number of different words in the sample.
- V1 is the number of words mentioned only once.

This measure is particularly useful for analyzing longer texts, as it reduces the sensitivity of the lexical diversity measure to text length.

A higher Honoré statistic indicates greater lexical diversity.

To operationalize and calculate the Honoré R statistic in Python you first need to tokenize your text to obtain the total number of words (N) count the number of unique words (V) and identify those that appear only once (V1). Then you can apply the above formula to obtain the value of R.

## Brunet's W index

A measure of lexical diversity relating sample length to the number of different words used in the sample.

The formula for this index is: `W = N ^ (V ^ (-0.165))`

- W is Brunet's W index.
- N is the total number of words in the text (also known as the token count).
- V is the total number of unique words (also known as the type count).

A higher Brunet W index indicates less lexical diversity (inverted scale). Relatively unaffected by variations in sample length.

## Familiarity

Degree to which a word is familiar to speakers of a language. Subjective familiarity ratings obtained from Glasgow norms (Scott et al. 2019).

Average familiarity will be calculated for all: words, nouns, verbs and adjectives in the sample.

Semantic and/or lexical access deficits could be manifested by increased use of words rated as highly familiar (Fraser et al. 2016).

## Imageability

Level of effort involved in generating a mental image of the concept represented by a word. Subjective ratings of imageability obtained from Glasgow norms (Scott et al. 2019).

Average imageability will be calculated for all: words, nouns, verbs and adjectives in the sample.

The "Glasgow Norms" are a set of normative ratings for 5,553 English words evaluated on nine psycholinguistic dimensions: arousal, valence, dominance, concreteness, imageability, familiarity, age of acquisition, semantic size, and gender association. This corpus is unique in several respects. It is relatively large and provides norms on a large number of lexical dimensions. For each subset of words, the same participants provided ratings on all nine dimensions. In addition, the corpus contains a set of 379 ambiguous words presented alone or with information selecting another meaning. The relationships between the Glasgow Norms dimensions were initially investigated by assessing their correlations. Principal component analysis revealed four main factors accounting for 82% of the variance. The validity of the Glasgow Norms was established through comparisons with 18 different sets of current psycholinguistic norms. The Glasgow Norms offer a valuable resource particularly for researchers investigating the role of word recognition in language comprehension.

[https://pubmed.ncbi.nlm.nih.gov/30206797/](https://pubmed.ncbi.nlm.nih.gov/30206797/)

## Concreteness

Degree to which the concept denoted by a word refers to a perceptible/tangible entity. Subjective assessments of concreteness from Brysbaert et al. 2014.

Average concreteness will be calculated for all: words, nouns, verbs and adjectives in the sample.

Concreteness ratings are presented for 37,058 English words and 2,896 two-word phrases (such as crosswalk and zoom in) obtained from over 4,000 participants through a standardization study using Internet crowdsourcing for data collection. Although the instructions stress that the assessment of word concreteness would be based on experiences involving all senses and motor responses a comparison with existing concreteness norms indicates that participants as before focused largely on visual and haptic experiences. The reported dataset is a subset of a complete list of English lemmas and contains all lemmas known to at least 85% of raters. It can be used in future research as a reference list of generally known English lemmas.

[https://pubmed.ncbi.nlm.nih.gov/24142837/](https://pubmed.ncbi.nlm.nih.gov/24142837/)

## Word frequency in everyday language

Evaluation of the frequency with which a word is used in everyday speech by speakers of a language. Objective measurement of word frequency from the SUBTLEX-US corpus (Brysbaert & New 2009).

The average frequency will be calculated for all: words, nouns, verbs and adjectives in the sample.

The SUBTLEX-US database contains word frequencies based on film subtitles as developed by Brysbaert and New in 2009. This database offers an objective measure of word frequency in American English drawn from a large corpus of subtitles. It also includes information on parts of speech (PoS) and uses Zipf's word frequency scale. This approach provides more representative data on word usage in everyday spoken language than frequencies based on written or literary texts. It is therefore particularly useful for research in psycholinguistics and automatic language processing.

Difficulties in accessing specific words generally result in the overuse of words with a high frequency (Wang et al. 2021). [https://osf.io/djpqz/](https://osf.io/djpqz/)

## Valence

Degree of agreeableness of emotions invoked by a word. Subjective valence assessments from Warriner et al. 2013.

Average valence will be calculated for all: words, nouns, verbs and adjectives in the sample.

The 2013 Warriner et al. study involved subjective valence ratings of arousal and dominance for 13,915 English lemmas. This research involved a group of 1,827 participants rating the emotional valence of these words in an online scoring study, [https://www.frontiersin.org/journals/communication/articles/10.3389/fcomm.2021.770497/full](https://www.frontiersin.org/journals/communication/articles/10.3389/fcomm.2021.770497/full).

Valence in this context refers to the affective quality of a word indicating whether it evokes positive or negative feelings. The researchers found a strong correlation between valence and dominance suggesting that stimuli could not easily be identified as varying in valence while remaining constant in dominance, [https://www.sciencedirect.com/science/article/pii/S0001691821001098](https://www.sciencedirect.com/science/article/pii/S0001691821001098). The results showed that the mean standard deviation of valence ratings was 168 while that of arousal ratings for the same words was 230 indicating greater variability in arousal than valence ratings, [https://www.sciencedirect.com/science/article/pii/S0346251X19302039](https://www.sciencedirect.com/science/article/pii/S0346251X19302039).

These norms of arousal valence and dominance for English words are used by researchers working on emotions and moods word recognition and memory as well as text-based sentiment analysis, [https://pubmed.ncbi.nlm.nih.gov/23404613/](https://pubmed.ncbi.nlm.nih.gov/23404613/). Warriner et al.'s research thus makes a significant contribution to our understanding of how words are emotionally perceived and their impact on various areas of psycholinguistics.

## French databases

Here are the databases for the French language: [Open Lexicon FR, Les bases de données lexicales en français](http://www.lexique.org/?page_id=378)

## Variable names

- `Mots_de_classe_ouverte`
- `Mots_de_classe_fermee`
- `Nombre_de_gerondifs`
- `Pronoms/(Noms+Pronoms)`
- `Noms/(Noms+Pronoms)`
- `Noms/(Noms+Verbes)`
- `Verbes/(Noms+Verbes)`
- `Verbes_avec_inflexions/Total_Verbes`
- `Mots_de_classe_ouverte/Total_Mots`
- `Mots_de_classe_fermee/Total_Mots`
- `Gerondifs/Total_Verbes`
- `Gerondifs/Total_Mots`
- `Nombre_de_pronoms_deictiques`
- `Nombre_de_pronoms_deictiques_spatiaux`
- `Nombre_de_pronoms_deictiques_personnels`
- `Nombre_de_pronoms_deictiques_temporels`
- `Nombre_de_termes_indefinis`
- `Ratio_termes_indefinis`
- `MATTR_10`
- `MATTR_25`
- `MATTR_40`
- `Nombre_de_mots_uniques`
- `Statistique_R_de_Honore`
- `Familiarite_moyenne_mots`
- `Familiarite_moyenne_noms`
- `Familiarite_moyenne_verbes`
- `Familiarite_moyenne_adjectifs`
- `Imageabilite_moyenne_mots`
- `Imageabilite_moyenne_noms`
- `Imageabilite_moyenne_verbes`
- `Imageabilite_moyenne_adjectifs`
- `Concretude_moyenne_mots`
- `Concretude_moyenne_noms`
- `Concretude_moyenne_verbes`
- `Concretude_moyenne_adjectifs`
- `Frequence_moyenne_mots`
- `Frequence_moyenne_noms`
- `Frequence_moyenne_verbes`
- `Frequence_moyenne_adjectifs`
- `Valence_moyenne_mots`
- `Valence_moyenne_noms`
- `Valence_moyenne_verbes`
- `Valence_moyenne_adjectifs`
- `Brunet_W_indice`