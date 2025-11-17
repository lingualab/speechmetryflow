#	PRAAT SCRIPT FILLED PAUSES
#	Set Syllable Boundaries at -6 dB around points in the tier "Nuclei" (as set by the
#	script "SyllableNucleiv3.praat"), compute a number of global (speaker specific) and
#	local (syllable specific) parameters for automatic detection of Filled Pauses.
#
#	Optionally, save the local parameters for all syllables in a table.
#
#	J J A Pacilly,  1-nov-2019, for Nivja de Jong, on behalf of:
#	  British Council, Aptis Research Grants
#	J J A Pacilly, 14-feb-2020, retain max. similarity with version for internal use
#
#	Note that this script is used by "SyllableNucleiv3.Praat", but it can also
#	be used as a standalone script with a selected Sound and Textgrid object
#	as long as this TextGrid contains a pointTier with the name "Nuclei".
#
#	The settings and thresholds in this script are trained and tested on
#	Dutch and English L2 data. See [LINK?] the ARAG report by De Jong and
#	Pacilly (2019) for more information.
#
#	Copyright (C) 2019 - J J A Pacilly & N H de Jong, LUCL - Universiteit Leiden
#
#	This program is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#	See the GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see http://www.gnu.org/licenses/

form Detect Filled Pauses
  optionmenu Language 1
    option English
#   option Mandarin (not yet implemented)
#   option Spanish  (not yet implemented)
    option Dutch
  real Filled_Pause_threshold 1.00  ; cut-off higher/lower
  boolean Save_Table 0
  endform
  
idSnd = selected ("Sound")
name$ = selected$("Sound")
idTG  = selected ("TextGrid")

@setSB: idSnd, idTG			; set/replace tier(s) and define vectors for initial analysis

if nrSyllables
  @doGlobalAnalyses: idSnd		; do global analysis of ALL syllables identified by tier Nuclei
  @sdF0:  idSnd				; fills the arrays dF0[],   dqF0[]   and sdF0[]
  @replaceUndefinedF0: 0		; replace Undefined values by mean
  @sdFmt: idSnd				; fills the arrays dF1-3[], dqF1-3[] and sdF1-3[]
  @processData: idTG, name$, "Auto"	; create Auto table, set labels
  idTableAuto = processData.idTable
  endif

selectObject: idSnd, idTG
if idTableAuto
  plusObject: idTableAuto
  endif


procedure setSB: .idSnd, .idTG

# For testing, allow successive runs of this script

  selectObject: .idTG
  .tierNuclei  = 0
  .tierPhrases = 0
  .tierAuto    = 0
  .nrTiers = Get number of tiers
  for .tier to .nrTiers
    .name$ = Get tier name: .tier
    if   .name$ == "Nuclei"
      .tierNuclei = .tier
    elif .name$ == "Phrases"
      .tierPhrases = .tier
    elif .name$ == "DFauto" + " ('language$')"
      Remove tier: .tier
      Insert interval tier: .tier, "DFauto" + " ('language$')"
      .tierAuto = .tier
    elif left$(.name$, 5) == "DFman" or left$(.name$, 5) == "dfMan"
      .tierMan = .tier
      endif
    endfor

  if .tierNuclei == 0
    exitScript: "No tier ""Nuclei"" found, please run ""SyllableNuclei.praat"" first."
    endif

  nrSyllables = Get number of points: .tierNuclei
  d#   = zero#(nrSyllables)

  tNuc[0]             = Get start time
  tNuc[nrSyllables+1] = Get end time
  for syllable to nrSyllables
    tNuc[syllable] = Get time of point: .tierNuclei, syllable
    if .tierPhrases
      .iPhrase = Get interval at time: .tierPhrases, tNuc[syllable]
      .tFromPhrase[syllable] = Get start time of interval: .tierPhrases, .iPhrase
      .tToPhrase[syllable]   = Get end time of interval: .tierPhrases, .iPhrase
      endif
    endfor

# Get minimum Intensity *between* Nuclei

  selectObject: .idSnd
  .idInt   = To Intensity: 100, 0, "yes"
  nrFrames = Get number of frames
  for syllable to nrSyllables+1
    tSBMin[syllable] = Get time of minimum: tNuc[syllable-1], tNuc[syllable], "Parabolic"
    endfor
  tMeanSyllable = (tSBMin[nrSyllables+1] - tSBMin[1]) / nrSyllables

