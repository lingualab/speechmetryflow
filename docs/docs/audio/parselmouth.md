# Parselmouth & Praat

The pipeline produces `population_lingualab_audio` which is an implementation of [Parselmouth Praat Scripts in Python](https://osf.io/6dwr3/) by [David R. Feinberg](https://osf.io/z2hy6/)

This script will measure pitch, standard deviation of pitch, hnr, jitter, shimmer, and formants in python using parselmouth, a package that runs Praat in python.

## Links to some relevant praat documentation

- Formant: [Formant-manual](https://www.fon.hum.uva.nl/praat/manual/Formant.html)
- Jitter: [Jitter-manual](https://www.fon.hum.uva.nl/praat/manual/Voice_2__Jitter.html)
- Shimmer: [Shimmer-manual](https://www.fon.hum.uva.nl/praat/manual/Voice_3__Shimmer.html)
- PointProcess: [PointProcess-manual](https://www.fon.hum.uva.nl/praat/manual/PointProcess.html)

## Variable definition

| Characteristic/feature family | Definition |
| --- | --- |
| **Fundamental Frequency (F0)** | Variations in voice pitch, useful for analyzing intonation and emotional stress. |
| **Intensity (Volume**) | Measure of loudness, can reflect emphasis or emotional changes. |
| **Voice Quality** | Characteristics such as roughness, breathiness, clarity or nasality of the voice. |
| **Spectrogram** | Visual representation of frequency evolution over time, useful for detailed analysis of sound characteristics. |
| **Formant Frequencies (F1, F2, etc.)** | Important information on the characteristics of pronounced vowels. |
| **Frequency and Amplitude Modulation** | Variations in frequency and amplitude within the same phoneme or word. |
| **Harmonic-to-Noise Ratio (HNR)** | Ratio between harmonic and noisy components of the voice, useful for assessing vocal quality. |
| **Jitter (Frequency Variability)** | Variability in the fundamental frequency of a sound, can indicate vocal stress or tension. |
| **Shimmer (Amplitude Variability**) | Variability in the amplitude of sound waves, related to vocal stability and quality. |
| **Phonation** | These characteristics focus on aspects of vocal production linked to vocal cord activity. They include measures such as pitch, jitter and shimmer, which are indicators of the frequency and amplitude stability of the voice. |
| **Articulation** | These characteristics relate to the way words and sounds are formed by the speaker. They can include measures of phoneme duration, articulation speed and articulatory movement dynamics. |
| **Prosody** | Prosody concerns the rhythm, intonation and accentuation of speech. Prosodic features include measures of intensity, syllable duration and stress patterns. |
| **Phonology** | These characteristics analyze aspects of speech related to phonemic structure, such as changes in vowel or consonant quality. |

## Variable names

- `F0_std`
- `duration`
- `f0_mean`
- `formants_1_mean`
- `formants_1_median`
- `formants_2_mean`
- `formants_2_median`
- `formants_3_mean`
- `formants_3_median`
- `formants_4_mean`
- `formants_4_median`
- `hnr`
- `jitter_ddp`
- `jitter_local`
- `jitter_local_absolute`
- `jitter_ppq5`
- `jitter_rap`
- `shimmer_apq11`
- `shimmer_apq3`
- `shimmer_apq5`
- `shimmer_dda`
- `shimmer_local`
- `shimmer_local_dB`