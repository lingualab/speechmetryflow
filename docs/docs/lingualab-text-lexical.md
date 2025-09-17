# Caractéristiques lexicales

## Parts-of-Speech

Classe grammaticale d’un mot. La catégorisation en parties du discours (Parts-of-Speech ou POS) se réfère à la classification des mots selon leur fonction grammaticale dans une phrase. Cela inclut la détermination de la classe à laquelle appartient chaque mot telles que les noms les pronoms les verbes les adverbes les adjectifs les prépositions les déterminants et les conjonctions.

Nombre d’occurrences de chaque classe grammaticale (noms pronoms verbes adverbes adjectifs prépositions déterminants conjonctions) dans l’échantillon. Calculé des 2 façons suivantes : en nombre absolu et en relation au nombre total de mots dans l’échantillon.

## Mots de classe ouverte et fermée

Les "mots de classes ouvertes" et les "mots de classes fermées" sont deux catégories principales dans la classification des mots selon leur rôle dans la langue. Nombre total de mots de classe ouverte (noms verbes adjectifs adverbes) et de classe fermée (conjonctions pronoms déterminants prépositions) dans l’échantillon.

### Mots de Classes Ouvertes

Ces mots constituent le contenu principal du discours. Ils sont appelés "ouverts" car de nouveaux mots peuvent être régulièrement ajoutés à ces catégories.

Ces mots incluent :

- Noms : Représentent des personnes lieux objets idées (ex. : pomme liberté).
- Verbes : Désignent des actions des états des occurrences (ex. : courir être).
- Adjectifs : Qualifient ou quantifient les noms (ex. : rapide grand).
- Adverbes : Modifient des verbes des adjectifs ou d'autres adverbes (ex. : rapidement très).

### Mots de Classes Fermées

Ces mots remplissent une fonction grammaticale plutôt que de transmettre un contenu concret. Ils forment un ensemble relativement fixe et limité de termes.

Ces mots incluent :
- Conjonctions : Relient des mots phrases ou clauses (ex. : et mais).
- Pronoms : Remplacent les noms (ex. : elle celui).
- Déterminants : Précisent les noms (ex. : le un).
- Prépositions : Relient un nom à un autre élément de la phrase (ex. : dans sur).

### Exemple

Voici les étapes générales pour compter les mots de classes ouvertes et fermées en Python en utilisant NLTK :

- Télécharger les Ressources Nécessaires : Utilisez `nltk.download('punkt')` et `nltk.download('averaged_perceptron_tagger')`.
- Tokeniser le Texte et Appliquer le POS Tagging : Utilisez word_tokenize pour diviser le texte en mots et pos_tag pour appliquer le POS tagging à chaque mot.
- Comptage des Mots : Comptez les occurrences de mots appartenant à des classes ouvertes (noms verbes adjectifs adverbes) et fermées (conjonctions pronoms déterminants prépositions) et calculez ces nombres en termes absolus.

## Ratio de différentes Parts-of-Speech et types de mots

Proportion de mots de différentes classes grammaticales ou de différents types de mots sur le nombre total de mots dans l’échantillon ou sur le nombre total de mots d’une ou plusieurs autre(s) classe(s) grammaticale(s). 

Nombre total d’occurrences d’une classe grammaticale dans l’échantillon divisé par le nombre total de mots dans l’échantillon ou par le nombre d’occurrences d’une ou plusieurs autre(s) classe(s) grammaticale(s).

Les ratios suivants seront calculés : 

- Pronoms/Noms + Pronoms 
- Noms/Noms + Pronoms 
- Noms/Noms + Verbes
- Verbes/Noms + Verbes
- Verbes avec inflexions/Nombre total de verbes
- Nombre de mots de classe ouverte/Nombre total de mots
- Nombre de mots de classe fermée/Nombre total de mots
- Gérondifs/Nombre total de verbes
- Gérondifs/Nombre total de mots

## Verbes légers

