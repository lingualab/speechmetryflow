# openSMILE

[openSMILE](https://audeering.github.io/opensmile-python/) is a toolbox developped by [audEERING](https://www.audeering.com/research/opensmile/)

The python interface is used to extract GeMAPS and eGeMAPS feature sets.

## Features

All features are described in the following paper: [GeMAPS-paper](https://sail.usc.edu/publications/files/eyben-preprinttaffc-2015.pdf)

| Frequency related parameters | |
| - | - |
| **Pitch** | logarithmic F0 on a semitone frequency scale, starting at 27.5 Hz (semitone 0). |
| **Jitter** | deviations in individual consecutive F0 period lengths. |
| **Formant 1, 2, and 3 frequency** | centre frequency of first, second, and third formant. |
| **Formant 1** | bandwidth of first formant. |

| Energy/Amplitude related parameters | |
| - | - |
| **Shimmer** | difference of the peak amplitudes of consecutive F0 periods. |
| **Loudness** | estimate of perceived signal intensity from an auditory spectrum. |
| **Harmonics-to-Noise Ratio (HNR)** | relation of energy in harmonic components to energy in noise-like components. |

| Spectral (balance) parameters | |
| - | - |
| **Alpha Ratio** | ratio of the summed energy from 50–1000 Hz and 1–5 kHz |
| **Hammarberg Index** | ratio of the strongest energy peak in the 0–2 kHz region to the strongest peak in the 2–5 kHz region. |
| **Spectral Slope 0–500 Hz and 500–1500 Hz** | linear regression slope of the logarithmic power spectrum within the two given bands. |
| **Formant 1, 2, and 3 relative energy** | as well as the ratio of the energy of the spectral harmonic peak at the first, second, third formant’s centre frequency to the energy of the spectral peak at F0. |
| **Harmonic difference H1–H2** | ratio of energy of the first F0 harmonic (H1) to the energy of the second F0 harmonic (H2). |
| **Harmonic difference H1–A3** | ratio of energy of the first F0 harmonic (H1) to the energy of the highest harmonic in the third formant range (A3). |
