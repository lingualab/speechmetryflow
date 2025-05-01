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

# Identification des pauses remplies

```python
import speech_recognition as sr

def count_filled_pauses(audio_path, languages):
    """
    Compte le nombre total d'occurrences des pauses remplies dans un échantillon audio.

    Paramètres :
    - audio_path : Chemin vers le fichier audio.
    - languages : Liste des codes de langue pour la reconnaissance vocale.

    Retourne :
    - counts : Dictionnaire avec le nombre total d'occurrences pour chaque pause remplie.
    """

    # Définir les mots de pause remplie pour chaque langue
    filled_pauses = {
        "en": ["uhm", "hmmm", "hum", "uh", "er", "ah"],  # Anglais
        "fr": ["euh", "hm", "heu", "hmm"],  # Français
        # Ajouter d'autres langues ici
    }

    # Initialiser le compteur
    counts = {word: 0 for lang in languages for word in filled_pauses.get(lang, [])}

    # Charger le fichier audio
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)

    # Effectuer la reconnaissance vocale pour chaque langue
    for lang in languages:
        try:
            text = recognizer.recognize_google(audio_data, language=lang)
            words = text.lower().split()

            # Compter les occurrences des pauses remplies
            for word in words:
                if word in filled_pauses[lang]:
                    counts[word] += 1

        except sr.UnknownValueError:
            print(f"Langue non reconnue ou audio non compréhensible en {lang}")
        except sr.RequestError:
            print(f"Erreur de requête pour la langue {lang}")

    return counts

# Exemple d'utilisation
# counts = count_filled_pauses("chemin/vers/audio.wav", ["en", "fr"])
# print(counts)
```

# Identification des Pauses silencieuses

### **Explication du Code**

Le code utilise la bibliothèque **`librosa`** pour charger et analyser le fichier audio. Voici les étapes clés du processus :

1. **Charger l'Audio** : Le fichier audio est chargé en mémoire. **`librosa.load`** renvoie le signal audio et le taux d'échantillonnage (fréquence d'échantillonnage).
2. **Calcul de l'Intensité Sonore** : L'intensité sonore du signal audio est calculée en décibels (dB) en utilisant une transformation de Fourier à court terme (STFT).
3. **Détection du Silence** : Un seuil de silence est défini (en dB). Les moments où l'intensité sonore est inférieure à ce seuil sont considérés comme du silence.
4. **Identification des Pauses** : Le code itère sur le signal pour identifier les débuts et fins des pauses silencieuses, en prenant en compte une durée minimale pour qu'une pause soit considérée comme significative.
5. **Conversion en Temps** : Les indices des pauses détectées sont convertis en temps réel (en secondes) pour une compréhension facile.

```python
# Importation des bibliothèques nécessaires
import librosa  # Utilisée pour le traitement de l'audio
import numpy as np  # Utilisée pour les opérations mathématiques

# Définition de la fonction pour détecter les pauses silencieuses
def detect_silent_pause(audio_path, silence_threshold=-30.0, min_pause_duration=0.5):
    # Charger le fichier audio à partir du chemin spécifié
    y, sr = librosa.load(audio_path, sr=None)  # y est le signal audio, sr est le taux d'échantillonnage

    # Calculer l'intensité sonore du signal en décibels
    intensity = librosa.amplitude_to_db(np.abs(librosa.stft(y)))  # Transformation de Fourier à court terme

    # Calculer la moyenne de l'intensité sonore sur toutes les fréquences à chaque instant
    mean_intensity = np.mean(intensity, axis=0)

    # Détecter les moments de silence (intensité en dessous du seuil de silence)
    silent = mean_intensity < silence_threshold

    # Initialiser la liste pour stocker les pauses détectées
    pauses = []
    pause_start = None  # Variable pour marquer le début d'une pause

    # Itérer sur le signal pour détecter les pauses silencieuses
    for i, is_silent in enumerate(silent):
        if is_silent and pause_start is None:
            # Marquer le début d'une pause
            pause_start = i
        elif not is_silent and pause_start is not None:
            # Marquer la fin d'une pause
            pause_end = i

            # Convertir les indices de début et de fin de la pause en temps réel
            start_time = librosa.frames_to_time(pause_start, sr=sr)
            end_time = librosa.frames_to_time(pause_end, sr=sr)

            # Ajouter la pause à la liste si sa durée est supérieure à la durée minimale
            if end_time - start_time >= min_pause_duration:
                pauses.append((start_time, end_time))

            # Réinitialiser pause_start pour la prochaine détection
            pause_start = None

    # Retourner la liste des pauses détectées
    return pauses

# Exemple d'utilisation de la fonction
# pauses = detect_silent_pause("chemin/vers/le/fichier/audio.wav")
# print(pauses)
```