Un verbe léger est un terme linguistique désignant un verbe qui pris isolément possède un contenu sémantique limité ou générique mais qui lorsqu'il est combiné avec d'autres mots (comme des noms des adjectifs ou des prépositions) contribue à créer une expression verbale avec un sens plus riche ou spécifique. Ces verbes souvent courants et polyvalents comme "faire" "mettre" "prendre" acquièrent une signification plus nuancée et spécifique dans le contexte de leur combinaison avec d'autres éléments linguistiques. 

Nombre d’occurrences des verbes suivants (à l’infinitif ou conjugués) dans l’échantillon : be, have, come, go, give, take, make, do, get, move, put.

Calculé des deux façons suivantes:
- en nombre absolu
- en relation au nombre total de verbes dans l’échantillon

## Pronoms déictiques

Pronoms utilisés pour faire référence directement aux caractéristiques personnelles temporelles ou de localisation de l’image à décrire. La signification spécifique de ces pronoms dépend du contexte dans lequel ils sont utilisés (Crystal 2011).

Nombre total d’occurrences des mots des quatre catégories suivantes dans l’échantillon:

- Deixis spatiale : this, that, here, there.
- Deixis personnelle : he, she, her, herself, him, himself.
- Deixis temporelle : then, now, soon, recently.
- Pronoms déictiques : somme des pronoms déictiques des trois catégories précédentes.

Calculé des 2 façons suivantes :
- en nombre absolu
- en relation au nombre total de mots dans l’échantillon

## Termes indéfinis

Les "termes indéfinis" dans un contexte linguistique sont des mots utilisés pour faire référence à des objets des personnes ou des quantités de manière vague ou non spécifique sans désigner un élément précis. Ils sont souvent employés pour parler de choses de manière générale ou pour indiquer une quantité indéterminée.

Exemples:

- Objets ou Choses Générales : thing, stuff".
- Indéfinis Quantitatifs : little, much, few, many, several".
- Indéfinis de Personnes : anyone, everyone, no one, someone, everybody, nobody.
- Autres Indéfinis : another, the other, each, either, neither, both, other, others.

- Objets ou Choses Générales : truc, chose.
- Indéfinis Quantitatifs : peu, beaucoup, quelques, plusieurs.
- Indéfinis de Personnes : quelqu'un, tout le monde, personne, chacun, n'importe qui.
- Autres Indéfinis : autre, l'autre, chaque, ni l'un ni l'autre, les deux, d'autres.

Nombre total d’occurrences des termes suivants dans l’échantillon, calculé des 2 façons suivantes :

- en nombre absolu
- en relation au nombre total de mots dans l’échantillon

## Moving Average Type-Token Ratio (MATTR)

Le Moving-Average Type-Token Ratio (MATTR) est une mesure en linguistique qui calcule la moyenne mobile pour tous les segments d'une longueur donnée dans un texte. Pour un segment de 50 mots par exemple le Type-Token Ratio (TTR) est calculé sur les mots 1-50 2-51 3-52 etc... et les mesures de TTR résultantes sont moyennées pour produire la valeur finale de MATTR. Cette approche permet d'obtenir une mesure plus stable et représentative de la diversité lexicale d'un texte car elle minimise l'impact de la longueur du texte sur le TTR​​.

Calculé en déplaçant une fenêtre de grandeur `x` à travers le texte. Pour chaque fenêtre un Type-Token Ratio est obtenu en divisant le nombre de mots uniques par le nombre total de mots dans la fenêtre. Pour obtenir le MATTR global d’un échantillon la moyenne des TTR de chaque fenêtre est calculée. La longueur de chaque fenêtre sera déterminée en calculant le nombre de mots moyen dans tous les échantillons de DS.

Trois groupes de fenêtre seront donc obtenus de façon à ce que chaque fenêtre contienne 10 25 et 40 mots (Covington & McFall 2010).

Un MATTR plus élevé indique une plus grande diversité lexicale (Covington & McFall 2010)

