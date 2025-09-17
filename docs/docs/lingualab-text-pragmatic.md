# Caractéristiques pragmatiques

## Cohérence locale

Similarité sémantique d’une phrase avec la précédente.

Le score de similarité sémantique moyen souvent calculé par la distance cosinus est une mesure courante en traitement automatique des langues (NLP) pour évaluer la proximité sémantique entre des phrases.

La distance cosinus est une mesure de similarité entre deux vecteurs dans un espace multidimensionnel qui se calcule en mesurant le cosinus de l'angle entre eux. En NLP, cette mesure est souvent utilisée pour comparer des vecteurs de mots ou de phrases où les vecteurs représentent la distribution sémantique des termes. La fonction `cosine_similarity` de la bibliothèque scikit-learn est une implémentation de cette mesure.

Des valeurs plus élevées indiquent une plus grande similarité et une moins grande distance sémantique. Des valeurs plus basses indiquent une moins grande similarité et une plus grande distance sémantique.

## Mots dénotant l’incertitude

Mots dénotant une incertitude à-propos de la nature d’un élément de l’image à décrire.

Nombre d’occurences des mots suivants dans l’échantillon : "think", "look", "like", "kind", "seem", "maybe", "can", "something".

Calculé des deux façons suivantes :

- en nombre absolu 
- en relation au nombre total de mots l’échantillon

Liste de mots inspirée par (Garrard et al., 2014), **Il faut faire une version française.**

## Difficultés à trouver les bons mots

Utilisation de mots indiquant des difficultés d’accès lexical.

Nombre d’instances des mots suivants dans l’échantillon : "know", "remember", "unable".

Calculé des deux façons suivantes :

- en nombre absolu 
- en relation au nombre total de mots l’échantillon

Liste de mots inspirée par (Garrard et al., 2014) et (Rentoumi et al., 2014), **Il faut faire une version française.**

## Connotation du discours

Émotions générées par le discours. Dépend de la valence moyenne des mots du discours. Le score de valence moyen de tous les mots de l’échantillon sera obtenu lors de l’extraction des variables psycholinguistiques. Pour chaque mot les scores possibles se situent entre 1 et 9. Un score plus élevé indique qu’un mot a une connotation davantage positive alors qu’un score plus bas indique une connotation davantage négative. 

- Si la valence moyenne est supérieure ou égale à 5, l’étiquette "connotation positive" sera donnée au discours.
- Si la valence moyenne est supérieure ou égale à 4 et inférieure à 5, l’étiquette "connotation neutre" sera donnée au discours.
- Si la valence moyenne est inférieure à 4, l’étiquette "connotation négative" sera donnée au discours.

## Expressions formulaiques

Expressions ayant une forme fixe et une signification non-littérale avec des nuances attitudinales.

Nombre total d’occurrences des expressions formulaiques suivantes dans l’échantillon : "well", "so", "I guess", "you know", "as it is", "as it were". (Van Lancker Sidtis et al. 2015)

Calculé des deux façons suivantes : 

- en nombre absolu 
- en relation au nombre total de mots l’échantillon

## Modalisations

Opinions d’un individu concernant le contenu de sa description (ou ce qui se passe sur l’image à décrire) incluant les doutes et les inquiétudes par rapport à sa production.

Nombre total d’occurrences des expressions suivantes dans l’échantillon : "I think", "In my opinion", "of course", "naturally", "unsure", "likely", "could be that", "unfortunately", "surely". (Boschi et al. 2017, Boyé et al. 2014)

Calculé des deux façons suivantes : 

- en nombre absolu 
- en relation au nombre total de mots l’échantillon

## Mots de remplissage

Mots ou groupes de mots utilisés pour mettre l’accent sur ce qui sera dit ou a été dit ou qui signalent qu’un individu réfléchi à ce qu’il dira ensuite.

Nombre total de fois où les expressions "you know", "I mean" sont mentionnées dans l’échantillon.

Calculé des deux façons suivantes : 

- en nombre absolu 
- en relation au nombre total de mots l’échantillon

Pourraient donner de l’information sur la capacité d’accès lexical d’un individu.

*Note*: Ce tableau se veut une version modifiée de celui qui est retrouvé dans [Slegers et al. 2021](https://papyrus.bib.umontreal.ca/xmlui/bitstream/handle/1866/26432/Slegers_Antoine_2021_these.pdf?sequence=2) et de Pellerin Sophie.

## Noms des variables

- `Coherence_locale`
- `Sentiment-valence`
- `Emotion`
- `Nombre_de_mots_incertitude`
- `Frequence_relative_mots_incertitude`
- `Nombre_de_mots_difficulte_acces_lexical`
- `Frequence_relative_mots_difficulte_acces_lexical`
- `Nombre_de_mots_expression_formulaiques`
- `Frequence_relative_mots_expression_formulaiques`
- `Nombre_de_mots_modalisations`
- `Frequence_relative_mots_modalisations`
- `Nombre_de_mots_de_remplissage`
- `Frequence_relative_mots_de_remplissage`