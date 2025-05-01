# Extraction de variables phonétiques

| Caractéristique/famille de caractéristique | Définition | Opérationnalisation | Nombre de caractéristiques | Informations additionnelles | Fonction Python associée |
| --- | --- | --- | --- | --- | --- |
| **Fréquence Fondamentale (F0)** | Variations de la tonalité de la voix, utile pour analyser l'intonation et le stress émotionnel. |  |  |  |  |
| **Intensité (Volume)** | Mesure du volume sonore, peut refléter l'emphase ou les changements émotionnels. |  |  |  |  |
| **Qualité de la Voix** | Caractéristiques telles que la rugosité, le souffle, la clarté ou la nasalité de la voix. |  |  |  |  |
| **Spectrogramme** | Représentation visuelle de l'évolution des fréquences dans le temps, utile pour une analyse détaillée des caractéristiques sonores. |  |  |  |  |
| F**réquences des Formants (F1, F2, etc.)** | Informations importantes sur les caractéristiques des voyelles prononcées. |  |  |  |  |
| **Modulation de Fréquence et d'Amplitude** | Variations de la fréquence et de l'amplitude au sein d'un même phonème ou mot. |  |  |  |  |
| **Harmonic-to-Noise Ratio (HNR)** | Rapport entre les composantes harmoniques et bruyantes de la voix, utile pour évaluer la qualité vocale. |  |  |  |  |
| **Jitter (Variabilité de Fréquence)** | Variabilité de la fréquence fondamentale d'un son, peut indiquer une tension ou un stress vocal. |  |  |  |  |
| **Shimmer (Variabilité d'Amplitude)** | Variabilité de l'amplitude des ondes sonores, liée à la stabilité et à la qualité de la voix. |  |  |  |  |
| **Phonation** | Ces caractéristiques se concentrent sur les aspects de la production vocale liés à l'activité des cordes vocales. Elles incluent des mesures comme la fréquence fondamentale (pitch), le jitter et le shimmer, qui sont des indicateurs de la stabilité de la fréquence et de l'amplitude de la voix. |  |  |  |  |
| **Articulation** | Ces caractéristiques sont liées à la manière dont les mots et les sons sont formés par le locuteur. Elles peuvent inclure des mesures de la durée des phonèmes, la vitesse de l'articulation et la dynamique des mouvements articulatoires. |  |  |  |  |
| **Prosodie** | La prosodie concerne le rythme, l'intonation et l'accentuation dans la parole. Les caractéristiques prosodiques comprennent des mesures de l'intensité, de la durée des syllabes et des motifs d'accentuation. |  |  |  |  |
| **Phonologie** | Ces caractéristiques analysent les aspects de la parole liés à la structure phonémique, comme les changements dans la qualité des voyelles ou des consonnes. |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

Praat, PyDub, librosa

[https://github.com/jcvasquezc/DisVoice](https://github.com/jcvasquezc/DisVoice)

### **DisVoice**

1. **Description** :
    - DisVoice est un framework Python conçu pour calculer des caractéristiques à partir de fichiers de parole. Il calcule des caractéristiques liées à la glotte, la phonation, l'articulation, la prosodie, la phonologie et utilise des stratégies d'apprentissage de représentation basées sur les autoencodeurs.
    - Les caractéristiques extraites sont utilisées pour reconnaître des aspects paralinguistiques de la parole, comme les émotions ou les capacités de communication chez les patients souffrant de différents troubles de la parole.
2. **Types de Caractéristiques** :
    - **Caractéristiques Glottales** : Incluent la variabilité du temps entre les instants de fermeture glottale consécutifs, le quotient d'ouverture moyen, l'amplitude normalisée et la richesse harmonique.
    - **Caractéristiques Phonatoires** : Comprend le premier et le second dérivé de la fréquence fondamentale, le jitter, le shimmer, et l'énergie logarithmique.
    - **Caractéristiques Articulatoires** : Comportent des énergies de bande Bark, des coefficients cepstraux de fréquence Mel, et les dérivées premières et secondes de ces coefficients dans les transitions de début et de fin de parole.
3. **Installation** :
    - Prérequis : Praat doit être installé avant d'utiliser DisVoice. Pour Linux, utilisez **`apt-get install praat`**, et pour Windows, téléchargez Praat et ajoutez son chemin d'accès aux variables d'environnement.
    - Installation de DisVoice : Utilisez la commande **`pip install disvoice`** ou **`python setup.py install`** après avoir cloné le dépôt depuis GitHub.
4. **Utilisation** :
    - Pour extraire des caractéristiques, vous devrez exécuter des scripts spécifiques en fonction du type de caractéristique que vous souhaitez calculer. Par exemple, **`articulation.py`** pour les caractéristiques articulatoires, en spécifiant le chemin vers le fichier audio et le format de sortie souhaité.

### **Comment S'en Servir**

- **Extraction de Caractéristiques** : Après l'installation, vous pouvez utiliser DisVoice pour extraire des caractéristiques spécifiques de fichiers audio de parole. Par exemple, pour les caractéristiques articulatoires, vous pouvez utiliser le script **`articulation.py`** avec des options pour spécifier si vous souhaitez des matrices statiques ou dynamiques, et choisir le format de sortie (par exemple, csv, txt, npy).
- **Analyse des Données** : Les caractéristiques extraites peuvent être utilisées pour diverses analyses, telles que l'évaluation des troubles de la parole, la détection des émotions, ou l'analyse de la qualité de la communication.

DisVoice offre une solution complète pour l'analyse des caractéristiques de la parole, utile dans des contextes de recherche et de diagnostic clinique. Son utilisation nécessite une compréhension des concepts de base du traitement du signal et de la linguistique.