[https://pypi.org/project/taaled/#:~:text=The Moving15](https://pypi.org/project/taaled/#:~:text=The%20Moving15)

## Statistique R de Honoré

La statistique R de Honoré est une mesure de la diversité lexicale qui prend en compte la longueur de l’échantillon le nombre de mots différents utilisés et le nombre de mots mentionnés une seule fois.

Elle est calculée selon la formule : `R=100×log(N)/(1−(V1/V))`

- N est le nombre total de mots dans l'échantillon.
- V est le nombre de mots différents dans l'échantillon.
- V1 est le nombre de mots mentionnés une seule fois.

Cette mesure est particulièrement utile pour analyser des textes plus longs car elle réduit la sensibilité de la mesure de diversité lexicale à la longueur du texte.

Une statistique d’Honoré plus élevée indique une plus grande diversité lexicale.

Pour opérationnaliser et calculer la statistique R de Honoré en Python vous devez d'abord tokeniser votre texte pour obtenir le nombre total de mots (N) compter le nombre de mots uniques (V) et identifier ceux qui n'apparaissent qu'une seule fois (V1). Ensuite vous pouvez appliquer la formule ci-dessus pour obtenir la valeur de R.

## Index W de Brunet

Mesure de diversité lexicale reliant la longueur de l’échantillon au nombre de mots différents utilisés dans celui-ci.

La formule de cet indice est : `W = N ^ (V ^ (-0.165))`

- W est l'indice W de Brunet.
- N est le nombre total de mots dans le texte (aussi connu sous le nom de compte de tokens).
- V est le nombre total de mots uniques (aussi connu sous le nom de compte de types).

Un index W de Brunet plus élevé indique une moins grande diversité lexicale (échelle inversée). Relativement peu affecté par les variations dans la longueur de l’échantillon.

## Familiarité

Degré avec lequel un mot est familier pour les locuteurs d’une langue. Évaluations subjectives de la familiarité obtenues des normes de Glasgow (Scott et al. 2019).

La familiarité moyenne sera calculée pour tous les : mots, noms, verbes et adjectifs de l’échantillon.

Des déficits sémantiques et/ou d’accès lexical pourraient se manifester par une utilisation accrue de mots évalués comme étant très familiers (Fraser et al. 2016).

## Imageabilité

Niveau d’effort impliqué dans la génération d’une image mentale du concept représenté par un mot. Évaluations subjectives de l’imageabilité obtenues des normes de Glasgow (Scott et al. 2019).

L’imageabilité moyenne sera calculée pour tous les : mots, noms, verbes et adjectifs de l’échantillon.

Les "Glasgow Norms" sont un ensemble de notations normatives pour 5 553 mots anglais évalués sur neuf dimensions psycholinguistiques : l'excitation (arousal), la valence, la dominance, la concrétude, l'imageabilité, la familiarité, l'âge d'acquisition, la taille sémantique, et l'association de genre. Ce corpus est unique en plusieurs aspects. Il est relativement large et fournit des normes sur un grand nombre de dimensions lexicales. Pour chaque sous-ensemble de mots les mêmes participants ont fourni des évaluations sur toutes les neuf dimensions. De plus le corpus contient un ensemble de 379 mots ambigus présentés seuls ou avec des informations sélectionnant un autre sens. Les relations entre les dimensions des Glasgow Norms ont été initialement étudiées en évaluant leurs corrélations. Une analyse en composantes principales a révélé quatre facteurs principaux représentant 82 % de la variance. La validité des Glasgow Norms a été établie par des comparaisons avec 18 ensembles différents de normes psycholinguistiques actuelles. Les Glasgow Norms offrent une ressource précieuse en particulier pour les chercheurs étudiant le rôle de la reconnaissance des mots dans la compréhension du langage.

[https://pubmed.ncbi.nlm.nih.gov/30206797/](https://pubmed.ncbi.nlm.nih.gov/30206797/)

## Concrétude

Degré avec lequel le concept dénoté par un mot fait référence à une entité perceptible/tangible. Évaluations subjectives de la concrétude de Brysbaert et al. 2014.

La concrétude moyenne sera calculée pour tous les : mots, noms, verbes et adjectifs de l’échantillon.

Les évaluations du caractère concret sont présentées pour 37 058 mots anglais et 2 896 expressions de deux mots (telles que passage piéton et zoom avant) obtenues auprès de plus de 4 000 participants au moyen d'une étude de normalisation utilisant le crowdsourcing sur Internet pour la collecte de données. Bien que les instructions soulignent que l'évaluation du caractère concret des mots serait basée sur des expériences impliquant tous les sens et réponses motrices une comparaison avec les normes de caractère concret existantes indique que les participants comme auparavant se sont largement concentrés sur les expériences visuelles et haptiques. L'ensemble de données rapporté est un sous-ensemble d'une liste complète de lemmes anglais et contient tous les lemmes connus par au moins 85 % des évaluateurs. Il peut être utilisé dans des recherches futures comme liste de référence de lemmes anglais généralement connus.

[https://pubmed.ncbi.nlm.nih.gov/24142837/](https://pubmed.ncbi.nlm.nih.gov/24142837/)

## Fréquence des mots dans le langage courant

Évaluation de la fréquence avec laquelle un mot est utilisé dans le langage courant par les locuteurs d’une langue. Mesure objective de la fréquence des mots tirées du corpus SUBTLEX-US (Brysbaert & New 2009).

La fréquence moyenne sera calculée pour tous les: mots, noms, verbes et adjectifs de l’échantillon.

La base de données SUBTLEX-US contient les fréquences de mots basées sur les sous-titres de films comme développé par Brysbaert et New en 2009. Cette base de données offre une mesure objective de la fréquence des mots en anglais américain tirée d'un large corpus de sous-titres. Elle inclut également des informations sur les parties du discours (PoS) et utilise l'échelle de fréquence de mots de Zipf. Cette approche fournit des données plus représentatives de l'utilisation des mots dans la langue parlée courante comparée aux fréquences basées sur des textes écrits ou littéraires. Elle est donc particulièrement utile pour la recherche en psycholinguistique et en traitement automatique des langues.

Les difficultés à accéder à des mots spécifiques résultent généralement en une sur-utilisation de mots avec une fréquence élevée (Wang et al. 2021). [https://osf.io/djpqz/](https://osf.io/djpqz/)

## Valence

Degré d’agréabilité des émotions invoquées par un mot. Évaluations subjectives de la valence de Warriner et al. 2013.

La valence moyenne sera calculée pour tous les: mots, noms, verbes et adjectifs de l’échantillon.

L'étude de Warriner et al. de 2013 a impliqué l'évaluation subjective de la valence de l'excitation et de la dominance pour 13 915 lemmes en anglais. Cette recherche a été réalisée par un groupe de 1 827 participants qui ont évalué la valence émotionnelle de ces mots dans une étude de notation en ligne, [https://www.frontiersin.org/journals/communication/articles/10.3389/fcomm.2021.770497/full](https://www.frontiersin.org/journals/communication/articles/10.3389/fcomm.2021.770497/full).

La valence dans ce contexte se réfère à la qualité affective d'un mot indiquant s'il évoque des sentiments positifs ou négatifs. Les chercheurs ont trouvé une corrélation forte entre la valence et la dominance suggérant que les stimuli ne pourraient pas être facilement identifiés comme variant en valence tout en restant constants en dominance, [https://www.sciencedirect.com/science/article/pii/S0001691821001098](https://www.sciencedirect.com/science/article/pii/S0001691821001098). Les résultats ont montré que l'écart-type moyen des évaluations de valence était de 168 tandis que celui des évaluations d'excitation pour les mêmes mots était de 230 indiquant une plus grande variabilité dans les évaluations d'excitation que de valence, [https://www.sciencedirect.com/science/article/pii/S0346251X19302039](https://www.sciencedirect.com/science/article/pii/S0346251X19302039).

Ces normes de valence d'excitation et de dominance pour les mots anglais sont utilisées par les chercheurs travaillant sur les émotions et les humeurs la reconnaissance et la mémoire des mots ainsi que l'analyse du sentiment basée sur le texte, [https://pubmed.ncbi.nlm.nih.gov/23404613/](https://pubmed.ncbi.nlm.nih.gov/23404613/). La recherche de Warriner et al. contribue ainsi de manière significative à notre compréhension de la manière dont les mots sont perçus émotionnellement et de leur impact sur divers domaines de la psycholinguistique.

## Base de données françaises

Voici les banques de données pour la langue française : [Open Lexicon FR, Les bases de données lexicales en français](http://www.lexique.org/?page_id=378)

## Noms des variables

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