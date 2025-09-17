# Production de la parole

## Définitions

### Lemmatisation

Un lemme dans le contexte de la linguistique est la forme canonique de base ou de référence d'un mot. En d'autres termes c'est la forme sous laquelle un mot est inscrit dans un dictionnaire ou utilisé pour représenter toutes les variantes flexionnelles d'un mot. L'idée est de regrouper les différentes formes d'un mot (comme les temps passés futurs les pluriels etc.) sous une seule forme standardisée.

Les lemmes ne sont pas des marqueurs de ponctuation ou des pauses remplies (comme "hmm" ou "euh") qui sont généralement omis dans l'analyse lexicale car ils ne portent pas de sens lexical spécifique.

Exemples:

- "suis", "es", "est", "sommes", "êtes", "sont" est "être"
- "chien", "chiens", "chienne", "chiennes", est "chien"
- "meilleur", "mieux" est "bon"

1. **Processus**: La lemmatisation implique une analyse morphologique complète des mots pour en déduire leur forme canonique ou lemme. La lemmatisation tient compte du contexte du mot de son genre de son nombre et de son temps pour déterminer sa forme de base.
2. **Exemple**: Reprenant votre exemple le mot « trouvez » est ramené à sa forme de base « trouver ». Contrairement au stemming le résultat de la lemmatisation est toujours un mot valide et reconnaissable.
3. **Usage**: La lemmatisation est souvent utilisée dans des situations où la précision est cruciale comme dans les systèmes de compréhension du langage naturel ou les applications linguistiques où la compréhension du contexte et la précision sémantique sont importantes.

### Phonème

Un phonème est une unité sonore de base dans une langue qui permet de distinguer un mot d'un autre. C'est la plus petite unité de son qui peut changer le sens d'un mot. Les phonèmes sont des concepts abstraits utilisés pour analyser la façon dont les sons fonctionnent dans une langue particulière. Ils ne sont pas les sons eux-mêmes mais plutôt des catégories de sons qui peuvent être prononcés de différentes manières par différents locuteurs tout en étant perçus comme le même son.

En français, les sons /p/ et /b/ sont des phonèmes distincts car ils différencient des mots comme "patte" et "batte". Le phonème /k/ est présent dans les mots "café" et "quai" bien que le son soit produit de manière différente dans chaque mot (avec une lettre différente).

En anglais les phonèmes /t/ et /d/ différencient les mots "tap" (taper) et "dap" (un mot inventé mais qui sonne différemment grâce au phonème initial différent).

### Tokenisation

Découpage du texte en plusieurs pièces appelés *tokens*.

Example: "Vous trouverez en pièce jointe le document en question" donne "Vous", "trouverez", "en", "pièce", "jointe", "le", "document", "en", "question"

### Stemming

1. **Processus**: Le stemming consiste à couper les extrémités (sufffixes et parfois préfixes) des mots pour atteindre une forme simplifiée. Ce processus est généralement heuristique et ne tient pas compte du contexte ou de la morphologie complète des mots. Il se base sur des règles simples et fixes pour tronquer les mots.
2. **Exemple**: Dans votre exemple « trouverez » devient « trouv ». Ici le suffixe « -erez » est enlevé pour arriver à la racine « trouv ». Cette racine n'est pas nécessairement un mot valide en soi.
3. **Usage**: Le stemming est souvent utilisé dans les systèmes de recherche et de filtrage où la précision n'est pas critique mais où la vitesse et la simplicité du processus sont importantes.

### Lemmatisation

Cela consiste à réaliser la même tâche que le stemming mais en utilisant un vocabulaire et une analyse fine de la construction des mots. La **lemmatisation** permet donc de supprimer uniquement les terminaisons inflexibles et donc à **isoler la forme canonique du mot** connue sous le nom de lemme.

### Similarité Sémantique

La similarité sémantique mesure à quel point deux mots ou concepts sont proches en termes de signification. Dans le contexte des word embeddings cela se traduit souvent par la proximité de leurs vecteurs dans l'espace vectoriel.

### Word Embedding

Le Word Embedding (ou plongement lexical en français) est une méthode d'encodage qui vise à représenter les mots ou les phrases d’un texte par des vecteurs de nombres réels décrit dans un modèle vectoriel (ou Vector Space Model).