# Find -6 dB *around* Nuclei but avoid that these boundaries cross
# the 'minimum Intensity boundaries' (yields twice as much intervals)

  for syllable to nrSyllables
    frNuc = Get frame number from time: tNuc[syllable]
    frNuc = round(frNuc)
    dBNuc = Get value in frame: frNuc

    frFrom = frNuc
    repeat
      frFrom -= 1
      dBL = Get value in frame: frFrom
      tL  = Get time from frame number: frFrom
      until dBL < dBNuc - 6 or tL < tSBMin[syllable] or frFrom < 2
    tFrom[syllable] = Get time from frame number: frFrom

    frTo = frNuc
    repeat
      frTo += 1
      dBR = Get value in frame: frTo
      tR  = Get time from frame number: frTo
      until dBR < dBNuc - 6 or tR > tSBMin[syllable+1] or frTo > nrFrames-1
    tTo[syllable] = Get time from frame number: frTo

    d6Org[syllable] = tTo[syllable] - tFrom[syllable]

    if .tierPhrases
      tFrom[syllable] = max(.tFromPhrase[syllable], tFrom[syllable])
      tTo  [syllable] = min(.tToPhrase  [syllable], tTo  [syllable])
      endif
    endfor

# only the boundaries *around* Nuclei are being used

  selectObject: .idTG
  if not .tierAuto
    Insert interval tier: .nrTiers + 1, "DFauto" + " ('language$')"
    .tierAuto = .nrTiers + 1
    endif

  for syllable to nrSyllables
#   Insert boundary: .tierMin, tSBMin[syllable]

    if tFrom[syllable] > tSBMin[syllable]
      Insert boundary: .tierAuto, tFrom[syllable]
      ts[syllable] = tFrom[syllable]
    else
      Insert boundary: .tierAuto, tSBMin[syllable]+0.00005
      ts[syllable] = tSBMin[syllable]
      endif
    if tTo[syllable] < tSBMin[syllable+1]
      Insert boundary: .tierAuto, tTo[syllable]
      te[syllable] = tTo[syllable]
    else
      Insert boundary: .tierAuto, tSBMin[syllable+1]-0.00005
      te[syllable] = tSBMin[syllable+1]
      endif

    d [syllable] = te[syllable] - ts[syllable]
    d#[syllable] = te[syllable] - ts[syllable]

    endfor
# Insert boundary: .tierMin, tSBMin[nrSyllables+1]
  removeObject: .idInt
  endproc

procedure doGlobalAnalyses: .idSnd

# Concatenate all Syllables

  .id# = zero#(nrSyllables)
  for syllable to nrSyllables
    selectObject: .idSnd
    .id#[syllable] = Extract part: ts[syllable], te[syllable], "rectangular", 1, "no"
    endfor
  selectObject: .id#
  .idSndTmp = Concatenate with overlap: 0.01
  removeObject: .id#

# Perform Initial Global Pitch analysis to determine Global Quantile
  selectObject: .idSndTmp
  .idPTmpInit  = noprogress To Pitch (ac): 0.02, 30, 4, "no", 0.03, 0.25, 0.01, 0.35, 0.25, 450
  .qGlobF0Init = Get quantile: 0, 0, 0.5, "Hertz"

# Perform Global Pitch and Formant analysis
  selectObject: .idSndTmp
  .idPTmp = noprogress To Pitch (ac): 0.02, 30, 4, "no", 0.03, 0.25, 0.01, 0.35, 0.25, 2.5 * .qGlobF0Init
  qGlobF0 = Get quantile: 0, 0, 0.5, "semitones re 100 Hz"

  selectObject: .idSndTmp
  .idFmtTmp = noprogress To Formant (burg): 0, 4, 4000 + 4 * (.qGlobF0Init - 100), 0.025, 50
  qGlobF1 = Get quantile: 1, 0, 0, "bark", 0.5
  qGlobF2 = Get quantile: 2, 0, 0, "bark", 0.5
  qGlobF3 = Get quantile: 3, 0, 0, "bark", 0.5
