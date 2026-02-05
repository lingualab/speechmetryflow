# Uhm-o-meter

The pipeline produces `population_uhmometer_metrics` which is an implementation of [PRAAT scripts to measure fluency automatically](https://sites.google.com/view/uhm-o-meter/home)

It consists of two [PRAAT](https://www.fon.hum.uva.nl/praat/) scripts to measure fluency automatically. A rewritten praat script to measure silent pauses and articulation rate (original script syllable nuclei described in [De Jong & Wempe, 2009](https://www.tandfonline.com/doi/full/10.1080/0969594X.2021.1951162)), and a new script to measure filled pauses. This new script is tested on Dutch and English L2 data.

# Features list

- nsyll
- npause
- dur(s)
- phonationtime(s)
- speechrate(nsyll/dur)
- articulation_rate(nsyll/phonationtime)
- ASD(speakingtime/nsyll)