D'une manière plus simple chaque mot du vocabulaire V étudié sera représenté par un vecteurs de taille m. Le principe du Word Embedding est de projeter chacun de ces mots dans un espace vectoriel d'une taille fixe N (N étant différent de m). C'est-à-dire quelle que soit la taille du vocabulaire on devra être capable de projeter un mot dans son espace.

### Modèles d'Embedding

CBOW (Continuous Bag-of-Words) : Dans ce modèle le mot cible est prédit à partir de mots environnants. Il prend en compte le contexte représenté par les mots voisins pour prédire le mot cible​​.

Skip-Gram : Inverse du CBOW, ce modèle prédit le contexte d'un mot donné. Il est efficace pour représenter des mots ou des phrases rares​​.

### Arbre de dépendance

Dans une grammaire de dépendance une phrase est représentée sous la forme d'un arbre. Chaque mot dans la phrase est un nœud de cet arbre. Les liens (ou arcs) entre ces mots représentent des relations syntaxiques.

## Variables

### Longueur de l’échantillon

Soit le nombre total de mots dans l’échantillon. C'est le nombre total de lemmas qui ne sont pas des marqueurs de ponctuation incluant les pauses remplies (ex. hmmm).

### Fragments de mots

Production de seulement une partie des phonèmes d’un mot sans remplacements de sons ou erreurs d’articulation. Peut être suivi de la production complète du mot ou non. Un fragment de mot est une portion d'un mot qui contient un ou plusieurs phonèmes de ce mot mais pas l'entièreté de ses phonèmes. En d'autres termes c'est une partie d'un mot pas le mot complet.

- **Identification des Fragments** : Dans l'échantillon de parole ou de texte vous cherchez des occurrences où seulement une partie d'un mot est prononcée ou écrite. Cela peut être le début d'un mot la fin ou même le milieu tant que ce n'est pas le mot entier.
- **Comptage des Fragments** : Vous comptez ensuite le nombre total de ces fragments dans l'échantillon. Chaque occurrence d'un fragment de mot est comptée comme une unité distincte.
- **Exclusion des Erreurs de Prononciation et Remplacements de Sons** : Il est important de noter que les fragments de mots ne doivent pas être confondus avec des erreurs de prononciation ou des substitutions de sons. Ce sont des occurrences spécifiques où les phonèmes manquants ne sont pas remplacés par d'autres sons ou erreurs.
- **Exemple** : "I her kitchkitchen" Un exemple de cela serait dans un échantillon de parole où quelqu'un commence à dire un mot mais s'arrête avant de le finir comme commencer à dire "incompréhens..." au lieu de "incompréhensible". Chaque fois que cela se produit cela compterait comme un fragment de mot.

### Fluence

#### Pauses silencieuses

Segments de l’échantillon au cours desquels aucun son n’est produit après que le participant ait commencé à parler. C'est le nombre total de fois où « [pause] » apparaît dans l’échantillon. Pourraient indiquer : difficultés d’accès lexical difficultés syntaxiques difficultés de planification du discours (Boschi et al. 2017).

#### Pauses remplies

Pause dans le discours marquée par « uhm » ou une variante de ce son (« hmmm » « hum » « er » « ah » etc.). Nombre total d’occurrences des mots « uhm » « hmmm » « hum » « uh » « er » et « ah » dans l’échantillon. Pourraient indiquer : difficultés d’accès lexical difficultés syntaxiques difficultés de planification du discours (Boschi et al. 2017).

#### Répétitions de mots de groupes de mots ou d’idées

Mots ou informations de contenu qui sont présentes plus d’une fois dans l’échantillon (répétitions directement collées les unes sur les autres ou plus éloignées dans l’échantillon). Nombre total de mots de groupes de mots (combinaisons de 2 à 6 mots) ou d’informations de contenu qui sont présents plus d’une fois dans l’échantillon. Pourrait indiquer: déficits lexico- sémantiques difficultés de planification du discours (Boschi et al. 2017).

### Noms des variables

- `Nombre_de_lemmes`
- `Nombre_de_fragments`
- `Nombre_de_fragments_autre_methode`
- `Fragments_en_contexte`
- `Nombre_de_mots`
- `Nombre_de_lemmes_differents`
- `Nombre_de_pauses_silencieuses`
- `Nombre_de_pauses_remplies`
- `Nombre_de_repetitions_mots`