# appendFileLine: "FilledPauses.txt", name$, tab$, "qGlobF0: (",
#..	fixed$(.qGlobF0Init, 1), "/", fixed$(qGlobF0, 1), ")"

  removeObject: .idSndTmp, .idPTmpInit, .idPTmp, .idFmtTmp
  endproc

procedure sdF0: .idSnd
  selectObject: .idSnd

    f0# = zero#(nrSyllables)
   dF0# = zero#(nrSyllables)
  dqF0# = zero#(nrSyllables)
  sdF0# = zero#(nrSyllables)

  .idF0   = noprogress To Pitch (ac): 0.02, 30, 4, "no", 0.03, 0.25, 0.01, 0.35, 0.25, 2.5 * doGlobalAnalyses.qGlobF0Init

  for syllable to nrSyllables
    q50F0 = Get quantile:  ts[syllable], te[syllable], 0.50, "semitones re 100 Hz"
    f0 [syllable] = q50F0
    f0#[syllable] = f0 [syllable]

    dF0 [syllable] = qGlobF0 - q50F0
    dF0#[syllable] = dF0[syllable]

    q95F0 = Get quantile:  ts[syllable], te[syllable], 0.95, "semitones re 100 Hz"
    q05F0 = Get quantile:  ts[syllable], te[syllable], 0.05, "semitones re 100 Hz"
    dqF0 [syllable] = q95F0 - q05F0
    dqF0#[syllable] = dqF0 [syllable]

    sdF0 [syllable] = Get standard deviation: ts[syllable], te[syllable], "semitones"
    sdF0#[syllable] = sdF0 [syllable]
    endfor
  removeObject: .idF0
  endproc

