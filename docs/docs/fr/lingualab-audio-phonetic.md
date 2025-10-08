# Extraction de variables phonétiques

## Définition des variables

| Caractéristique/famille de caractéristique | Définition |
| --- | --- |
| Fréquence Fondamentale (F0) | Variations de la tonalité de la voix, utile pour analyser l'intonation et le stress émotionnel. |
| Intensité (Volume) | Mesure du volume sonore, peut refléter l'emphase ou les changements émotionnels. |
| Qualité de la Voix | Caractéristiques telles que la rugosité, le souffle, la clarté ou la nasalité de la voix. |
| Spectrogramme | Représentation visuelle de l'évolution des fréquences dans le temps, utile pour une analyse détaillée des caractéristiques sonores. |
| Fréquences des Formants (F1, F2, etc.) | Informations importantes sur les caractéristiques des voyelles prononcées. |
| Modulation de Fréquence et d'Amplitude | Variations de la fréquence et de l'amplitude au sein d'un même phonème ou mot. |
| Harmonic-to-Noise Ratio (HNR) | Rapport entre les composantes harmoniques et bruyantes de la voix, utile pour évaluer la qualité vocale. |
| Jitter (Variabilité de Fréquence) | Variabilité de la fréquence fondamentale d'un son, peut indiquer une tension ou un stress vocal. |
| Shimmer (Variabilité d'Amplitude) | Variabilité de l'amplitude des ondes sonores, liée à la stabilité et à la qualité de la voix. |
| Phonation | Ces caractéristiques se concentrent sur les aspects de la production vocale liés à l'activité des cordes vocales. Elles incluent des mesures comme la fréquence fondamentale (pitch), le jitter et le shimmer, qui sont des indicateurs de la stabilité de la fréquence et de l'amplitude de la voix. |
| Articulation | Ces caractéristiques sont liées à la manière dont les mots et les sons sont formés par le locuteur. Elles peuvent inclure des mesures de la durée des phonèmes, la vitesse de l'articulation et la dynamique des mouvements articulatoires. |
| Prosodie | La prosodie concerne le rythme, l'intonation et l'accentuation dans la parole. Les caractéristiques prosodiques comprennent des mesures de l'intensité, de la durée des syllabes et des motifs d'accentuation. |
| Phonologie | Ces caractéristiques analysent les aspects de la parole liés à la structure phonémique, comme les changements dans la qualité des voyelles ou des consonnes. |

Praat, PyDub, librosa

[https://github.com/jcvasquezc/DisVoice](https://github.com/jcvasquezc/DisVoice)

## Noms des variables

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
