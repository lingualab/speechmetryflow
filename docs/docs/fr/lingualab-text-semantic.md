# Caractéristiques sémantiques

## 25 informations de contenu (ICUs)

Sujets, lieux, objets et actions séparés qui sont représentés dans l’image *Cookie Theft*.

La liste des unités de contenu (ICUs) pour le test de l'image du vol de cookies tel qu'établi par Yorkston et Beukelman (1980).

La définition des ICUs se trouve [ici](https://github.com/lingualab/Text2Variable/blob/e24a89cf4a39db8e415245a531c2102ede15d7b1/lingua_extraction/Database_linguistique.py#L68)

## Nombre total d’ICUs

Nombre total d’ICUs qui apparaissent dans l’échantillon. Nombre total d’ICUs étiquetées comme « VRAI».

## Efficacité

Ratio de la longueur totale de l’échantillon sur le nombre total d’ICUs présentes dans l’échantillon.

## Densité d’idées

Similarité sémantique moyenne entre les idées (conceptuellement distinctes) transmises à l’intérieur d’une fenêtre de mots déplacée à-travers le texte.

La distance cosine (similarité sémantique) moyenne entre toutes les paires de "word embeddings" à l’intérieur d’une fenêtre déplacée à-travers le texte. Les "word embeddings" seront extraits à partir du modèle spaCy `en_core_web_lg` qui a supporté l’identification des dépendances syntaxiques et le Part-of-Speech tagging. À l’intérieur d’une fenêtre la moyenne de toutes les distances cosines sera calculée. Des fenêtres de 3, 10, 25 et 40 mots avec un incrément de la moitié de la longueur de la fenêtre seront implémentées.

## Noms des variables

- `Nombre_ICU_TRUE`
- `Efficacite_ICU`
- TODO