procedure replaceUndefinedF0: .dummy
# small amounts (< 10%) of undefined F0 values are replaced by MEAN without warning
  nrUndef# = zero#(4)
  total#   = zero#(4)
  for syllable to nrSyllables
    if f0#[syllable] == undefined
      nrUndef#[1] = nrUndef#[1] + 1
      listUndefined[1, nrUndef#[1]] = syllable
    else
      total#[1] = total#[1] + f0#[syllable]
      endif
    if dF0#[syllable] == undefined
      nrUndef#[2] = nrUndef#[2] + 1
      listUndefined[2, nrUndef#[2]] = syllable
    else
      total#[2] = total#[2] + dF0#[syllable]
      endif
    if dqF0#[syllable] == undefined
      nrUndef#[3] = nrUndef#[3] + 1
      listUndefined[3, nrUndef#[3]] = syllable
    else
      total#[3] = total#[3] + dqF0#[syllable]
      endif
    if sdF0#[syllable] == undefined
      nrUndef#[4] = nrUndef#[4] + 1
      listUndefined[4, nrUndef#[4]] = syllable
    else
      total#[4] = total#[4] + sdF0#[syllable]
      endif
    endfor
  mean__F0 = total#[1] / (nrSyllables - nrUndef#[1])
  mean_dF0 = total#[2] / (nrSyllables - nrUndef#[2])
  meandqF0 = total#[3] / (nrSyllables - nrUndef#[3])
  meansdF0 = total#[4] / (nrSyllables - nrUndef#[4])
  for syllable to nrUndef#[1]
      f0#[listUndefined[1, syllable]] = mean__F0
    if syllable == 1 and nrUndef#[1] > nrSyllables / 10
      appendInfoLine: "Warning: replaced ", nrUndef#[1], "/'nrSyllables' F0 values by mean ('mean__F0:3') in 'name$'."
      endif
    endfor
  for syllable to nrUndef#[2]
     dF0#[listUndefined[2, syllable]] = mean_dF0
    if syllable == 1 and nrUndef#[2] > nrSyllables / 10
      appendInfoLine: "Warning: replaced ", nrUndef#[2], "/'nrSyllables' dF0 values by mean ('mean_dF0:3') in 'name$'."
      endif
    endfor
  for syllable to nrUndef#[3]
    dqF0#[listUndefined[3, syllable]] = meandqF0
    if syllable == 1 and nrUndef#[3] > nrSyllables / 10
      appendInfoLine: "Warning: replaced ", nrUndef#[3], "/'nrSyllables' dqF0 values by mean ('meandqF0:3') in 'name$'."
      endif
    endfor
  for syllable to nrUndef#[4]
    sdF0#[listUndefined[4, syllable]] = meansdF0
    if syllable == 1 and nrUndef#[4] > nrSyllables / 10
      appendInfoLine: "Warning: replaced ", nrUndef#[4], "/'nrSyllables' sdF0 values by mean ('meansdF0:3') in 'name$'."
      endif
    endfor
  endproc

procedure sdFmt: .idSnd
  selectObject: .idSnd
  .idFmt   = noprogress To Formant (burg): 0, 4, 4000 + 4 * (doGlobalAnalyses.qGlobF0Init - 100), 0.025, 50

    f1# = zero#(nrSyllables)
    f2# = zero#(nrSyllables)
    f3# = zero#(nrSyllables)
   dF1# = zero#(nrSyllables)
   dF2# = zero#(nrSyllables)
   dF3# = zero#(nrSyllables)
  dqF1# = zero#(nrSyllables)
  dqF2# = zero#(nrSyllables)
  dqF3# = zero#(nrSyllables)
  sdF1# = zero#(nrSyllables)
  sdF2# = zero#(nrSyllables)
  sdF3# = zero#(nrSyllables)

  for syllable to nrSyllables
    fs = Get frame number from time: ts[syllable]
    fs = round(fs)
    if fs < 1						; are these frame numbers reliable ?!?
      fs = 1
      endif
    fe = Get frame number from time: te[syllable]
    fe = round(fe)
    f1 [syllable] = Get quantile: 1, ts[syllable], te[syllable], "bark", 0.5
    f2 [syllable] = Get quantile: 2, ts[syllable], te[syllable], "bark", 0.5
    f3 [syllable] = Get quantile: 3, ts[syllable], te[syllable], "bark", 0.5
    f1#[syllable] = f1[syllable]
    f2#[syllable] = f2[syllable]
    f3#[syllable] = f3[syllable]

    dF1[syllable] = 0
    dF2[syllable] = 0
    dF3[syllable] = 0
    for frame from fs to fe
      t   = Get time from frame number: frame
      lF1 = Get value at time: 1, t, "bark", "Linear"
      lF2 = Get value at time: 2, t, "bark", "Linear"
      lF3 = Get value at time: 3, t, "bark", "Linear"
      if lF1 <> undefined
        dF1[syllable] += abs(qGlobF1 - lF1)
        endif
      if lF2 <> undefined
        dF2[syllable] += abs(qGlobF2 - lF2)
        endif
      if lF3 <> undefined
        dF3[syllable] += abs(qGlobF3 - lF3)
        endif
      endfor
    dF1 [syllable] /= (fe-fs+1)
    dF2 [syllable] /= (fe-fs+1)
    dF3 [syllable] /= (fe-fs+1)
    dF1#[syllable]  = dF1[syllable]
    dF2#[syllable]  = dF2[syllable]
    dF3#[syllable]  = dF3[syllable]

    q95F1 = Get quantile: 1, ts[syllable], te[syllable], "bark", 0.95
    q05F1 = Get quantile: 1, ts[syllable], te[syllable], "bark", 0.05
    q95F2 = Get quantile: 2, ts[syllable], te[syllable], "bark", 0.95
    q05F2 = Get quantile: 2, ts[syllable], te[syllable], "bark", 0.05
    q95F3 = Get quantile: 3, ts[syllable], te[syllable], "bark", 0.95
    q05F3 = Get quantile: 3, ts[syllable], te[syllable], "bark", 0.05
    dqF1 [syllable] = q95F1 - q05F1
    dqF2 [syllable] = q95F2 - q05F2
    dqF3 [syllable] = q95F3 - q05F3
    dqF1#[syllable] = dqF1[syllable]
    dqF2#[syllable] = dqF2[syllable]
    dqF3#[syllable] = dqF3[syllable]

    sdF1 [syllable] = Get standard deviation: 1, ts[syllable], te[syllable], "bark"
    sdF2 [syllable] = Get standard deviation: 2, ts[syllable], te[syllable], "bark"
    sdF3 [syllable] = Get standard deviation: 3, ts[syllable], te[syllable], "bark"
    sdF1#[syllable] = sdF1[syllable]
    sdF2#[syllable] = sdF2[syllable]
    sdF3#[syllable] = sdF3[syllable]
    endfor
  removeObject: .idFmt
  endproc

procedure processData: .idTG, .name$, .type$

  if save_Table
    .idTable = Create Table with column names: .name$, 0, "type ts dur durz F0 F0z F1 F1z F2 F2z F3 F3z dF0 dF0z dF1 dF1z dF2 dF2z dF3 dF3z
...		dqF0 dqF0z dqF1 dqF1z dqF2 dqF2z dqF3 dqF3z sdF0 sdF0z sdF1 sdF1z sdF2 sdF2z sdF3 sdF3z score"
  else
    .idTable = 0
    endif

  if .type$ == "Auto"
    mean_d    =  mean(   d#)
      sd_d    = stdev(   d#)
     mean_F0  =  mean(  f0#)
       sd_F0  = stdev(  f0#)
     mean_F1  =  mean(  f1#)
       sd_F1  = stdev(  f1#)
     mean_F2  =  mean(  f2#)
       sd_F2  = stdev(  f2#)
     mean_F3  =  mean(  f3#)
       sd_F3  = stdev(  f3#)
    mean_dF0  =  mean( dF0#)
      sd_dF0  = stdev( dF0#)
    mean_dF1  =  mean( dF1#)
      sd_dF1  = stdev( dF1#)
    mean_dF2  =  mean( dF2#)
      sd_dF2  = stdev( dF2#)
    mean_dF3  =  mean( dF3#)
      sd_dF3  = stdev( dF3#)
    mean_dqF0 =  mean(dqF0#)
      sd_dqF0 = stdev(dqF0#)
    mean_dqF1 =  mean(dqF1#)
      sd_dqF1 = stdev(dqF1#)
    mean_dqF2 =  mean(dqF2#)
      sd_dqF2 = stdev(dqF2#)
    mean_dqF3 =  mean(dqF3#)
      sd_dqF3 = stdev(dqF3#)
    mean_sdF0 =  mean(sdF0#)
      sd_sdF0 = stdev(sdF0#)
    mean_sdF1 =  mean(sdF1#)
      sd_sdF1 = stdev(sdF1#)
    mean_sdF2 =  mean(sdF2#)
      sd_sdF2 = stdev(sdF2#)
    mean_sdF3 =  mean(sdF3#)
      sd_sdF3 = stdev(sdF3#)
  endif

# z-transform data

  dz#    = ( d#   - mean_d   ) / sd_d
   f0z#  = (  f0# - mean_F0  ) / sd_F0
   f1z#  = (  f1# - mean_F1  ) / sd_F1
   f2z#  = (  f2# - mean_F2  ) / sd_F2
   f3z#  = (  f3# - mean_F3  ) / sd_F3
  dF0z#  = ( dF0# - mean_dF0 ) / sd_dF0
  dF1z#  = ( dF1# - mean_dF1 ) / sd_dF1
  dF2z#  = ( dF2# - mean_dF2 ) / sd_dF2
  dF3z#  = ( dF3# - mean_dF3 ) / sd_dF3
  dqF0z# = (dqF0# - mean_dqF0) / sd_dqF0
  dqF1z# = (dqF1# - mean_dqF1) / sd_dqF1
  dqF2z# = (dqF2# - mean_dqF2) / sd_dqF2
  dqF3z# = (dqF3# - mean_dqF3) / sd_dqF3
  sdF0z# = (sdF0# - mean_sdF0) / sd_sdF0
  sdF1z# = (sdF1# - mean_sdF1) / sd_sdF1
  sdF2z# = (sdF2# - mean_sdF2) / sd_sdF2
  sdF3z# = (sdF3# - mean_sdF3) / sd_sdF3

  for syllable to nrSyllables
    selectObject: .idTG

    scoreUK =  4.73 * sqrt(   d[syllable]) - 0.29 * f0z#[syllable]
...          - 0.32 * sqrt(sdF1[syllable]) - 0.10 * sqrt(dF1[syllable])
...          - 1.38 * sqrt(sdF2[syllable]) - 0.80 * sqrt(dF2[syllable])
...          - 0.20 * (f2[syllable] - f1[syllable])
...          + 0.31 *  f3[syllable]

    scoreNL =  8.62 * sqrt(   d[syllable]) - 0.36 * f0z#[syllable]
...                                        - 0.72 * sqrt(dF1[syllable])
...          - 1.36 * sqrt(sdF2[syllable]) - 1.62 * sqrt(dF2[syllable])
...          - 1.02 * sqrt(sdF3[syllable])
...          - 0.11 * (f2[syllable] - f1[syllable])
...          + 0.21 *  f3[syllable]

    lbl2$ = Get label of interval: setSB.tierAuto, 2*syllable

    if   language$ == "English"
      score = scoreUK
      if  score > 3.4942 * filled_Pause_threshold
        lbl2$ += "fp"
        endif
    elif language$ == "Dutch"
      score = scoreNL
      if score > 2.7094 * filled_Pause_threshold
        lbl2$ += "fp"
        endif
    else
      exitScript: "Language not supported."
      endif

    if .type$ == "Auto"
      type$ [syllable] = lbl2$
      Set interval text: setSB.tierAuto,  2*syllable, lbl2$
#     Set interval text: setSB.tierAuto,  2*syllable, fixed$(score, 3)
      endif

    if save_Table
      selectObject: .idTable
      Append row
      row = Get number of rows

      Set string value: row, "type" ,          type$ [syllable]
      Set string value: row,    "ts",   fixed$(ts    [syllable], 3)
      Set string value: row,  "dur" ,   fixed$( d    [syllable], 3)
      Set string value: row,  "durz",   fixed$( dz#  [syllable], 3)
      Set string value: row,   "F0" ,   fixed$(  f0  [syllable], 3)
      Set string value: row,   "F0z",   fixed$(  f0z#[syllable], 3)
      Set string value: row,   "F1" ,   fixed$(  f1  [syllable], 3)
      Set string value: row,   "F1z",   fixed$(  f1z#[syllable], 3)
      Set string value: row,   "F2" ,   fixed$(  f2  [syllable], 3)
      Set string value: row,   "F2z",   fixed$(  f2z#[syllable], 3)
      Set string value: row,   "F3" ,   fixed$(  f3  [syllable], 3)
      Set string value: row,   "F3z",   fixed$(  f3z#[syllable], 3)
      Set string value: row,  "dF0" ,   fixed$( dF0  [syllable], 3)
      Set string value: row,  "dF0z",   fixed$( dF0z#[syllable], 3)
      Set string value: row,  "dF1" ,   fixed$( dF1  [syllable], 3)
      Set string value: row,  "dF1z",   fixed$( dF1z#[syllable], 3)
      Set string value: row,  "dF2" ,   fixed$( dF2  [syllable], 3)
      Set string value: row,  "dF2z",   fixed$( dF2z#[syllable], 3)
      Set string value: row,  "dF3" ,   fixed$( dF3  [syllable], 3)
      Set string value: row,  "dF3z",   fixed$( dF3z#[syllable], 3)
      Set string value: row, "dqF0" ,   fixed$(dqF0  [syllable], 3)
      Set string value: row, "dqF0z",   fixed$(dqF0z#[syllable], 3)
      Set string value: row, "dqF1" ,   fixed$(dqF1  [syllable], 3)
      Set string value: row, "dqF1z",   fixed$(dqF1z#[syllable], 3)
      Set string value: row, "dqF2" ,   fixed$(dqF2  [syllable], 3)
      Set string value: row, "dqF2z",   fixed$(dqF2z#[syllable], 3)
      Set string value: row, "dqF3" ,   fixed$(dqF3  [syllable], 3)
      Set string value: row, "dqF3z",   fixed$(dqF3z#[syllable], 3)
      Set string value: row, "sdF0" ,   fixed$(sdF0  [syllable], 3)
      Set string value: row, "sdF0z",   fixed$(sdF0z#[syllable], 3)
      Set string value: row, "sdF1" ,   fixed$(sdF1  [syllable], 3)
      Set string value: row, "sdF1z",   fixed$(sdF1z#[syllable], 3)
      Set string value: row, "sdF2" ,   fixed$(sdF2  [syllable], 3)
      Set string value: row, "sdF2z",   fixed$(sdF2z#[syllable], 3)
      Set string value: row, "sdF3" ,   fixed$(sdF3  [syllable], 3)
      Set string value: row, "sdF3z",   fixed$(sdF3z#[syllable], 3)
      Set string value: row, "score",   fixed$(score,            3)
      endif
    endfor
  endproc

