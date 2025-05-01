# Fluence

Pauses :

Sur GitHub, il existe une bibliothèque nommée **`pauses`** développée par Jim Schwoebel, conçue spécifiquement pour extraire les longueurs des pauses à partir de fichiers audio. Cette bibliothèque offre deux techniques principales pour l'analyse des pauses dans les enregistrements audio :

1. **Seuillage (Thresholding)** :
    - Le script **`extract_pauselength.py`** utilise la technique de seuillage pour segmenter les enregistrements audio.
    - Il se base sur un seuil de silence défini (par exemple, 50 millisecondes et -32 dBFS) pour distinguer les segments parlés des segments silencieux.
2. **Classification par Apprentissage Automatique** :
    - Une autre approche consiste à utiliser un modèle de machine learning pour détecter les longueurs des pauses.
    - Dans cette méthode, les fichiers sont divisés en fenêtres de 200 millisecondes, chacune étant étiquetée comme un événement de 'pause' ou de 'parole'.
    - Un modèle SVM optimisé est utilisé pour la classification, atteignant une précision d'environ 91.23%.

Il est important de noter que ces méthodes sont limitées aux environnements à faible bruit. Si le fichier audio contient beaucoup de bruit de fond, il est recommandé de nettoyer et de supprimer le bruit avant d'utiliser ces scripts pour calculer les longueurs des pauses.

Pour plus d'informations et pour accéder aux scripts, vous pouvez visiter le [dépôt GitHub de **`pauses`**](https://github.com/jim-schwoebel/pauses).

[Identification des pauses remplies](Fluence%2018ccd6be978b81579626db7b4f4bab2e/Identification%20des%20pauses%20remplies%2018ccd6be978b81de8758efdc166c3f67.md)

[**Identification des Pauses** silencieuses](Fluence%2018ccd6be978b81579626db7b4f4bab2e/Identification%20des%20Pauses%20silencieuses%2018ccd6be978b81928ebecd306d911683.md)