# Syntactic features

## Universal syntactic dependencies

Universal syntactic dependencies are a set of rules that model grammatical relationships in languages. They are characterized by a hierarchical structure in which words are connected according to their syntactic function in a sentence. These rules are called "universal" because they are intended to be applicable across different languages, providing a common framework for linguistic analysis.

The directional dependency relation is a specification of dependency grammar that establishes a connection between a syntactic unit (e.g. a verb) and the entities that make up its relational structure (such as subjects and objects). In a dependency tree, which is a graphical representation of these relationships, the words or morphemes are the nodes and the dependency relationships are the edges, often annotated with syntactic functions such as subject object, etc. [https://fr.wikipedia.org/wiki/Grammaire_de_dépendance](https://fr.wikipedia.org/wiki/Grammaire_de_d%C3%A9pendance) 

Total number of each syntactic dependency: This means counting how many times each type of dependency relation (such as subject, object, complement, etc.) appears in a text.

Calculation with spaCy dependencies (DEP): spaCy is able to analyze a sentence and identify these dependency relationships. Each word in a sentence is associated with a DEP tag that describes its syntactic role.

Two calculation methods:
- In absolute number: Count the total number of times a specific syntactic dependency appears.
- In relation to the total number of words: Calculate the frequency of each syntactic dependency in relation to the total number of words in the sample, giving a relative measure.

### Example

To illustrate the directional dependency relationship in syntax, let's consider the simple sentence: "The cat eats a mouse."

In a dependency tree for this sentence :

- "eats" would be the root because it's the verb, the main action of the sentence.
- "The cat" would be an actant, more precisely the subject of the verb "eats". There would therefore be a directional arrow starting from "mange" and pointing towards "chat", indicating that "chat" is the subject of "mange".
- A mouse" would be another actant, the direct object of the verb "mange". Similarly, a directional arrow would run from "mange" to "souris" to indicate this relationship.

In this tree, each word is connected by lines (or edges) that show how each word depends on the verb (or other words) for its syntactic function in the sentence.

### References

- [Universal Dependencies](https://universaldependencies.org/)
- [https://spacy.io/usage/linguistic-features#dependency-parse](https://spacy.io/usage/linguistic-features#dependency-parse)

## Length of syntax dependencies

Average and maximum length of syntactic dependencies. Average and maximum number of words in a sample's syntactic dependencies.

## Left and right children

Direct dependents of a word that are connected to it by a single arc to its left or right in the dependency tree.

We measure the average number of left and right children for each word in a sample of texts. This helps us to understand the syntactic structure of the sentences in this sample.

Calculated using spaCy commands `n_left` and `n_right` in two ways:

- as an absolute number
- in relation to the total number of words in the sample

[https://spacy.io/usage/linguistic-features#navigating](https://spacy.io/usage/linguistic-features#navigating) |

## Verbs with inflections (conjugated verbs)

Verbs in the sample that do not match their lemma as extracted by spaCy.

Calculated in two ways:

- in absolute number
- in relation to the total number of words in the sample

## Subordinate clauses

Group of words that does not express a complete thought, does not constitute a complete sentence. Complex clauses involving subordination occur when a syntactic dependent (main or not) is used as a causal structure.

Total number of the 4 basic universal dependency types calculated using spaCy's default dependency parse:

- Clausal subjects (csubj)
- Clausal complements divided into those whose subject must be checked (subject outside the clause; `xcomp`) and those whose subject is not checked (subject inside the clause; `ccomp`).
- Adverbial clause modifiers (`advcl`)
- Adnominal clause modifiers (`acl`)

Calculated in two ways:

- as an absolute number 
- in relation to the total number of words in the sample

[https://universaldependencies.org/u/overview/complex-syntax.html](https://universaldependencies.org/u/overview/complex-syntax.html)

## Average sentence length

Average number of words per sentence. The average number of words per sentence in the sample will be calculated. Sentence boundaries will be determined by spaCy's default "dependency parse".

[https://spacy.io/usage/linguistic-features#sbd](https://spacy.io/usage/linguistic-features#sbd)

## Incomplete sentences

Phrases that do not contain a minimum of one verb and its subject. Total number of sentences in the sample that contain no verb with its subject.

Calculated in two ways:

- in absolute numbers 
- in relation to the total number of words in the sample

Could indicate: lexical-semantic deficits, syntactic deficits, difficulties with discourse planning (Boschi et al. 2017).

## Number of prepositional phrases

Sentences that contain a preposition its object (noun or pronoun) and any object modifier, (Boschi et al. 2017).

Calculated in the following two ways:

- in absolute number 
- in relation to the total number of words in the sample

## Number of verbal phrases

Basic sentences containing at least one verb and its dependents. Calculated using basic spaCy implementations.

Calculated in two ways:

- absolute number 
- in relation to the total number of words in the sample

## Length and number of noun phrases

A nominal phrase is a group of words centered around a noun (substantive) that functions as the subject, object or complement in a sentence. For example, in the sentence "The black cat sleeps on the carpet", "The black cat" is a noun phrase.

The length of a nominal phrase is the number of words that make it up. It can vary from two words like "A house" to a longer sequence like "The big house by the road".

Total number and average length of noun phrases in the sample. Calculated using basic spaCy implementations.

Calculated in two ways:

- absolute number 
- in relation to the total number of words in the sample

[https://spacy.io/usage/linguistic-features#noun-chunks](https://spacy.io/usage/linguistic-features#noun-chunks)

## Verb tenses used

Forms verbs take to indicate when the action takes place in time. Total number of verbs conjugated in the present, past and future tenses in the sample.

Calculated in two ways:

- in absolute numbers 
- in relation to the total number of words in the sample

## Clauses per sentence

Groups of words comprising a subject and a verb normally used to add further details about a noun in a sentence. Average number of clauses per sentence calculated using basic spaCy implementations.

## Proportion of nouns with determiners

Proportion of names for which a determiner is present. Number of names in the sample attached to a determiner out of the total number of names in the sample. Calculated using spaCy's dependency parse.

## Coordinated phrases

Phrases linked by one or more coordinating conjunctions. Total number of sentences in the sample containing the following coordinating conjunctions: "and", "but", "for", "nor", "or", "yet", "so" (Boschi et al. 2017).

Calculated in the following two ways:

- in absolute numbers 
- in relation to the total number of words in the sample

## Variable names

- `Longueur_moyenne_des_dependances`
- `Longueur_maximale_des_dependances`
- `Moyenne_enfants_gauches`
- `Moyenne_enfants_droits`
- `Total_enfants_gauches`
- `Total_enfants_droits`
- `Nombre_de_verbes_inflexion`
- `Verbe_inflection_relatif`
- `Sujets_Clausaux_absolu`
- `Sujets_Clausaux_relatif`
- `Complements_Clausaux_Controles_absolu`
- `Complements_Clausaux_Controles_relatif`
- `Complements_Clausaux_Non_Controles_absolu`
- `Complements_Clausaux_Non_Controles_relatif`
- `Modificateurs_Clauses_Adverbiaux_absolu`
- `Modificateurs_Clauses_Adverbiaux_relatif`
- `Modificateurs_Clauses_Adnominaux_absolu`
- `Modificateurs_Clauses_Adnominaux_relatif`
- `Longueur_moyenne_phrases`
- `Nombre_de_phrases_incompletes_absolu`
- `Nombre_de_phrases_incompletes_relatif`
- `Nombre_de_phrases_prepositionnelles_absolu`
- `Nombre_de_phrases_prepositionnelles_relatif`
- `Nombre_de_phrases_verbales_absolu`
- `Nombre_de_phrases_verbales_relatif`
- `Nombre_absolu_phrases_nominales`
- `Longueur_moyenne_phrases_nominales`
- `Frequence_relative_phrases_nominales`
- `Nbre_verb_present_absolu`
- `Nbre_verb_present_relatif`
- `Nbre_verb_past_absolu`
- `Nbre_verb_past_relatif`
- `Nbre_verb_future_absolu`
- `Nbre_verb_future_relatif`
- `Nbre_clauses_par_phrase`
- `Proportion_noms_determinants`
- `Nombre_de_phrases_coordonnees`
- `Frequence_relative_phrases_coordonnees`
