# Semantic features

## 25 content information units (ICUs)

Separate subjects, places, objects and actions that are represented in the *Cookie Theft* image.

The list of content units (ICUs) for the Cookie Theft image test as established by Yorkston and Beukelman (1980).

The definition of ICUs can be found [here](https://github.com/lingualab/Text2Variable/blob/e24a89cf4a39db8e415245a531c2102ede15d7b1/lingua_extraction/Database_linguistique.py#L68)

## Total number of ICUs

Total number of ICUs that appear in the sample. Total number of ICUs labeled as "TRUE".

## Efficiency

Ratio of the total length of the sample to the total number of ICUs present in the sample.

## Idea density

Average semantic similarity between (conceptually distinct) ideas transmitted within a window of words moved through the text.

The average cosine distance (semantic similarity) between all pairs of word embeddings within a window moved through the text. Word embeddings will be extracted from the spaCy `en_core_web_lg` model, which supports syntactic dependency identification and Part-of-Speech tagging. Within a window, all cosine distances will be averaged. Windows of 3, 10, 25 and 40 words with an increment of half the window length will be implemented.

## Variable names

- `Nombre_ICU_TRUE`
- `Efficacite_ICU`
- TODO