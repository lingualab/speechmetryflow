# Caractéristiques syntaxiques

## Dépendances syntaxiques universelles

Les dépendances syntaxiques universelles sont un ensemble de règles qui modélisent les relations grammaticales dans les langues. Elles se caractérisent par une structure hiérarchique où les mots sont connectés selon leur fonction syntaxique dans une phrase. Ces règles sont dites "universelles" car elles visent à être applicables à travers différentes langues offrant un cadre commun pour l'analyse linguistique.

La relation de dépendance directionnelle est une spécification de la grammaire de dépendance qui établit une connexion entre une unité syntaxique (par exemple un verbe) et les entités qui composent sa structure relationnelle (comme les sujets et objets). Dans un arbre de dépendance qui est une représentation graphique de ces relations les mots ou morphèmes sont les nœuds et les relations de dépendance sont les arêtes souvent annotées par des fonctions syntaxiques telles que sujet objet etc.​​. [https://fr.wikipedia.org/wiki/Grammaire_de_dépendance](https://fr.wikipedia.org/wiki/Grammaire_de_d%C3%A9pendance) 

Nombre total de chaque dépendance syntaxique : Cela signifie compter combien de fois chaque type de relation de dépendance (comme sujet, objet, complément, etc.) apparaît dans un texte.

Calcul avec spaCy dependencies (DEP) : spaCy est capable d'analyser une phrase et d'identifier ces relations de dépendance. Chaque mot dans une phrase est associé à une étiquette DEP qui décrit son rôle syntaxique.

Deux méthodes de calcul :
- En nombre absolu : Compter le nombre total de fois qu'une dépendance syntaxique spécifique apparaît.
- En relation au nombre total de mots : Calculer la fréquence de chaque dépendance syntaxique par rapport au nombre total de mots dans l'échantillon ce qui donne une mesure relative.

### Exemple

Pour illustrer la relation de dépendance directionnelle en syntaxe considérons la phrase simple : "Le chat mange une souris."

Dans un arbre de dépendance pour cette phrase :

- "mange" serait la racine car c'est le verbe, l'action principale de la phrase.
- "Le chat" serait un actant, plus précisément le sujet du verbe "mange". Il y aurait donc une flèche directionnelle partant de "mange" et pointant vers "chat" indiquant que "chat" est le sujet de "mange".
- "une souris" serait un autre actant, l'objet direct du verbe "mange". De même une flèche directionnelle partirait de "mange" vers "souris" pour indiquer cette relation.

Dans cet arbre chaque mot est connecté par des lignes (ou arêtes) qui montrent comment chaque mot dépend du verbe (ou d'autres mots) pour sa fonction syntaxique dans la phrase.

### Références

- [Universal Dependencies](https://universaldependencies.org/)
- [https://spacy.io/usage/linguistic-features#dependency-parse](https://spacy.io/usage/linguistic-features#dependency-parse)

## Longueur des dépendances syntaxiques

Longueur moyenne et maximale des dépendances syntaxiques. Nombre moyen et maximal de mots dans les dépendances syntaxiques d’un échantillon.

## Enfants gauches et droits

Dépendants directs d’un mot qui sont connectés à celui-ci par un seul arc à sa gauche ou à sa droite dans l’arbre de dépendance.

On mesure le nombre moyen d'enfants gauches et droits pour chaque mot dans un échantillon de textes. Cette mesure nous aide à comprendre la structure syntaxique des phrases dans cet échantillon.

Calculé à l’aide des commandes spaCy `n_left` et `n_right` des deux façons suivantes :

- en nombre absolu
- en relation au nombre total de mots dans l’échantillon

[https://spacy.io/usage/linguistic-features#navigating](https://spacy.io/usage/linguistic-features#navigating) |

## Verbes avec inflexions (Verbes conjugués)

Verbes dans l’échantillon qui ne correspondent pas à leur lemma tel qu’extrait par spaCy.

Calculé des deux façons suivantes:

- en nombre absolu
- en relation au nombre total de mots dans l’échantillon

## Clauses subordonnées

Groupe de mots qui n’exprime pas une pensée complète, ne constitue pas une phrase complète. Les clauses complexes impliquant la subordination surviennent lorsqu’un dépendant syntaxique (principal ou non) est utilisé comme structure causale.

Nombre total des 4 types de dépendances universelles de base calculé à l’aide du dependency parse par défaut de spaCy:

- Sujets clausaux (csubj)
- Compléments clausaux divisés en ceux dont le sujet doit être contrôlé (sujet à l’extérieur de la clause; `xcomp`) et ceux dont le sujet n’est pas contrôlé (sujet à l’intérieur de la clause; `ccomp`)
- Modificateurs de clauses adverbiaux (`advcl`)
- Modificateurs de clauses adnominaux (`acl`)

Calculé des deux façons suivantes :

- en nombre absolu 
- en relation au nombre total de mots l’échantillon

[https://universaldependencies.org/u/overview/complex-syntax.html](https://universaldependencies.org/u/overview/complex-syntax.html)

## Longueur moyenne des phrases

Nombre moyen de mots par phrase. Le nombre moyen de mots par phrase dans l’échantillon sera calculé. Les limites des phrases seront déterminées par le "dependency parse" par défaut de spaCy.

[https://spacy.io/usage/linguistic-features#sbd](https://spacy.io/usage/linguistic-features#sbd)

## Phrases incomplètes

Phrases qui ne contiennent pas un minimum d’un verbe et son sujet. Nombre total de phrases dans l’échantillon qui ne contiennent aucun verbe accompagné de son sujet.

Calculé des deux façons suivantes :

- en nombre absolu 
- en relation au nombre total de mots l’échantillon

Pourraient indiquer : déficits lexico-sémantiques, déficits syntaxiques, difficultés à planifier le discours (Boschi et al. 2017).

## Nombre de phrases prépositionnelles

Phrases qui contiennent une préposition son objet (nom ou pronom) et n’importe quel modificateur de l’objet, (Boschi et al. 2017).

Calculé des deux façons suivantes :

- en nombre absolu 
- en relation au nombre total de mots l’échantillon

## Nombre de phrases verbales

Phrases de bases contenant au moins un verbe et ces dépendants. Calculé à l’aide des implémentations de base de spaCy.

Calculé des deux façons suivantes :

- en nombre absolu 
- en relation au nombre total de mots l’échantillon

## Longueur et nombre de phrases nominales

Une phrase nominale est un groupe de mots centré autour d'un nom (substantif) qui fonctionne comme sujet, objet ou complément dans une phrase. Par exemple dans la phrase "Le chat noir dort sur le tapis", "Le chat noir" est une phrase nominale.

La longueur d'une phrase nominale est le nombre de mots qui la composent. Elle peut varier de deux mots comme "Une maison" à une séquence plus longue comme "La grande maison au bord de la route".

Nombre total et longueur moyenne des phrases nominales dans l’échantillon. Calculé à l’aide des implémentations de base de spaCy.

Calculé des deux façons suivantes:

- en nombre absolu 
- en relation au nombre total de mots l’échantillon

[https://spacy.io/usage/linguistic-features#noun-chunks](https://spacy.io/usage/linguistic-features#noun-chunks)

## Temps de verbes utilisés

Formes que prennent les verbes pour indiquer à quel moment l’action se situe dans le temps. Nombre total de verbes conjugués au présent, au passé et au futur dans l’échantillon.

Calculé des deux façons suivantes:

- en nombre absolu 
- en relation au nombre total de mots l’échantillon

## Clauses par phrase

Groupes de mots comprenant un sujet et un verbe normalement utilisés pour ajouter davantage de détails concernant un nom dans une phrase. Nombre moyen de clauses par phrase calculé à l’aide des implémentations de base de spaCy.

## Proportion de noms accompagnés de déterminants

Proportion de noms pour lesquels un déterminant est présent. Nombre de noms dans l’échantillon rattachés à un déterminant sur le nombre total de noms dans l’échantillon. Calculé à l’aide du dependency parse de spaCy.

## Phrases coordonnées

Phrases unies par une ou plusieurs conjonctions de coordination. Nombre total de phrases dans l’échantillon contenant les conjonctions de coordination suivantes: "and", "but", "for", "nor", "or", "yet", "so" (Boschi et al. 2017).

Calculé des deux façons suivantes:

- en nombre absolu 
- en relation au nombre total de mots l’échantillon

## Noms des variables

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
